str_1 = input()
str_2 = input()

last_char = str_2[-1]
ans = 0

for i in str_1:
    if i == last_char:
        ans += 1
        
print(ans)