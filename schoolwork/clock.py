import re

def getct(time):
    pattern = r'^([01]\d|2[0-3]):([0-5]\d)$'
    if re.match(pattern, time):
        h, m = int(time.split(":")[0]), int(time.split(":")[1])
        if m>0:
            return f"{str(60-m).zfill(2)}:{str(11-h).zfill(2)}"
        else:
            return f"{str(12-h).zfill(2)}:{str(m).zfill(2)}"
    else:
        return 
try:
    while(1):
        print(getct(input()))
except EOFError as e:
   print(end="")

