n = int(input())
for i in range(n):
    s = int(input())
    s = input()
    l = s.split()
    l2=[]
    for e in l:
        l2.append(int(e))
    l2.sort()
    m =l2[-1:]
    q = l2.count(m[0])
    print(m[0],q)