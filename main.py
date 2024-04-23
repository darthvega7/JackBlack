import tkinter as tk
import trainer_engine as trainer
import bjbs_chart
import random

checkAnswer = ""
play_token = "none"
play_random = True

def splitsChart():
    rows = 11
    cols = 11

    splits_chart = tk.Toplevel()
    splits_chart.title("Basic Strategy Chart: Splits")
    splits_chart.geometry("1280x720")
    #splits_chart.geometry("1920x1080")
    splits_chart.geometry("+0+0")
    #splits_chart_icon = tk.PhotoImage(file="bitcoin.png")
    #splits_chart.iconphoto(True, chart_icon)
    splits_chart.configure(background="#3aa31a")

    for i in range(rows):
        for j in range(cols):
            cell_value = bjbs_chart.chart_array[i][j]
            label = tk.Label(
                splits_chart, text=cell_value, padx=10, pady=5, relief=tk.RIDGE, borderwidth=2,
                font=("Arial", 20)
            )
            label.grid(row=i, column=j, sticky="nsew")

    for i in range(rows):
        splits_chart.grid_rowconfigure(i, weight=1, minsize=40)
    for j in range(cols):
        splits_chart.grid_columnconfigure(j, weight=1, minsize=80)

    splits_chart.grid_slaves(0, 0)[0].config(text="")

    # Always Splits Aces
    for j in range(1, 11):
        label = splits_chart.grid_slaves(row=1, column=j)[0]
        label.config(bg="green")

    # Never Split 10's
    for j in range(1, 11):
        label = splits_chart.grid_slaves(row=2, column=j)[0]
        label.config(bg="white")

    # Split 9's against 2 thru 9 except for 7
    for j in range(1, 9):
        label = splits_chart.grid_slaves(row=3, column=j)[0]
        label.config(bg="green")
    for j in range(9, 11):
        label = splits_chart.grid_slaves(row=3, column=j)[0]
        label.config(bg="white")
    splits_chart.grid_slaves(3, 6)[0].config(bg="white")

    # Always Split 8's
    for j in range(1, 11):
        label = splits_chart.grid_slaves(row=4, column=j)[0]
        label.config(bg="green")

    # Split 7's against 2 thru 7
    for j in range(1, 7):
        label = splits_chart.grid_slaves(row=5, column=j)[0]
        label.config(bg="green")
    for j in range(7, 11):
        label = splits_chart.grid_slaves(row=5, column=j)[0]
        label.config(bg="white")

    # Split 6's against 2 thru 6
    for j in range(1, 6):
        label = splits_chart.grid_slaves(row=6, column=j)[0]
        label.config(bg="green")
    for j in range(6, 11):
        label = splits_chart.grid_slaves(row=6, column=j)[0]
        label.config(bg="white")

    # Never Split 5's
    for j in range(1, 11):
        label = splits_chart.grid_slaves(row=7, column=j)[0]
        label.config(bg="white")

    # Split 4's against 5 and 6
    for j in range(1, 11):
        label = splits_chart.grid_slaves(row=8, column=j)[0]
        label.config(bg="white")
    for j in range(4, 6):
        label = splits_chart.grid_slaves(row=8, column=j)[0]
        label.config(bg="green")

    # Split 3's and 2's against 2 thru 7
    for i in range(9, 11):
        for j in range(1, 7):
            label = splits_chart.grid_slaves(row=i, column=j)[0]
            label.config(bg="green")
        for j in range(7, 11):
            label = splits_chart.grid_slaves(row=i, column=j)[0]
            label.config(bg="white")

def resetCards():
    dealerCardValue.config(text="X")
    dealerSuitValue.config(text="O")
    playerCard1Value.config(text="X")
    playerCard2Value.config(text="X")
    playerCard1SuitValue.config(text="O")
    playerCard2SuitValue.config(text="O")

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
            #print("Dealer suit is Hearts")
            dealerSuitValue.config(text="♥", fg="red")
            dealerCardValue.config(fg="red")
        case 2:
            #print("Dealer suit is Spades")
            dealerSuitValue.config(text="♠", fg="black")
            dealerCardValue.config(fg="black")
        case 3:
            #print("Dealer suit is Clubs")
            dealerSuitValue.config(text="♣", fg="green")
            dealerCardValue.config(fg="green")
        case 4:
            #print("Dealer suit is Diamonds")
            dealerSuitValue.config(text="♦", fg="blue")
            dealerCardValue.config(fg="blue")
        case _:
            print("ERROR choosing dealer suit")

    random_p1_suit = random.randint(1, 4)
    random_p2_suit = random.randint(1, 4)
    match(random_p1_suit):
        case 1:
            #print("Player Card 1 suit is Hearts")
            playerCard1SuitValue.config(text="♥", fg="red")
            playerCard1Value.config(fg="red")
        case 2:
            #print("Player Card 1 suit is Spades")
            playerCard1SuitValue.config(text="♠", fg="black")
            playerCard1Value.config(fg="black")
        case 3:
            #print("Player Card 1 suit is Clubs")
            playerCard1SuitValue.config(text="♣", fg="green")
            playerCard1Value.config(fg="green")
        case 4:
            #print("Player Card 1 suit is Diamonds")
            playerCard1SuitValue.config(text="♦", fg="blue")
            playerCard1Value.config(fg="blue")
        case _:
            print("ERROR choosing p1 suit")

    match(random_p2_suit):
        case 1:
            #print("Player Card 2 suit is Hearts")
            playerCard2SuitValue.config(text="♥", fg="red")
            playerCard2Value.config(fg="red")
        case 2:
            #print("Player Card 2 suit is Spades")
            playerCard2SuitValue.config(text="♠", fg="black")
            playerCard2Value.config(fg="black")
        case 3:
            #print("Player Card 2 suit is Clubs")
            playerCard2SuitValue.config(text="♣", fg="green")
            playerCard2Value.config(fg="green")
        case 4:
            #print("Player Card 2 suit is Diamonds")
            playerCard2SuitValue.config(text="♦", fg="blue")
            playerCard2Value.config(fg="blue")
        case _:
            print("ERROR choosing p2 suit")

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
    p1, p2 = trainer.hardTotalToCards(player_card)
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
        p1, p2 = trainer.hardTotalToCards(player_card)
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

chartButton = tk.Button(window, text="Splits Chart", command=splitsChart)
chartButton.place(x=1700, y=200)

window.mainloop()
