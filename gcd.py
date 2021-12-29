def gcd(a, b):
    naj = 0
    rez = 0
    if a > b:
        naj = a
    else:
        naj = b
    for i in range(1, naj):
        if a%i == 0 and b%i == 0:
            rez = i
    print(f"GCD({a}, {b}) = {rez}")
    return rez

def veljaven_LDE(a, b, deljiv):
    if deljiv%gcd(a, b) == 0:
        print("LDE je veljaven")
    else:
        print("LDE ni veljaven")

veljaven_LDE(43 , 7, 8)


