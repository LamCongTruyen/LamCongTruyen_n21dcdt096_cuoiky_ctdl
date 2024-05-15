a = int(input()) #nhập vào số a(a phải lớn hơn b)
b = int(input()) #nhập vào số b
def gcdrecursive(a,b):#tạo hàm tìm ước lớn nhất với hai biến đã nhập vào là a và b
    if b == 0: #nếu b bằng 0 thì trả về giá trị của a(a chính là ước lớn nhất)
        return a
    else:#nếu khác 
        return gcdrecursive(b, a % b)#thực hiện đệ quy bằng cách gọi lại chính nó với ai tham số là b và phần dư của phép chia a,b
    
c = gcdrecursive(a,b)#gán giá trị hàm gcdrecursive(a,b) vào biến c
print(f"Uoc chung lon nhat cua hai so {a} va {b} la: {c}")#in ra màn hình