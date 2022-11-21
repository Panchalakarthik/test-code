inp_mat = []

for i in range(256):
    row = list(map(int,input().split()))
    inp_mat.append(row)

x1 = 256
x2 = 0
y1 = 256
y2 = 0


end_row = len(inp_mat)
end_col = len(inp_mat[0])

for i in range(0,end_row):
    start = 0
    while(start < end_col):
        if (inp_mat[i][start] == 0):
            y1 = min(y1,start)
            break
        start+=1
    
    end = end_col - 1
    while(end >=0 ):
        if(inp_mat[i][end] == 0):
            y2 = max(end,y2)
            break
        end -= 1

    start_top = 0
    while(start_top < end_row):
        if (inp_mat[start_top][i] == 0):
            x1 = min(x1,start_top)
            break
        start_top+=1

    end_bottom = end_row - 1
    while(end_bottom >= 0):
        if (inp_mat[end_bottom][i] == 0):
            x2 = max(x2,end_bottom)
            break
        end_bottom-=1

print((x1,y1),(x1,y2),(x2,y1),(x2,y2))