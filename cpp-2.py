# mylist=["prashant","sachin","rohit","virat","dhoni",77,88,99,100,"sandeep",60.52]
# print(mylist)
# print(type(mylist)) 
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])
# print(mylist[5])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[5:])
# print(mylist[::2])
# print(mylist[::-1])
# print(mylist[1:8:2])
# print(mylist[1:8:3])


mylist = ["prashant", "sachin", "rohit", "virat", "dhoni", 77, 88, 99, 100, "sandeep", 60.52]

mylist.append('kshitij')
mylist.append("kshitij_panday")
print(mylist)
mylist.insert(2, "panday")
print(mylist)
mylist.remove("panday")
print(mylist)
newList = mylist.copy()
print(newList)    


crazylist =[['prashant', 'sachin', 'rohit'], [77, 88, 99], [100, 'sandeep', 60.52]]
print(crazylist)
print(crazylist[0][0])
print(crazylist[0][1])
print(crazylist[0][2])
print(crazylist[1][0])
print(crazylist[1][1])
print(crazylist[1][2])
print(crazylist[2][0])
print(crazylist[2][1])
print(crazylist[2][2])



list1=["Kshitij","Panday"]
print(list1*2)

list2=[50,25.50]
print(list1+list2)