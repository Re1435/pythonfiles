n = int(input())  # reading input
for i in range(n):  # upper part
    left_space = ' '*(n-i-1)  # (5-0-1) = (4)
    hollow_space = ' '*(2*i)  # (0)
    print(left_space+"/"+hollow_space+"\\")
for j in range(n):  # lower part
    left_space = ' '*(j)  # 0,1,2,3,4
    hollow_space = ' '*(2*(n-j-1))  # (2*(5-0-1))=(2(4))=8
    print(left_space+"\\"+hollow_space+"/")
