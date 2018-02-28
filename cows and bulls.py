import random
print("Welcome to cows and bulls game")
print("How to play:\nYou have to enter a random 4 digit number.\nYou will get a cow for correct no. at correct place and a bull for a correct no. at wrong place.")
print("You have to guess the correct no. by the no. of cows and bulls at the end of every input")
print("The game ends and u win if you get four cows and lose if u get 4 bulls")
print("Let's start....")

no = str(random.randint(0,9999))

cows = 0
bulls = 0
flag=0

while cows != 4:
    l2 = [" ", " ", " ", " "]
    cows = 0
    bulls = 0
    l1=[]
    l3=[]
    r = input("Enter a no.")
    flag+=1
    for i in range(len(no)):
        if no[i] == r[i]:
            cows+=1
            l1.append(i)
    print(l1)

    for i in range(len(l2)):
        for j in range(len(l1)):
            if i == l1[j]:
                l2[i]="c "

    for i in range(len(no)):
            for j in range(len(r)):
                if i in l1:
                    continue
                elif no[i] == r[j]:
                    bulls+=1
                    l3.append(j)
    print(l3)

    for i in range(len(l2)):
        for j in range(len(l3)):
            if i == l3[j]:
                if l2[i]==" ":
                    l2[i]="b "

    print(l2)

    print("Cows = {}, bulls = {}".format(cows,bulls))
if cows == 4:
    print("Congratulations you won after {} guesses".format(flag))
    print("The no. was {}".format(no))
else:
    print("Oops!! You lose.....")
    print("The no. was {}".format(no))
