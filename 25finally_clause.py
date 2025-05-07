def func1():
    try :
        l=[1,2,3,4]
        l=int(int(input("enter the index :")))
        print(l[i])
        return 1
    except:
        print("Some error occurred") 
        return 0  
    finally:
        print(" I am Always executed")
    
x=func1()
print(x)