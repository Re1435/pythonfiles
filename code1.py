alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
ind = 0
count = 1
for i in range(1,n+1):
    left_spaces = " " * (n-i)
    hollow_spaces = " " * (count)
    if i == 1:
        pattern = left_spaces + alphas[ind]
        print(pattern)
        ind += 1
    else:
        pattern = left_spaces + alphas[ind] + hollow_spaces + alphas[ind+1]
        print(pattern)
        count += 2
        ind += 2
ind = ind
re_ind = ind - 2
count = count
re_count = count - 2
for i in range(1,n):
    left_spaces = " " * (i)
    if i == n-1:
        pattern = left_spaces + alphas[re_ind-1]
        print(pattern)
    else:
        re_count -= 2
        re_ind -= 2
        hollow_spaces = " " * (re_count)
        pattern = left_spaces + alphas[re_ind] + hollow_spaces + alphas[re_ind+1]
        print(pattern)
        