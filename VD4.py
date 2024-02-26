#Danh sách các số chẵn liên tiếp từ 1->100
#Sử dụng Python For Comprehension
myList = [i for i in range(1, 101)]
print(myList)

#Danh sách các số lẻ liên tiếp từ 1->100
myOddNumbers = [i for i in range(1, 101) if i % 2 != 0]
print(myOddNumbers)