def base_3(num):
    ans = ""

    while(num!=0):
        ans = str(num%3) + ans
        num = num // 3

    return ans

num = int(input())

print(base_3(num))