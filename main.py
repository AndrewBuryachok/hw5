import math

mode = True

al = 2
bt = 228
p = 383
n = 191

X = [1]
A = [0]
B = [0]

def check_x(xi):
    if mode:
        if xi % 3 == 1:
            return 1
        if xi % 3 == 0:
            return 2
        if xi % 3 == 2:
            return 3
    else:
        if 0 <= xi and xi < p / 3:
            return 1
        if p / 3 <= xi and xi < 2 * p / 3:
            return 2
        if 2 * p / 3 <= xi and xi < p:
            return 3

def get_equal(xi):
    for i in range(len(X) - 1):
        if X[i] == xi:
            return i
    return -1

def calc(i, j):
    print("calc for i =", i, "j =", j, "value =", X[i])
    r = (B[int(i / 2)] - B[i]) % n
    print("r =", r)
    if r == 0:
        print("ERROR")
        return 1
    b = A[i] - A[int(i / 2)]
    d = math.gcd(r, n)
    if b % d == 0:
        new_n = int(n / d)
        new_b = int(b / d)
        new_r = int(r / d)
        res = (new_b * pow(new_r, -1, new_n)) % new_n
        res_X = []
        for i in range(d):
            x = res + i * new_n
            res_X.append(x)
        print("all candedats =", res_X)
        print("answers")
        stop = False
        for x in res_X:
            if pow(al, x, p) == bt:
                print("super final x =", x)
                stop = True
                break
        if stop:
            return 1
    else:
        print("ERROR")
    return 0

i = 1
while True:
    print("i =", i)
    s = check_x(X[-1])
    print("s =", s)
    if s == 1:
        A.append(A[-1])
        B.append((B[-1] + 1) % n)
    if s == 2:
        A.append((2 * A[-1]) % n)
        B.append((2 * B[-1]) % n)
    if s == 3:
        A.append((A[-1] + 1) % n)
        B.append(B[-1])
    X.append((al ** A[-1] * bt ** B[-1]) % p)
    print("a =", A[-1])
    print("b =", B[-1])
    print("x =", X[-1])
    print("all x =", X, "len =", len(X))
    if mode:
        j = get_equal(X[-1])
        if j != -1:
            if calc(len(X) - 1, j):
                break
    else:
        if i % 2 == 0 and i != 0:
            print("check", X[i], X[int(i / 2)])
            if X[i] == X[int(i / 2)]:
                if calc(i, int(i / 2)):
                    break
    i += 1
    print()
