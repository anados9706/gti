from math import floor

cost = 0
low = 0
high = 100
playing = True

while playing:
    print("Cost: $" + str(cost))
    guess = floor((low + high)/2)
    print("Our guess is " + str(guess) + ":")
    action = input()
    if action == "l":
        high = guess - 1
    elif action == "h":
        low = guess + 1
    elif action == "c":
        print("We found the cat!!")
        playing = False
    elif action == "exit":
        print("Bye")
        playing = False
    else:
        print("Sorry what was that?")  

    cost = cost + 1  