#homework2
#四則運算 開根號 9X9列表

#四則運算
# n1=int(input("enter a Number"))
# d1=input("填入運算： ＋, -, *, / ")
# n2=int(input("enter a Number"))

# if d1=="+":
#     result=n1+n2
# elif d1=="-":
#     result=n1-n2
# elif d1=="*":
#     result=n1*n2
# elif d1=="/":
#     result=n1/n2

# print(int(result))





# #開根號
# n=int(input("Enter a Positive Integer: "))
# ans=1
# while ans<n:
#     if ans*ans==n:
#         print("Answer", ans)
#         break
#     ans+=1
# if ans==n: # 迴圈測試到最後都沒有找到答案
#     print("No Answer")



#開平方號
n=int(input("Enter a Positive Integer: "))
ans=1
while ans<n:
    if ans*ans*ans==n:
        print("Answer", ans)
        break
    ans+=1
if ans==n: # 迴圈測試到最後都沒有找到答案
    print("No Answer")








# #9X9列表

# for x in range(1, 10):
#     for y in range(1, 10):
#         print(x, y, x*y)