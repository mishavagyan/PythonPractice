"""
Implement a function that works the same as str.split method
(without using str.split itself, ofcourse).
Pay attention to strings with multiple spaces.
"""

def split(data: str, sep=None, maxsplit=-1):
    res = []
    i = 0
    data_length = len(data)
    if sep is None:
        while i < data_length:
            s = ""
            while i < data_length and not data[i].isspace():
                s += data[i]
                i += 1
            if s != "":
                res.append(s)
            while i < data_length and data[i].isspace():
                i += 1
            if maxsplit != -1 and len(res) == maxsplit:
                if i < data_length:
                    res.append(data[i:])
                break
    else:
        sep_len = len(sep)
        while i < data_length:
            s = ""
            sep_index = data.find(sep, i)
            if sep_index == -1 or (maxsplit != -1 and maxsplit == len(res)):
                res.append(data[i:])
                break
            while i < data_length and i != sep_index:
                s += data[i]
                i += 1
            res.append(s)
            s = ""
            if sep_index != -1 and i == sep_index:
                i += sep_len
                if i >= data_length:
                    res.append(s)
    return res

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']