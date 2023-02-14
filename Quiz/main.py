Num1 =int(input("Enter First Number"))
Num2 =int(input("Enter Second Number"))

for i in range(Num1, Num2):

    if ((i%3==0) and (i%5==0)):
        print(i,"FizzBuzz")
else:
    if(i%5==0):
        print(i, "Buzz")
    else:
        if(i%3==0):
            print(i, "Fizz")
        else:
            print(i)




