import datetime
def getdate():
    return datetime.datetime.now()
def dieth():
    harry = int(input("1 For Add a Diet.\n2 For See The Diets.\nHere: "))
    if harry == 1:
        ad = str(input("Enter What You Want To Add"))
        with open("harrydiet.txt","a") as h:
            h.write(str((getdate()," ",ad)))
    elif harry == 2:
        with open("harrydiet.txt","rt") as h1:
            print(h1.readlines())
    else:
        print("Index Out Of Range")
        dieth()
def exerciseh():
    harryexer = int(input("1 For Add a Exercise.\n2 For See The Exercise.\nHere: "))
    if harryexer == 1:
        adex = str(input("Enter What You Want to Add."))
        with open("harryexercise.txt",'a') as he:
            he.write(str((getdate()," ",adex)))
    elif harryexer == 2:
        with open("harryexercise.txt",'rt') as he1:
            print(he1.readlines())
    else:
        print("Index Out Of Range")
        exerciseh()

def dietr():
    harry = int(input("1 For Add a Diet.\n2 For See The Diets.\nHere: "))
    if harry == 1:
        ad = str(input("Enter What You Want To Add"))
        with open("rohandiet.txt", "a") as h:
            h.write(str((getdate(), " ", ad)))
    elif harry == 2:
        with open("rohandiet.txt", "rt") as h1:
            print(h1.readlines())
    else:
        print("Index Out Of Range")
        dieth()
def exerciser():
    harryexer = int(input("1 For Add a Exercise.\n2 For See The Exercise.\nHere: "))
    if harryexer == 1:
        adex = str(input("Enter What You Want to Add."))
        with open("rohanexercise.txt", 'a') as he:
            he.write(str((getdate(), " ", adex)))
    elif harryexer == 2:
        with open("rohanexercise.txt", 'rt') as he1:
            print(he1.readlines())
    else:
        print("Index Out Of Range")
        exerciseh()
def dietha():
    harry = int(input("1 For Add a Diet.\n2 For See The Diets.\nHere: "))
    if harry == 1:
        ad = str(input("Enter What You Want To Add"))
        with open("hammaddiet.txt", "a") as h:
            h.write(str((getdate(), " ", ad,)))
    elif harry == 2:
        with open("hammaddiet.txt", "rt") as h1:
            print(h1.readlines())
    else:
        print("Index Out Of Range")
        dieth()
def exerciseha():
    harryexer = int(input("1 For Add a Exercise.\n2 For See The Exercise.\nHere: "))
    if harryexer == 1:
        adex = str(input("Enter What You Want to Add."))
        with open("hammadexercise.txt", 'a') as he:
            he.write(getdate(), " ", adex)
    elif harryexer == 2:
        with open("hammadexercise.txt", 'rt') as he1:
            print(he1.readlines())
    else:
        print("Index Out Of Range")
        exerciseh()

if __name__ == '__main__':
    while True:
        a = int(input("Enter The Number\n1 For Harry\n2 For Rohan\n3 For Hammad\nEnter 5 for Quit\nHere: "))
        if a == 1:
            print("For Harry")
            b = int(input("Enter The Number\n1 For Diet\n2 For Exercise\nHere: "))
            if b == 1:
                dieth()
            elif b == 2:
                exerciseh()
        elif a == 2:
            print("For Rohan")
            b = int(input("Enter The Number \n1 For Diet\n2 For Exercise\nHere: "))
            if b == 1:
                dietr()
            elif b == 2:
                exerciser()
        elif a == 3:
            print("For Hammad")
            b = int(input("Enter The Number \n1 For Diet\n2 For Exercise\nHere: "))
            if b == 1:
                dietha()
            elif b == 2:
                exerciseha()
        elif a == 5:
            print("Thanks For Coming")
            exit()
        else:
            continue
