def gcd(a, b, x, y):
    if b == 0:
        return (a, 1, 0)
    d, x, y = gcd(b, a % b, 0, 0)
    x -= (a // b) * y
    y, x = x, y
    return (d, x ,y)


def find_solution(a, b, c, x0, y0, g):
    g, x0, y0 = gcd(abs(a), abs(b), x0, y0)
    x0 *= c // g
    y0 *= c // g
    return (g, x0, y0)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    d, x, y = find_solution(a, b, c, 0, 0, 0)
    if c % d == 0:
        while x - b // d > 0:
            x -= b // d
            y += a // d

        while (x < 0):
            x += b // d
            y -= a // d
        print(x, y)
    else:
        print(0,0)

