try:
    def age():
        age = int(input("Enter Your Age"))
        mon_1 = age
        mon_2 = int(12)
        result = int(mon_1 * mon_2)

        print(f"Your age in months is {result}")

    age()
except:
    print("Not a Number")
