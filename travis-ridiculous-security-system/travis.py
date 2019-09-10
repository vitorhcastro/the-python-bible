known_users = ["Alice", "Bob", "Claire", "Dan", "Emman", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?\n").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n): ").lower()
        if remove == "y":
            known_users.remove(name)
        else:
            print("No problem, I didn't want you to leave anyway.")
    else:
        print("I don't think I've met you yet {}.".format(name))
        add_me = input("Would you like to be added to the system? (y/n): ").lower()
        if add_me == "y":
            known_users.append(name)
        else:
            print("No problem, see you later!")
        
    print("="*20)
