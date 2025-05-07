tup=(32,54,23,23,65,)
temp=list(tup)
print(type(temp))
temp.append("32")  #add item
temp.pop(3)       #remove item

temp[2]="999" #change item
tupl=tuple(temp)
print(tupl)

res=tup.count(23)
print(res)