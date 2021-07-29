# Given two points represented as x1,y1,x2,y2. Return the (float) distance between them considering the following distance equation.(((x2-x1)**2)+((y2-y1)**2))**0.5

flag = 0

while flag < 1 :
    x1 = input("enter x1 =")
    y1 = input("enter y1 =")
    x2 = input("enter x2 =")
    y2 = input("enter y2 =")
    if x1.isdigit() & x2.isdigit() & y1.isdigit() & y2.isdigit() :
        flag = 1
    else :
        print("Invalid data type, please try again")


leftsqur = (int(x2) - int(x1))**2
rightsqur = (int(y2) - int(y1))**2
total= (leftsqur + rightsqur)**0.5
print ("Distance Between Them is = ",round(total,3))
