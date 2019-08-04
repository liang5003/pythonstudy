import random
print("Let's see who's the poop king,shall we?")
print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
play = input("How many players?Please enter a number:")
try:
    play = int(play)
except ValueError:
    print("You can't enter letters!")
    play = 0
while play != 2 and play != 3 and play != 4 and play != 5:
    play = input("Only support two to five players.Please enter a number again:")
    try:
        play = int(play)
    except ValueError:
        print("You can't enter letters!")
        play = 0
print("\nOK,let's get started!")
player = list(range(1, play+1))
state = {}
a = 1
while a <= play:
    state[a] = 2
    a = a+1
current = 0
currentp = player[current]
stated = {1: "the poop pool.roll 1,2 to enter the meal box;roll 3,4,5 to stay still;roll 6 to fail.",
          2: "the toilet.roll 1,3,5 to enter the meal box;roll 2,4,6 to enter the poop pool.",
          3: "the meal box.roll 1,2,3 to stay still;roll 4,5,6 to enter the toilet."}
stated0 = {1: "the poop pool.", 2: "the toilet.", 3: "the meal box.", 4: "the poop heaven."}
while len(player) > 1:
    print("\nPlayer"+str(currentp)+",you are now in "+stated[state[currentp]])
    input("Press 'enter' to roll the dice.")
    dice = random.randint(1, 6)
    print(dice)
    if state[currentp] == 1:
        if dice < 3:
            state[currentp] = 3
        elif dice > 5:
            print("Oh no,Player"+str(currentp)+"!You have just been abandoned in the poop pool!")
            state[currentp] = 4
            del player[current]
            if current == len(player)-1:
                current = -1
            else:
                current = current-1
        else:
            state[currentp] = 1
    elif state[currentp] == 2:
        if dice == 1 or dice == 3 or dice == 5:
            state[currentp] = 3
        else: 
            state[currentp] = 1
    else:
        if dice < 4:
            state[currentp] = 3
        else:
            state[currentp] = 2
    print("You are now in " + stated0[state[currentp]])
    if current >= len(player)-1:
        current = 0
    else:
        current = current + 1
    currentp = player[current]
print("\nplayer"+str(player[0])+",you win!You must be very lucky today!")
