def Number(n): #hàm phân loại deficient, perfect, abundant
    s = 0#khởi tạo tổng bằng 0 
    for i in range(1,n//2+1): #vòng lặp i chạy trong khoảng 1 đến ước lớn nhất !1 của số n để rút gọn vòng lặp 
        if n % i == 0: #nếu n chia hết cho số bất kì trong khoảng trên thì tổng sẽ bằng các số đấy cộng lại
             s += i
    if s < n: #nếu tổng đó nhỏ hơn n thì...
        return"is deficeient!"
    elif s == n: #tổng đó bằng n thì...
        return"is perfect!"
    else:
        return"is abundant :))))"


def ktra_number(x,y): #tạo hàm kiểm tra các số trong khoảng x,y
    for i in range(x,y + 1): #cho biến i chạy trong khoảng từ x tới y tính cả x,y
        ktra_number = Number(i) #hàm ktra sẽ bằng hàm phân loại với biến i thay vì biến n
        print(f" {i} la {ktra_number}") #in ra

print(f"nhap vao khoang x,y muon kiem tra voi x<=y: ")
x = int(input())
y = int(input()) 
ktra_number(x,y) #gọi lại hàm kiểm tra để in ra màn hình
