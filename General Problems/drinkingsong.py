X = int(input())
drink = input()

while X > 0:
    result = str(X) + " bottle"
    take = "it"
    if X != 1:
        take = "one"
        result += "s"
    result += " of " + drink
    print(result, "on the wall,", result + ".")

    X -= 1

    if X == 0:
        result = "no more bottles of " + drink + "."
    else:
        result = str(X) + " bottle"
        if X != 1:
            result += "s"
        result += " of " + drink
        result += " on the wall."
    
    print("Take", take, "down, pass it around,", result)
    if X != 0:
        print("\n")
    