pr=int(input("enter your percentage--"))
if pr<=25:
    print("the grade is d--")
elif pr>=25 and pr<=45:
    print(" the grade is c--")
elif pr>=45 and pr<=50:
    print("the grade is b")
elif pr>=50 and pr<=60:
    print("the grade is b+")
elif pr>=60 and pr<=80:
    print("the grade is a--")
elif pr>80:
    print("the grade is a++--")
else:
    print("you are failed")

