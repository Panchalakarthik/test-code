def validate(s, valid):
    while(s!=0):
        if str(s%10) not in valid:
            return False
        s = s//10
    return True

num = int(input())

valid = "0125689"

c = 0
s = 0

while(c != num):
    if validate(s, valid):
        c+=1
    s += 1
print(s)

