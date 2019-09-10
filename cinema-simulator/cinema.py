films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

while True:
    choice = input("What film would you like to watch?\n").strip().title()

    if choice in films:
        age = int(input("How old are you?\n").strip())
        if age >= films[choice][0]:

            if films[choice][1] > 0:
                print("Enjoy your film.")
                films[choice][1] -= 1
            else:
                print("Sorry but we're sold out.")
        else:
            print("You're not old enough.")
    else:
        print("We don't have that film.")
    print("=" * 50)
