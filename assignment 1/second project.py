print("Hey we are going to tell you that you can draw a triangle or not")
side1=input("Please enter the first side of your triangle")
side2=input("now enter the second side of your triangle")
side3=input("at last enter the third side of your triangle")

if side1<side2+side3 or side2<side1+side3 or side3<side1+side2:
    print("congrats you can draw your triangle")
else:
    print("sorry you can't draw it")