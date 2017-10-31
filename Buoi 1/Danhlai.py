a= int(intput("a= ?"))
b = int(input("b= ?"))
c= int(inpnut("c= ?"))
delta = b * b - 4 * a * c
if delta < 0 :
    print("Phuong trinh vo nghiem")
elif delta = 0:
    print("Phuong trinh co nghiem kep: ",-b / (2 * c))
else:
    print("Phuong trinh co 2 nghiem phan biet")
    print("x1= ", (-b + delta**0.5)/(2 * a))
    print("x2= ", (-b - delta**0.5)/(2 * a))
