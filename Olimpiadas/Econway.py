n = int(input())
for i in range(n):
    f,c = map(int, input().split())
    x = [ map(list(e).append(input().split())) for e in range(f)]


"""resultat = pestat(x, f, c)
for e in range(f):
    print("").join(e)    """