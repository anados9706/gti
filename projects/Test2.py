
answer = input("Would you like to play? (yes/no) ")

if answer.lower().srtip() == "yes":
    print("You are the last hero, and need to defeat the 7 most dangerous villains of the Galaxy!")

    answer = input("Oh no! Here they come! How are you going to atack? (Fury Whip/Double swing/Power Strike)").lower().srtip()

    if answer == "Fury Whip":
        print("Good shot!")

    elif answer == "Double Swing":
        print("Sweet!")

    elif answer == "Power Strike":
        print("Nice Job!")
else:
   print("Oh snap!! That's to bad!")
