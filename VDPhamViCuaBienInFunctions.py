def MyFunc(n):
    x =100
#Thu doc gia tri bien x
#print ('x=%d'%x)

def MyFunc2():
    global x2
    x2=100

#Goi ham MyFunc
MyFunc2()

#thu doc gia tri bien x2
print('x2=%d'%x2)

