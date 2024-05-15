n = int(input())#nhap so n nguyen duong n>=0
def Fibonacci(n):#khoi tao ham tính Fibnacci với biến n
    if n ==1 or n == 2:#đặt điều kiện dừng cho hàm đệ quy
        return 1#trả về 1 nếu số n nhập vào là 1 hoặc 2
    else:#nếu chưa thõa điều kiện
        return Fibonacci(n-1) + Fibonacci(n-2)#trả về n = (n-1)+(n-2)
    
a = Fibonacci(n)#gán giá trị của hàm Fibonacci cho biến a
print(f"gia tri cua so Fibonacci thu {n} la: ")#in ra màn hình thông điệp
print(a) #in giá trị của biến a ra màn hình  


