# def double(x):
#     return x*2

def appl(fx, value):
    return fx(value)

double =lambda x: x*2
cube = lambda x:x*x*x
avg = lambda x,y: (x+y)/2
print(double(5))
print(cube(6))
print(avg(6,9))

print(appl(lambda x: x* x* x, 2))