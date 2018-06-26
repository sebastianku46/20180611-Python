#有序可以變動的列表list
grade=[12,60,15,70,90]
print(grade)

#取得列表中的資料
grade=[12,60,15,70,90]
print(grade[2])

#將列表中的數字做調整
grade=[12,60,15,70,90]
grade[1]=55
print(grade[1])

#取得列表區段
grade=[12,60,15,70,90]
print(grade[1:3])

#刪除列表1-3
grade=[12,60,15,70,90]
grade[1:3]=[]
print(grade)

#加入串接
grade=[12,60,15,70,90]
grade=grade+[222,400]
print(grade)

#認識列表的長度 len
print(len(grade))

#巢狀列表
data=[[3,4,5],[6,7,8]]
print(data[0])


#取代數列
data=[[3,4,5],[6,7,8]]
data[0][0:2]=[888,888,888]
print(data[0])

data=[[3,4,5],[6,7,8]]
print(data)

#有序不可以變動的列表Tuple
data=(3,4,5)
print(data)
#不可使用 []=[] 會出現錯誤

