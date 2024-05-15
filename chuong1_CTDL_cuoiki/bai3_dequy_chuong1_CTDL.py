print(f"nhap gia tri a va b: ")
a = int(input()) #nhập vào số nguyên dương a sao cho a lớn hơn b
b = int(input()) #nhập vào số nguyên dương b
def gcd_recursive(a,b): #tạo hàm tìm ước chung lớn nhất không dùng đệ quy
    while b!= 0: #trong khi số nhập vào là b không phải bằng không
        temp = b #gán b cho một biến đến tạm
        b = a % b
        a = temp
    return a

print(f"uocchung lon nhat cua hai so a va b la: " ,gcd_recursive(a,b))