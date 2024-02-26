# nhap 1 so nguyen 0<n<=1000
# a kiem tra n cos phai so nguyen to
# b In ra cac so nguyento <=n
while True:
    n = int(input("Nhap so nguyen n:"))
    if 0 < n <= 1000:
        break


def LaSNT(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


# a
if LaSNT(n):
    print("{} la so nguyen to".format(n))
else:
    print("{} khong phai la so nguyen to".format(n))

# b
print("Cac so nguyen to <= {}:".format(n))
for i in range(2, n + 1):
    if LaSNT(i):
        print("%d" % i, end =" ")
