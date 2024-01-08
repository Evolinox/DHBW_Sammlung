amount = input("Hoehe eingeben: ")

for x in range (1, int(amount)+1):
    for i in range (0, x):
        print(x, end="")
    print("")