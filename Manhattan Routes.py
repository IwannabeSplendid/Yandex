def coordinates(route, t, d):
    up, down, right, left = (0,0,0,0)
    for i in route:
        upNew = i[0] - i[1] - d
        downNew = i[0] - i[1] + d
        rightNew = i[0] + i[1] + d
        leftNew = i[0] + i[1] - d

        up = max(up-t,upNew)
        down = min(down+t, downNew)
        right = min(right+t, rightNew)
        left = max(left-t, leftNew)

    return printCoor(up, down, right, left)

def printCoor(u,d,r,l):
    coordin = []
    for _ in range(d-u+1):
        rTemp = r
        for _ in range(r-l+1):
            cUp = [(u + rTemp) // 2, (rTemp - u) // 2]
            if ((u + rTemp) % 2 == 0):
                coordin.append(cUp)
            rTemp -= 1
        u += 1
    return coordin

def main():
    t, d, n = map(int, input().split())
    route=[]

    for _ in range(n):
        x, y = map(int, input().split())
        route.append((x, y))

    results = coordinates(route, t, d)
    print(len(results))
    for i in results:
        print(i[0], i[1])

if __name__ == '__main__':
    main()





