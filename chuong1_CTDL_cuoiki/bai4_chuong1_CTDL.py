print(f"nhap gia tri n: ")
n = int(input())  #nhập vào giá trị n 
def tinh_to_hop(n, k): #tạo hàm tính tổ hợp Cn/k
    if k == 0 or k == n: #theo công thức tính hàm pascal thì khi k=0 và khi k=0 thì C0/n và Cn/n bằng 1
        return 1
    return tinh_to_hop(n - 1, k - 1) + tinh_to_hop(n - 1, k) #nếu k khác n thì Ck/n=Ck-1/n-1 + Ck/n-1

def Pascal(n):
    for i in range(n + 1): #vòng lặp cho biến i chạy trong vùng giá trị của n 
        for j in range(i + 1):
            print(tinh_to_hop(i, j),end=" ") #in ra giá trị của Cn/k, môi lần in sẽ in thêm 1 khoảng trống
        print() #in thêm một khoảng cách xuống dòng để dễ nhìn thấy
print(f"tam giac Pascal la: ")
Pascal(n) 
