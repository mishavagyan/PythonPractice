from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import json as js
import html


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    ar = []
    i = 0
    while i < len(xml):
        tag = ""
        if xml[i] == "<":
            while i < len(xml) and xml[i] != ">":
                tag += xml[i]
                i += 1
            if i < len(xml):
                tag += xml[i]
                i += 1
        else:
            while i < len(xml) and xml[i] != "<":
                tag += xml[i]
                i += 1
        ar.append(tag)

    res = {
        "title": None,
        "link": None,
        "lastBuildDate": None,
        "pubDate": None,
        "language": None,
        "category": [],
        "managingEditor": None,
        "description": None,
    }

    item_order = ["title", "author", "pubDate", "link", "category", "description"]
    items = []
    item_index = 0
    in_item = False
    item_data = None

    for i in range(len(ar)):
        if limit and item_index == limit:
            break
        if ar[i] == "<channel>":
            continue
        if ar[i] == "</channel>":
            break
        if ar[i] == "<item>":
            in_item = True
            item_data = {}
            for key in item_order:
                if key == "category":
                    item_data[key] = []
                else:
                    item_data[key] = None
        elif ar[i] == "</item>":
            in_item = False
            items.append(item_data)
            item_index += 1

        if not in_item:
            if ar[i] == "<title>" and i + 1 < len(ar):
                res["title"] = html.unescape(ar[i + 1])
            elif ar[i] == "<link>" and i + 1 < len(ar):
                res["link"] = html.unescape(ar[i + 1])
            elif ar[i] == "<lastBuildDate>" and i + 1 < len(ar):
                res["lastBuildDate"] = html.unescape(ar[i + 1])
            elif ar[i] == "<pubDate>" and i + 1 < len(ar):
                res["pubDate"] = html.unescape(ar[i + 1])
            elif ar[i] == "<language>" and i + 1 < len(ar):
                res["language"] = html.unescape(ar[i + 1])
            elif ar[i] == "<category>" and i + 1 < len(ar):
                if "category" in res:
                    res["category"].append(html.unescape(ar[i + 1]))
                else:
                    res["category"] = [html.unescape(ar[i + 1])]
            elif ar[i] == "<managingEditor>" and i + 1 < len(ar):
                res["managingEditor"] = html.unescape(ar[i + 1])
            elif ar[i] == "<description>" and i + 1 < len(ar):
                res["description"] = html.unescape(ar[i + 1])

        elif in_item:
            if ar[i] == "<title>" and i + 1 < len(ar):
                item_data["title"] = html.unescape(ar[i + 1])
            elif ar[i] == "<author>" and i + 1 < len(ar):
                item_data["author"] = html.unescape(ar[i + 1])
            elif ar[i] == "<pubDate>" and i + 1 < len(ar):
                item_data["pubDate"] = html.unescape(ar[i + 1])
            elif ar[i] == "<link>" and i + 1 < len(ar):
                item_data["link"] = html.unescape(ar[i + 1])
            elif ar[i] == "<category>" and i + 1 < len(ar):
                if "category" in item_data:
                    item_data["category"].append(html.unescape(ar[i + 1]))
                else:
                    item_data["category"] = [html.unescape(ar[i + 1])]
            elif ar[i] == "<description>" and i + 1 < len(ar):
                item_data["description"] = html.unescape(ar[i + 1])

    result = []
    if res["title"]:
        result.append(f"Feed: {res['title']}")
    else:
        del res["title"]
    if res["link"]:
        result.append(f"Link: {res['link']}")
    else:
        del res["link"]
    if res["lastBuildDate"]:
        result.append(f"Last Build Date: {res['lastBuildDate']}")
    else:
        del res["lastBuildDate"]
    if res["pubDate"]:
        result.append(f"Publish Date: {res['pubDate']}")
    else:
        del res["pubDate"]
    if res["language"]:
        result.append(f"Language: {res['language']}")
    else:
        del res["language"]
    if res["category"]:
        result.append(f"Categories: {', '.join(res['category'])}")
    else:
        del res["category"]
    if res["managingEditor"]:
        result.append(f"Editor: {res['managingEditor']}")
    else:
        del res["managingEditor"]
    if res["description"]:
        result.append(f"Description: {res['description']}")
    else:
        del res["description"]

    # Add items
    for item in items:
        if "title" in item:
            if item["title"]:
                result.append(f"Title: {item['title']}")
            else:
                del item['title']
        if "author" in item:
            if item["author"]:
                result.append(f"Author: {item['author']}")
            else:
                del item['author']
        if "pubDate" in item:
            if item["pubDate"]:
                result.append(f"Published: {item['pubDate']}")
            else:
                del item["pubDate"]
        if "link" in item:
            if item["link"]:
                result.append(f"Link: {item['link']}")
            else:
                del item["link"]
        if "category" in item:
            if item["category"]:
                result.append(f"Categories: {', '.join(item['category'])}")
            else:
                del item["category"]
        if "description" in item:
            if item["description"]:
                result.append(f"\n{item['description']}")
            else:
                del item["description"]

    if items:
        res["items"] = items

    if json:
        result = js.dumps(res, indent=4)
        result = [result]

    return result


def main(argv: Optional[Sequence] = None):
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )
    args = parser.parse_args(argv)
    xml = requests.get(args.source).text

    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
