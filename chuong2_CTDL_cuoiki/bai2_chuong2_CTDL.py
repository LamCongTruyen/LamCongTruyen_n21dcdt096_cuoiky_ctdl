def TrungHang(mang):
    n = len(mang)
    
    # Duyệt qua từng cặp hàng
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if mang[i] == mang[j]:
    for j in range(len(mang[0])):
        for row in mang:
            if row[j] != row[j+1]:
                return True
                
    return False

# Sử dụng hàm kiểm tra
mang1 = [[1, 2, 1],
         [4, 5, 4],
         [1, 3, 1]]

mang2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print("Mang 1 co it nhat hai hang giong nhau khong:", TrungHang(mang1))
print("Mang 2 co it nhat hai hang giong nhau khong:", TrungHang(mang2))
