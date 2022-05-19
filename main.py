import math

al = 2
bt = 228
p = 383
n = 191

X = [1]
A = [0]
B = [0]

def check_x(xi):
    if xi % 3 == 0:
        return 1
    if xi % 3 == 1:
        return 2
    if xi % 3 == 2:
        return 3
    '''if 0 <= xi and xi < p / 3:
        return 1
    if p / 3 <= xi and xi < 2 * p / 3:
        return 2
    if 2 * p / 3 <= xi and xi < p:
        return 3'''

i = 1
while True:
    print("i =", i)
    check = check_x(X[-1])
    print("s =", check)
    if check == 1:
        A.append(A[-1])
        B.append((B[-1] + 1) % n)
    if check == 2:
        A.append((2 * A[-1]) % n)
        B.append((2 * B[-1]) % n)
    if check == 3:
        A.append((A[-1] + 1) % n)
        B.append(B[-1])
    X.append((al ** A[-1] * bt ** B[-1]) % p)
    print("a =", A[-1])
    print("b =", B[-1])
    print("x =", X[-1])
    print("all x =", X, "len =", len(X))
    if i % 2 == 0 and i != 0:
        print("check", X[i], X[int(i / 2)])
        if X[i] == X[int(i / 2)]:
            r = (B[int(i / 2)] - B[i]) % n
            print("r =", r)
            if r == 0:
                print("ERROR")
                break
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
                    break
            else:
                print("ERROR")
    i += 1
    print()
