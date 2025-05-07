ep1={122:54, 123:57, 124:56, 125:87}
ep2={222: 67, 544:69}
print(ep1)
ep1.update(ep2)
ep1.clear
print(ep1)

ep1.popitem()
print(ep1)

#del ep1["122"]  # use for delete the dictionary 