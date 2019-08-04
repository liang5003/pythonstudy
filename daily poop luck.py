import random
print("Dear werepoop,you have been made in the factory.")
a = input("Enter 'bbb' to learn about the rule.Enter any other things to skip.")
a = str(a)
if a == "bbb":
    print("\nYou will go from grade one to grade nine.Your initial IQ is 100."
          "\nIn each grade You will roll a dice to decide whether your IQ will rise or fall."
          "\n1,2 makes you smarter;3,4 does nothing;5,6 makes you more and more stupid."
          "\nBe careful not to make your IQ too high or too low,or you'll in great trouble."
          "\nAt the end of grade nine,your dice along with your IQ will decide where you will be then."
          "\nThis game can be used to try your daily luck,which is also called'daily poop luck'.")
print("\nOK!Let's get started.")
iq = 100
grade = 1
alive = 1
while grade <= 8 and alive == 1:
    print("\nYou are now in grade "+str(grade)+".Your IQ is "+str(iq)+".")
    if 80 <= iq <= 120:
        state = 1
    elif iq == 70:
        state = 2
    elif iq == 130 and grade != 5:
        state = 3
    else:
        state = 4
    if state == 2:
          print("You are too stupid!If your IQ continues falling,the aunts will throw you back in the poop oven.")
    elif state == 3:
          print("You are too smart!If your IQ continues growing,the aunts will force you yo build factories.")
    elif state == 4:
          print("If you roll 1,2 this round,you have a chance to get to the Chemistaro Middle School!")
    nothing = input("Press 'enter' to roll the dice!")
    dice = random.randint(1,6)
    print(dice)
    if dice < 3:
        if state != 3 and state != 4:
            iq = iq+10
        elif state == 3:
            alive = 0
            print("Oh no!You are too smart!The aunts have forced you design factory equipment for them!")
        else:
            alive = 5
            print("Oh my goodness!You are accepted by the Chemistaro Middle School!What a genius!")
    elif dice > 4:
        if state != 2:
            iq = iq-10
        else:
            alive = 0
            print("Oh no!You are too stupid!The aunts have thrown you back into the poop oven!")
    grade = grade+1
if alive == 1:
    print("You are now in grade 9.Your IQ is "+str(iq)+".")
    if iq > 115:
        print("Roll 1,2,3 to enter Hatchegg High School;Roll 4,5,6 to enter Pigeon High school.")
        nothing = input("Press 'enter' to roll the dice!")
        dice = random.randint(1, 6)
        print(dice)
        if dice > 3:
            alive = 3
        else:
            alive = 4
    elif iq < 85:
        print("Roll 1,2,3 to enter Pigeon High school;Roll 4,5,6 to enter Savenergy Factory.")
        nothing = input("Press 'enter' to roll the dice!")
        dice = random.randint(1, 6)
        print(dice)
        if dice > 3:
            alive = 2
        else:
            alive = 3
    else:
        print("Roll 1 to enter Hatchegg High School;Roll 2,3,4,5 to enter Pigeon High School;Roll 6 to enter "
              "Savenergy Factory.")
        nothing = input("Press 'enter' to roll the dice!")
        dice = random.randint(1, 6)
        print(dice)
        if dice < 2:
            alive = 4
        elif dice > 5:
            alive = 2
        else:
            alive = 3
if alive == 0:
    print("\nBad luck!You should behave carefully today!")
elif alive == 2:
    print("\nWorst luck!You must behave EXTREMELY carefully today!")
elif alive == 3:
    print("\nNormal ending!You will have another simple day like before!")
elif alive == 4:
    print("\nGood luck!Maybe something good will happen unexpectedly today!")
else:
    print("\nBest luck!You can do whatever you like today!")