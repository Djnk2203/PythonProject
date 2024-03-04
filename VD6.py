#Mot may ATM cos cac loai tien 100,20 va 5 USD.Mot nguoi can rut so tien m.
##a, Tim phuong an rut tot nhat (co it to tien nhat)
###b, Liet ke tat ca cac cach rut duoc so tien m. co tat ca bao nhieu cach

#Lap lai nhap so tien den khi thoa dieu kien
while True:
    m = int(input("Nhap so tien rut: "))
    if m <= 0 or m % 5 !=0:
        print("So tien khong thoa man.")
    else:
        break
#lưu lại số tiền m ban đầu
m1 = m
##a - Tim phuong an tot nhat
##Cach lam: uu tien rut menh gia tien cao truoc
soTo100 = m //100   #chia lay phan nguyen
m = m % 100         #So tien con lai
soTo20 = m //20
m = m % 20          #So tien con lai
soTo5 = m // 5
#In ket qua
print("Phuong an rut tien tot nhat: ")
print("{} to 100 + {} to 20 + {} to 5".format(soTo100,soTo20,soTo5))

##b - Liet ke tat ca cac cach rut tien
m= m1   #lay lai gia tri ban dau
soCach = 0
for soTo100 in range(m // 100 + 1):
    for soTo20 in range(m // 20 + 1 ):
        for soTo5 in range (m // 5+1 ):
            if soTo100 * 100 + soTo20 * 20 + soTo5 * 5 == m:
                soCach += 1
                print("{}: {} to 100 + {} to 20 + {} to 5.".format( soCach, soTo100, soTo20, soTo5))

print("Co tat ca {} cach rut".format(soCach))