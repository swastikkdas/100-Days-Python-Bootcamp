print("Welcome To the RollerCoaster!")
height = int(input("What is your Height? "))
bill = 0

if height >= 120:
    print("You can ride the RollerCoaster")
    age = int(input("Enter Your Age: "))
    if age < 12:
        bill = 5
        print("Please Pay $5.")
    elif age <= 18:
        bill = 7
        print("Please Pay $7.")
    elif age >=45 and age < 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please Pay $12.")

    wants_photo = input("If you want a Photo (Y or N): ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your Final Bill is ${bill}")

else:
    print("Sorry, You have to grow taller before you can ride.")
