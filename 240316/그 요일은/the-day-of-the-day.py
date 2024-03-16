m1, d1, m2, d2 = tuple(map(int,input().split()))
A = input()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cnt_days(x, y):
    cnt = 0
    for i in range(1, x):    
        cnt += num_of_days[i]
    return cnt+y

diff = cnt_days(m2, d2) - cnt_days(m1, d1)

num_of_weeks = diff//7 + 1
end_of_day = days[diff%7]

if days.index(end_of_day) < days.index(A):
    print(num_of_weeks-1)
else:
    print(num_of_days)