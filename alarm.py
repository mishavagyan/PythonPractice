# Alarm clock
import time
import datetime
invalid = True
alarmTime = []
while invalid:
    t = input("please input time when you want to set alarm like this\n00:00\n")
    try:
        alarmTime = [int(n) for n in t.split(":")]
    except ValueError:
        print("Invalid time!!!!")
    if 0 <= alarmTime[0] <= 23 and 0 <= alarmTime[1] <= 59:
        invalid = False

alarmSeconds = alarmTime[0] * 3600 + alarmTime[1] * 60
now = datetime.datetime.now()
currSeconds = now.hour * 3600 + now.minute * 60 + now.second
secondsUntilAlarm = alarmSeconds - currSeconds
if secondsUntilAlarm < 0:
    secondsUntilAlarm += 86400

print("Alarm is set!")
print("The alarm will ring at %s" % datetime.timedelta(seconds=secondsUntilAlarm))

for i in range(0, secondsUntilAlarm):
    time.sleep(1)
    secondsUntilAlarm -= 1
    if secondsUntilAlarm <= 20:
        print(datetime.timedelta(seconds=secondsUntilAlarm))
print("Ring Ring... time to wake up!")
