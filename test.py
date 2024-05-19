import random
d1 = {
    1: "\u2680",
    2: "\u2681",
    3: "\u2682",
    4: "\u2683",
    5: "\u2684",
    6: "\u2685"
}
home, userscore, compscore, flag = 10,0,0,0
while userscore <= 10 and compscore <= 10:
    userinp = input("Type 'y' to roll the dice or 'n' to quite the game: ")
    if(userinp == 'y'):
        userdice = random.randint(1, 6)
        print("your dice:", d1[userdice])
        userscore += userdice
        compdice = random.randint(1, 6)
        print("your dice:", d1[compdice])
        compscore += compdice
        print("your score:", compscore)
    elif(userinp == "n"):
        flag = 1
        break
if(userscore > compscore and flag == 0):
    print("User won the match!")
elif(userscore < compscore and flag == 0):
    print("Computer won the match!")
else:
    print("You quit the game!")