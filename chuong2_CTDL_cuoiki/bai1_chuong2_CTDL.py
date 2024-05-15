def doi_xung(mang):#tạo hàm kiểm tra xem một mảng có đối xứng hay khôg
    if(len(mang) != len(mang[0])):
#nếu chiều dài của mảng không bằng độ dài của hàng đầu tiên
#trả về False
        return False
#vòng lặp trong ma trận từ [0][0] đến [m-1][n-1]  
    for i in range(len(mang)):##duyệt biến i cho đến vị trí hàng-1 của ma trận
        for j in range(len(mang)):#duyệt biến i cho đến vị trí cột-1 của ma trận
            if mang[i][j] != mang [j][i]:#so sánh các ptu tại vị trí(i,j) và (j,i)
                return False#nếu ko bằng nhau thì trả về False
    return True   #ngc lại trả về true    
mang = [[1, 2, 3],
         [2, 4, 5],
         [3, 5, 6]]
print("Mang tren la mot mang doi xung !? >>", doi_xung(mang))