#Viết chương trình có các hàm sau:
##a, Hàm kiểm tra 1 số tự nhiên có phải số nguyên tố hay không?
##b, Hàm in ra các số nguyên tố <= n. Sử dụng hàm ở câu a.
##c, Hàm tìm số NT nhỏ nhất > n.
def LaSNT(n):
    #Nếu n <2 thì không phải SNT
    if n < 2: return False
    #nếu n>= 2: nếu trong đoạn [2,n//2] có 1 ước số của n thì n không phải SNT
    for i in range(2, n//2 +1):
        if n % i == 0: return False
    #Nếu không phải 2 trường hợp trên -> n là SNT
    return True
def InSNT(n):
    for i in range(2, n + 1):
        if LaSNT(i):
            print(i, end=' ')
def TimSNT(n):
    i = n + 1
    while not LaSNT(i):
        i += 1
    return i

#Chuong trinh chinh
if __name__ == '__main__':
    n= 37
    print(LaSNT(n))
    print('Cac so nguyen to <= %d la' % (n))
    InSNT(n)
    print("\nSo nguyen to nho nhat > {} la {}".format(n,TimSNT(n)))