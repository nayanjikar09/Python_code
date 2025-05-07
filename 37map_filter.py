# 1 map fun

def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,3,4,6,3]
# newl=[]
# for item in l:
#     newl. append(cube(item))

newl=list(map(cube, l))
print(newl)

#filter
def filter_function(a):
    return a>4
newl =filter(filter(filter_function, l))
print(newl)
