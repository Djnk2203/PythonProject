#Tạo module tự định nghĩa và sử dụng
##Bước 1: Tạo 1 thư mục đặt tên tùy ý, chẳng hạn 'my_lib'
###Trong thư mục này phải tạo file có tên '_init.py_', file này không cần có mã nguồn
##Bước 2: Trong thư mục 'my_lib' tạo file mã nguồn, chẳng hạn 'functions.py' chức các thành phần tự cài đặt
##Bước 3: Sử dụng module tự định nghĩa
###Tạo file mã nguồn Python mới
####Thêm dòng khai báo
#import from my_lib import funcitons

from my_lib.functions import *

SayHi("Nha Trang")