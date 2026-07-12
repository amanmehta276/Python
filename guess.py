def max_guests(entry, exit):
    curr = 0
    ans = 0

    for i in range(len(entry)):
        curr += entry[i]
        curr -= exit[i]

        ans = max(ans, curr)

    return ans


entry = [7, 0, 5, 1, 3]
exit = [1, 2, 1, 3, 4]

print(max_guests(entry, exit))

'''
i=0
curr=7
curr=6
ans=6
i=1
curr=6,4
ans=6

i=2
curr=9,8
ans=8

i=3
curr=9,6
ans=8

i=4
curr=9,5
ans=8
'''