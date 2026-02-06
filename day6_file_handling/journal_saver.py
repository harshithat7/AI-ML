name = input("Enter your name: ")
goal = input("Daily goal: ")
with open("journal.txt", "a") as file:
    file.write(f"{name}: {goal}\n")