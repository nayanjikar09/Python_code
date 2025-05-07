# lists are mutable 
marks=[3,4,5,"nayan", True]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-5])

if "nayan" in marks:
    print("yes")
else:
    print("no")
    
print(marks[1:3:2])