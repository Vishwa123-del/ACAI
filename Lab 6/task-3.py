age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
        print("Child")
elif age < 19 and age >= 13:
        print("Teenager")
elif age < 59 and age >= 19:
        print("Adult")
else:
        print("Senior")
