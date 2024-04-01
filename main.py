import tkinter as tk
import trainer
import random

checkAnswer = ""
play_token = "none"
play_random = True

def playRandom():
    global play_random
    play_random = True
    trainer.resetMode()
    randBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    inOrderBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    if play_token == "splits":
        nextSplit()
    elif play_token == "softs":
        nextSoft()
    elif play_token == "hards":
        nextHard()
    elif play_token == "all":
        nextAll()

def playInOrder():
    global play_random
    play_random = False
    trainer.resetMode()
    randBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    inOrderBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    if play_token == "splits":
        nextSplit()
    elif play_token == "softs":
        nextSoft()
    elif play_token == "hards":
        nextHard()
    elif play_token == "all":
        nextAll()

def randomSuit():
    random_dealer_suit = random.randint(1, 4)
    match(random_dealer_suit):
        case 1:
            print("Dealer suit is Hearts")
            dealerSuitValue.config(text="♥", fg="red")
            dealerCardValue.config(fg="red")
        case 2:
            print("Dealer suit is Spades")
            dealerSuitValue.config(text="♠", fg="black")
            dealerCardValue.config(fg="black")
        case 3:
            print("Dealer suit is Clubs")
            dealerSuitValue.config(text="♣", fg="green")
            dealerCardValue.config(fg="green")
        case 4:
            print("Dealer suit is Diamonds")
            dealerSuitValue.config(text="♦", fg="blue")
            dealerCardValue.config(fg="blue")
        case _:
            print("ERROR choosing dealer suit")

    random_p1_suit = random.randint(1, 4)
    random_p2_suit = random.randint(1, 4)
    match(random_p1_suit):
        case 1:
            print("Player Card 1 suit is Hearts")
            playerCard1SuitValue.config(text="♥", fg="red")
            playerCard1Value.config(fg="red")
        case 2:
            print("Player Card 1 suit is Spades")
            playerCard1SuitValue.config(text="♠", fg="black")
            playerCard1Value.config(fg="black")
        case 3:
            print("Player Card 1 suit is Clubs")
            playerCard1SuitValue.config(text="♣", fg="green")
            playerCard1Value.config(fg="green")
        case 4:
            print("Player Card 1 suit is Diamonds")
            playerCard1SuitValue.config(text="♦", fg="blue")
            playerCard1Value.config(fg="blue")
        case _:
            print("ERROR choosing p1 suit")

    match(random_p2_suit):
        case 1:
            print("Player Card 2 suit is Hearts")
            playerCard2SuitValue.config(text="♥", fg="red")
            playerCard2Value.config(fg="red")
        case 2:
            print("Player Card 2 suit is Spades")
            playerCard2SuitValue.config(text="♠", fg="black")
            playerCard2Value.config(fg="black")
        case 3:
            print("Player Card 2 suit is Clubs")
            playerCard2SuitValue.config(text="♣", fg="green")
            playerCard2Value.config(fg="green")
        case 4:
            print("Player Card 2 suit is Diamonds")
            playerCard2SuitValue.config(text="♦", fg="blue")
            playerCard2Value.config(fg="blue")
        case _:
            print("ERROR choosing p2 suit")

def hardTotalToCards(input):
    match(int(input)):
        case 17:
            rand_value = random.randint(0, 1)
            match(rand_value):
                case 0:
                    print("GOT 10,7")
                    return 10,7
                case 1:
                    return 9,8
                    print("GOT 9,8")
                case _:
                    print("ERROR on Hard 17")
        case 16:
            rand_value = random.randint(0, 1)
            match(rand_value):
                case 0:
                    return 10,6
                case 1:
                    return 9,7
                case _:
                    print("ERROR on Hard 16")
        case 15:
            rand_value = random.randint(0, 2)
            match(rand_value):
                case 0:
                    return 10,5
                case 1:
                    return 9,6
                case 2:
                    return 8,7
                case _:
                    print("ERROR on Hard 15")
        case 14:
            rand_value = random.randint(0, 2)
            match(rand_value):
                case 0:
                    return 10,4
                case 1:
                    return 9,5
                case 2:
                    return 8,6
                case _:
                    print("ERROR on Hard 14")
        case 13:
            rand_value = random.randint(0, 3)
            match(rand_value):
                case 0:
                    return 10,3
                case 1:
                    return 9,4
                case 2:
                    return 8,5
                case 3:
                    return 7,6
                case _:
                    print("ERROR on Hard 13")
        case 12:
            rand_value = random.randint(0, 3)
            match(rand_value):
                case 0:
                    return 10,2
                case 1:
                    return 9,3
                case 2:
                    return 8,4
                case 3:
                    return 7,5
                case _:
                    print("ERROR on Hard 12")
        case 11:
            rand_value = random.randint(0, 3)
            match(rand_value):
                case 0:
                    return 9,2
                case 1:
                    return 8,3
                case 2:
                    return 7,4
                case 3:
                    return 6,5
                case _:
                    print("ERROR on Hard 11")
        case 10:
            rand_value = random.randint(0, 2)
            match(rand_value):
                case 0:
                    return 8,2
                case 1:
                    return 7,3
                case 2:
                    return 6,4
                case _:
                    print("ERROR on Hard 10")
        case 9:
            rand_value = random.randint(0, 2)
            match(rand_value):
                case 0:
                    return 7,2
                case 1:
                    return 6,3
                case 2:
                    return 5,4
                case _:
                    print("ERROR on Hard 9")
        case 8:
            rand_value = random.randint(0, 1)
            match(rand_value):
                case 0:
                    return 6,2
                case 1:
                    return 5,3
                case _:
                    print("ERROR on Hard 8")
        case _:
            print("ERROR: Hard Total not in list")
