a=int(input("Giá niêm yết: "))
b=int( input('Chiết khấu: '))
VAT=float((a-b)/100)
print("Giá bán: ",a-b+VAT)