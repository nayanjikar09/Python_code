a=input("enter the number=  ")
print(f"multi table of {a}")
try:
 for i in range(1,11):
    print(f"{int(a)} X {i}={int(a)*i}")
except Exception as e:            
    print("some error occured")
print("end of program")