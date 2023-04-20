import re

def time(time_in_mirror):
    pattern = r'^([01]\d|2[0-3]):([0-5]\d)$'
    if not re.match(pattern, time_in_mirror):
        return
    
    hour = int(time_in_mirror[0:2])
    minute = int(time_in_mirror[3:5])
    
    if hour < 11:
      hour1 = 11 - hour
    else:
      hour1 = 23 - hour

    minute1 = 60 - minute
    if minute1 == 60:
      minute1 -=60
      hour1 += 1
    if hour1 > 12:
      hour1 -=12
    ans = ""
    if hour1 > 9 :
      ans = str(hour1) + ':'
    else:
      ans = '0' + str(hour1) + ':'

    if minute1 > 9:
      ans += str(minute1)
    else:
      ans += '0' + str(minute1)
    print(ans)

try:
    while(1):
        time(input())
except EOFError as e:
   print(end="")
