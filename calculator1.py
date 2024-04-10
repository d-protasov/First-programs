print("Hello, this is calculator Python!!!")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
operator = int(input("What kind of operation? \n"
              "1) Addition \n"
              "2) Subtraction \n"
              "3) Division \n"
              "4) Multiplication \n"))
if operator == 1:
    r = number_1 + number_2
    o = "Addition"
    t = o
elif operator == 2:
    r = number_1 - number_2
    p = "Subtraction"
    t = p
elif operator == 3:
    if number_2 == 0:
        print("Sorry, error, because division on zero!!!")
        exit()
    r = float(number_1 / number_2)
    c = "Division"
    t = c
elif operator == 4:
    r = number_1 * number_2
    m = "Multiplication"
    t = m
else:
    print("Dont have this operator")
print("Resultat", t, "=", r)