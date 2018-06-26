#數字
5.6
#字串
"測試中文"
"hello world"
#布林值
True
False
#有順序. 可動的列表 list
[3,4,5]
["hello","world"]

#有順序. 不可動的列表  tuple
(3,4,5)
("hello","world")

#集合 Set
{3,4,5}
{"hello","world"}

#字典 Dictionary
{"apple":"蘋果","Banana":"香蕉"}

#變數名稱=資料
x=3
#print(資料)
print(x)

#數字運算
#小數點除法
x=3/6
print(x)
#整數除法
y=3//6
print (y)

#次方的運算
z=2**3
print(z)

#開根號
h=2**0.5
print(h)

#取餘數
r=7%3
print(r)

#變數運算
x=2+3
print(x)
x+=1 #相等於x=x+1
print(x)

#字串運算
s="hello" #雙"" 單''都可以
print(s)

#\跳脫
t="hell\"o" 
print(t)

s="Hello"+"John"
print(s)

s="Hello" "John"
print(s)

#command+/
#將所有code轉成筆記

#字串串接 \n 表達多行文字
s="hello\nworld"
print(s)

#字串串接 """ """ 表達多行文字
s="""hello
world"""
print(s)

#字串加乘
s="hello "*3+"world"
print(s)

#字串內的字都有編號從0開始 用[]去選取字
s="hello "
print(s[2])

#字串內的字都有編號從0開始 用[]去選取字，可以設定開始和結尾
s="hello "
print(s[1:4])

#字串內的字都有編號從0開始 用[]去選取字，給開頭沒有給結尾
s="hello "
print(s[1:])

#字串內的字都有編號從0開始 用[]去選取字，給結尾沒有給開頭
s="hello "
print(s[:3])
