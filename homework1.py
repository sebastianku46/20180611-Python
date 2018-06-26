#讓使用者輸入5個數字
#告訴人家哪個數字最大 1.算總和 2.哪一個數字最大
#使用列表 list 列表處理

n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n3=int(input("Enter a number:"))
n4=int(input("Enter a number:"))
n5=int(input("Enter a number:"))
List=[n1,n2,n3,n4,n5]
print(List)
List2=(n1+n2+n3+n4+n5)
print("總和:",List2)
print("最大值:", max(List))