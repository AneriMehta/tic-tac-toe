import random
import turtle
a = ['orange', 'red', 'purple', 'blue', 'white', 'brown', 'green', 'black']
s = random.choice(a)
flag=0
l = len(s)
print(l)
l1 = []
for j in range(len(s)):
    l1.append('_ ')
print(l1)
print("Guess the word..")
hm = True
'''for k in range(len(s)):
    print(s[k])'''
while hm:
    w = input("Enter a letter: ")
    c=0
    for i in range(len(s)):
        if w == s[i]:
            l1[i] = w
            c = 1
    if c == 1:
        print(l1)

    else:
        flag+=1
        l=l-1
        print(l)
        if l>0:
            print("You have {} chances left..".format(l))

    print(s)
    print(l1)

    if flag==len(s):
        print("Sorry u could not guess")
        print("The word was {}".format(s))
        hm = False
    elif l1 == s:
        print("Congratulations You guessed the correct word")
        hm = False
