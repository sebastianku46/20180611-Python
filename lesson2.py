#流程控制Flow

# if 判斷式
# If 布林值：
# #    如果布林值是True執行這個程式區塊
# money=int(input("多少錢："))
# if money<0:
#     print("請輸入大於0的數字")
# #如果要增加很多條件就加上這個
# elif money<=30000:
#     print("ok")
# else:
#     #如果布林值是False 執行這個區塊
#     print("超過30000限額")

# #Control +/ 註解所有東西

# n1=int(input("enter a Number"))
# n2=int(input("enter a Number"))
# op=input("運算： ＋, -, *, /")
# #作業請使用者輸入兩個數字，並且讓使用者自動加入他們想要輸入的功能去運算




#迴圈
#中央處理器CPU 1GHz，可以跑10億個指令/每秒
#跟if不一樣的地方是跑完一次又再跑一次，不斷跑直到false為止

#break
# n=1
# while n<=5:
#     #如果布林值是True執行這個程式碼
#     print(n)
#     n+=1
#     if n==3:
#         break #終止迴圈
# print("Final",n )

#continue
# n=1
# while n<=5:
#     #如果布林值是True執行這個程式碼
#     print(n)
#     n+=1
#     if n==3:
#         continue #持續迴圈
#     print(n)
# print("Final",n )


# n=1
# while n<=5:
#     #如果布林值是True執行這個程式碼
#     print(n)
#     n+=1
#     if n%2==0: #如果 n是偶數
#         continue #持續迴圈
#     print(n)
# print("Final",n )


# #1+2+3+4+.....+50
# result=(1+50)*50/2
# print(result)

# sum=0 # 紀錄最後加總的結果
# n=1 #在迴圈中追蹤1,2,3....50
# while n<=50:
#     print(n, sum)
#     sum=sum+n #將n 的數字累加盡sum
#     n+=1
# print(sum)

# #########作業：
# n=int(input("輸入一個正整數"))
# # 1.算整數平方根 9=>3, 25>=5, 8=>沒有
# # 2.算出99乘法表


#For迴圈
# for 變數名稱 in 列表：
#     迴圈區塊 break & continue 都可以用

for n in [2,5,8,9]:#僅印出列表中數字
    print(n)

print("+++++++++++++")

for x in range(1,10):#range是從1-6所有數字的列表
    print(x)