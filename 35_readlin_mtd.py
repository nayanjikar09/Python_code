f=open('text.py','r')
while True:
    line = f.readline()
    m1 = f.splite(",")[0]
    m2 = f.splite(",")[1]
    m2 = f.splite(",")[2]
    if not line:
        break
    print(line)