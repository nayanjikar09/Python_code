question=["Which language was use to create fb",
          "python","French","Javascript","PHP","none",4]

question=["Which language was use to create fb",
          "python","French","Javascript","PHP","none",4]

question=["Which language was use to create fb",
          "python","French","Javascript","PHP","none",4]

question=["Which language was use to create fb",
          "python","French","Javascript","PHP","none",4]

question=["Which language was use to create fb",
          "python","French","Javascript","PHP","none",4]
levels=[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000]

for i in range(0, len(question)):
    question=question[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a.{question[1]}  b.{question[2]} ")    
    print(f"c.{question[3]}  d.{question[4]} ")
    reply = int(input("Enter  "))
    if (reply==question[-1]):
     print(f"Correct answer, you have won Rs.{levels[i]}")
     if(i==4):
         money=1000
    else:
        print("wrong ans!!!")
        break