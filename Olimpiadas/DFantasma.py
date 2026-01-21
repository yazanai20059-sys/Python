t = int(input())

for _ in range(t):
    libros = []
    fantasma = False

    for x in map(int, input().split()):
        if x > 0:
            libros.append(x)
        if x < 0:
            if not libros or libros[-1] != -x:
                fantasma = True
            else:
                libros.pop()

    if fantasma or libros:
        print("PARANORMAL")
    else:
        print("NORMAL")