def nextSplit():
    global checkAnswer, play_random
    dealer_card, player_card, answer = trainer.playSplits(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    #correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = player_card.split(",")
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()

def nextSoft():
    global checkAnswer, play_random
    dealer_card, player_card, answer = trainer.playSofts(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    #correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = player_card.split(",")
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()

def nextHard():
    global checkAnswer, play_random
    dealer_card, player_card, answer = trainer.playHards(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    #correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = hardTotalToCards(player_card)
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()

def nextAll():
    global checkAnswer, play_random
    dealer_card, player_card, answer, check_mode = trainer.playAll(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    #correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer
    if(check_mode == "splits"):
        hitBtn.place_forget()
        standBtn.place_forget()
        doubleHitBtn.place_forget()
        doubleStandBtn.place_forget()
        splitYesBtn.place(x=875, y=800)
        splitNoBtn.place(x=975, y=800)
    else:
        splitYesBtn.place_forget()
        splitNoBtn.place_forget()
        hitBtn.place(x=770, y=800)
        standBtn.place(x=825, y=800)
        doubleHitBtn.place(x=900, y=800)
        doubleStandBtn.place(x=1025, y=800)
    if(check_mode == "splits"):
        dealerCardValue.config(text=dealer_card)
        p1, p2 = player_card.split(",")
        playerCard1Value.config(text=p1)
        playerCard2Value.config(text=p2)
    elif(check_mode == "softs"):
        dealerCardValue.config(text=dealer_card)
        p1, p2 = player_card.split(",")
        playerCard1Value.config(text=p1)
        playerCard2Value.config(text=p2)
    elif(check_mode == "hards"):
        dealerCardValue.config(text=dealer_card)
        p1, p2 = hardTotalToCards(player_card)
        playerCard1Value.config(text=p1)
        playerCard2Value.config(text=p2)
    else:
        print("ERROR in All Mode: Mode Not Found")
    randomSuit()

def changeToSplits():
    global play_token
    play_token = "splits"
    splitsBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hitBtn.place_forget()
    standBtn.place_forget()
    doubleHitBtn.place_forget()
    doubleStandBtn.place_forget()
    splitYesBtn.place(x=875, y=800)
    splitNoBtn.place(x=975, y=800)
    nextSplit()
def changeToSofts():
    global play_token
    play_token = "softs"
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    splitYesBtn.place_forget()
    splitNoBtn.place_forget()
    hitBtn.place(x=770, y=800)
    standBtn.place(x=825, y=800)
    doubleHitBtn.place(x=900, y=800)
    doubleStandBtn.place(x=1025, y=800)
    nextSoft()

def changeToHards():
    global play_token
    play_token = "hards"
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    allBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    splitYesBtn.place_forget()
    splitNoBtn.place_forget()
    hitBtn.place(x=770, y=800)
    standBtn.place(x=825, y=800)
    doubleHitBtn.place(x=900, y=800)
    doubleStandBtn.place(x=1025, y=800)
    nextHard()
def changeToAll():
    global play_token
    play_token = "all"
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    nextAll()
def checkSplitYes():
    global play_token
    print("Split Yes")
    if(checkAnswer == "Y"):
        print("Correct")
        correctCheck.config(text="CORRECT!", fg="green")
    else:
        print("Incorrect. Correct answer is Do Not Split")
        correctCheck.config(text="Incorrect", fg="red")

    if(play_token == "splits"):
        nextSplit()
    else:
        nextAll()

def checkSplitNo():
    global play_token
    print("Split No")
    if(checkAnswer == "N"):
        print("Correct")
        correctCheck.config(text="CORRECT!", fg="green")
    else:
        print("Incorrect. Correct answer is Split")
        correctCheck.config(text="Incorrect", fg="red")

    if(play_token == "splits"):
        nextSplit()
    else:
        nextAll()

def checkHit():
    global play_token
    print("Hit")
    if(checkAnswer == "H"):
        print("Correct")
        correctCheck.config(text="CORRECT!", fg="green")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        correctCheck.config(text="Incorrect", fg="red")

    if(play_token == "softs"):
        nextSoft()
    elif(play_token == "hards"):
        nextHard()
    else:
        nextAll()

def checkStand():
    print("Stand")
    if(checkAnswer == "S"):
        print("Correct")
        correctCheck.config(text="CORRECT!", fg="green")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        correctCheck.config(text="Incorrect", fg="red")

    if(play_token == "softs"):
        nextSoft()
    elif(play_token == "hards"):
        nextHard()
    else:
        nextAll()

def checkDh():
    print("Double or Hit")
    if(checkAnswer == "Dh"):
        print("Correct")
        correctCheck.config(text="CORRECT!", fg="green")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        correctCheck.config(text="Incorrect", fg="red")

    if(play_token == "softs"):
        nextSoft()
    elif(play_token == "hards"):
        nextHard()
    else:
        nextAll()
def checkDs():
    print("Double or Stand")
    if(checkAnswer == "Ds"):
        print("Correct")
        correctCheck.config(text="CORRECT!", fg="green")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        correctCheck.config(text="Incorrect", fg="red")

    if(play_token == "softs"):
        nextSoft()
    elif(play_token == "hards"):
        nextHard()
    else:
        nextAll()

window = tk.Tk()
window.title("Joshy's BlackJack Basic Strategy Trainer")
window.geometry("1920x1080")
window.geometry("+0+0")
icon = tk.PhotoImage(file="bitcoin.png")
window.iconphoto(True, icon)
window.configure(background="#3aa31a")

splitsBtn = tk.Button(window, text="Play Splits", command=changeToSplits)
splitsBtn.place(x=700, y=25)

softsBtn = tk.Button(window, text="Play Soft Totals", command=changeToSofts)
softsBtn.place(x=815, y=25)

hardsBtn = tk.Button(window, text="Play Hard Totals", command=changeToHards)
hardsBtn.place(x=975, y=25)

allBtn = tk.Button(window, text="Play All", command=changeToAll)
allBtn.place(x=1125, y=25)

dealerCard = tk.Label(window, text="Dealer Card: ", font=("Arial", 20))
dealerCard.place(x=100, y=300)

playerCard = tk.Label(window, text="Player Card: ", font=("Arial", 20))
playerCard.place(x=100, y=350)

# correctAnswer = tk.Label(window, text="Correct Answer: ", font=("Arial", 20))
# correctAnswer.place(x=100, y=400)

correctCheck = tk.Label(window, text="", font=("Arial", 20))
correctCheck.place(x=1300, y=400)

randBtn = tk.Button(window, text="Play Random Hands", command=playRandom)
inOrderBtn = tk.Button(window, text="Play Hands In Order", command=playInOrder)
randBtn.place(x=1700, y=25)
inOrderBtn.place(x=1700, y=60)
randBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)

# nextBtn = tk.Button(window, text="Next Card", command=nextSplit)
# nextBtn.place(x=800, y=300)

splitYesBtn = tk.Button(window, text="Split", command=checkSplitYes)
splitNoBtn = tk.Button(window, text="Do Not Split", command=checkSplitNo)

hitBtn = tk.Button(window, text="Hit", command=checkHit)
standBtn = tk.Button(window, text="Stand", command=checkStand)
doubleHitBtn = tk.Button(window, text="Double or Hit", command=checkDh)
doubleStandBtn = tk.Button(window, text="Double or Stand", command=checkDs)

#dealerCardCanvas = tk.Canvas(window, width=250, height=350, bg="white")
dealerCardCanvas = tk.Canvas(window, width=200, height=300, bg="white")
dealerCardCanvas.place(x=850, y=75)

playerCard1Canvas = tk.Canvas(window, width=200, height=300, bg="white")
playerCard1Canvas.place(x=735, y=450)
playerCard2Canvas = tk.Canvas(window, width=200, height=300, bg="white")
playerCard2Canvas.place(x=985, y=450)

dealerCardValue = tk.Label(text="X", font=("Arial", 75, "bold"), bg="white")
dealerSuitValue = tk.Label(text="O", font=("Arial", 75, "bold"), bg="white")
dealerCardValue.place(x=875, y=100)
dealerSuitValue.place(x=950, y=240)
playerCard1Value = tk.Label(text="X", font=("Arial", 75, "bold"), bg="white")
playerCard2Value = tk.Label(text="X", font=("Arial", 75, "bold"), bg="white")
playerCard1SuitValue = tk.Label(text="O", font=("Arial", 75, "bold"), bg="white")
playerCard2SuitValue = tk.Label(text="O", font=("Arial", 75, "bold"), bg="white")
playerCard1Value.place(x=760, y=475)
playerCard2Value.place(x=1010, y=475)
# x + 75, y + 140
playerCard1SuitValue.place(x=835, y=615)
playerCard2SuitValue.place(x=1085, y=615)

window.mainloop()