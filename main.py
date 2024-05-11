import tkinter as tk
import trainer_engine as trainer
import visual_chart as vischart
import random

BUTTON_FONT = 20
CARD_FONT = 75
ANSWER_FONT = 30
CORRECT_ANSWER_CANVAS_WIDTH = 500
CORRECT_ANSWER_CANVAS_HEIGHT = 100
INCORRECT_ANSWER_CANVAS_WIDTH = 500
INCORRECT_ANSWER_CANVAS_HEIGHT = 200
ANSWER_CANVAS_X = 705
ANSWER_CANVAS_Y = 370
SPLITS_BTN_X = 500
SPLITS_BTN_Y = 25
SOFTS_BTN_X = 700
SOFTS_BTN_Y = 25
HARDS_BTN_X = 950
HARDS_BTN_Y = 25
ALL_BTN_X = 1210
ALL_BTN_Y = 25
RAND_BTN_X = 1600
RAND_BTN_Y = 25
INORDER_BTN_X = 1600
INORDER_BTN_Y = 80
DEALER_CARD_CANVAS_X = 850
DEALER_CARD_CANVAS_Y = 100
DEALER_CARD_CANVAS_WIDTH = 200
DEALER_CARD_CANVAS_HEIGHT = 300
DEALER_CARD_VALUE_X = 25
DEALER_CARD_VALUE_Y = 25
DEALER_SUIT_VALUE_X = 100
DEALER_SUIT_VALUE_Y = 165
PLAYERCARD1_CANVAS_X = 735
PLAYERCARD1_CANVAS_Y = 450
PLAYERCARD1_CANVAS_WIDTH = 200
PLAYERCARD1_CANVAS_HEIGHT = 300
PLAYERCARD2_CANVAS_X = 985
PLAYERCARD2_CANVAS_Y = 450
PLAYERCARD2_CANVAS_WIDTH = 200
PLAYERCARD2_CANVAS_HEIGHT = 300
PLAYERCARD1_VALUE_X = 25
PLAYERCARD1_VALUE_Y = 25
PLAYERCARD1_SUIT_X = 100
PLAYERCARD1_SUIT_Y = 165
PLAYERCARD2_VALUE_X = 25
PLAYERCARD2_VALUE_Y = 25
PLAYERCARD2_SUIT_X = 100
PLAYERCARD2_SUIT_Y = 165
CHART_BTN_X = 1600
CHART_BTN_Y = 400
SPLIT_YES_BTN_X = 800
SPLIT_YES_BTN_Y = 800
SPLIT_NO_BTN_X = 1005
SPLIT_NO_BTN_Y = 800
HIT_BTN_X = 800
HIT_BTN_Y = 775
STAND_BTN_X = 785
STAND_BTN_Y = 850
DH_BTN_X = 1000
DH_BTN_Y = 775
DS_BTN_X = 985
DS_BTN_Y = 850

checkAnswer = ""
play_token = "none"
play_random = True
count = 0

def resetCards():
    global play_token, count
    dealerCardValue.config(text="X")
    dealerSuitValue.config(text="O")
    playerCard1Value.config(text="X")
    playerCard2Value.config(text="X")
    playerCard1SuitValue.config(text="O")
    playerCard2SuitValue.config(text="O")
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    splitYesBtn.place_forget()
    splitNoBtn.place_forget()
    hitBtn.place_forget()
    standBtn.place_forget()
    doubleHitBtn.place_forget()
    doubleStandBtn.place_forget()
    play_token = "none"
    count = 0

def result(corr, answer):
    global play_token

    def show(time):
        answer_label.place(relx=0.5, rely=0.5, anchor="center")
        window.after(time, hide)
    def hide():
        answer_canvas.place_forget()
        answer_label.place_forget()

    if corr:
        answer_canvas = tk.Canvas(window, width=CORRECT_ANSWER_CANVAS_WIDTH, height=CORRECT_ANSWER_CANVAS_HEIGHT,
                                  bg="green")
        answer_canvas.place(x=ANSWER_CANVAS_X, y=ANSWER_CANVAS_Y)
        answer_label = tk.Label(answer_canvas, text="CORRECT!", font=("Arial", ANSWER_FONT), fg="white", bg="green")
        show(2000)
    else:
        answer_canvas = tk.Canvas(window, width=INCORRECT_ANSWER_CANVAS_WIDTH, height=INCORRECT_ANSWER_CANVAS_HEIGHT,
                                  bg="red")
        answer_canvas.place(x=ANSWER_CANVAS_X, y=ANSWER_CANVAS_Y)
        if answer == "Y":
            answer_label = tk.Label(answer_canvas, text="Incorrect\nCorrect Answer Is:\nSplit",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "N":
            answer_label = tk.Label(answer_canvas, text="Incorrect\nCorrect Answer Is:\nDo Not Split",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "H":
            answer_label = tk.Label(answer_canvas, text="Incorrect\nCorrect Answer Is:\nHit",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "S":
            answer_label = tk.Label(answer_canvas, text="Incorrect\nCorrect Answer Is:\nStand",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "Dh":
            answer_label = tk.Label(answer_canvas, text="Incorrect\nCorrect Answer Is:\nDouble or Hit",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "Ds":
            answer_label = tk.Label(answer_canvas, text="Incorrect\nCorrect Answer Is:\nDouble or Stand",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        else:
            print("Error in Answer")
        show(4000)

def playRandom():
    global play_random, count
    play_random = True
    count = 0
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
    global play_random, count
    play_random = False
    count = 0
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
    global checkAnswer, play_random, count
    dealer_card, player_card, answer = trainer.playSplits(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    curr_count.config(text="Count: " + str(count))
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = player_card.split(",")
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()
    count += 1

def nextSoft():
    global checkAnswer, play_random, count
    dealer_card, player_card, answer = trainer.playSofts(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    curr_count.config(text="Count: " + str(count))
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = player_card.split(",")
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()
    count += 1

def nextHard():
    global checkAnswer, play_random, count
    dealer_card, player_card, answer = trainer.playHards(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    curr_count.config(text="Count: " + str(count))
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = trainer.hardTotalToCards(player_card)
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()
    count += 1

def nextAll():
    global checkAnswer, play_random, count
    dealer_card, player_card, answer, check_mode = trainer.playAll(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    curr_count.config(text="Count: " + str(count))
    checkAnswer = answer
    if(check_mode == "splits"):
        hitBtn.place_forget()
        standBtn.place_forget()
        doubleHitBtn.place_forget()
        doubleStandBtn.place_forget()
        splitYesBtn.place(x=SPLIT_YES_BTN_X, y=SPLIT_YES_BTN_Y)
        splitNoBtn.place(x=SPLIT_NO_BTN_X, y=SPLIT_NO_BTN_Y)
    else:
        splitYesBtn.place_forget()
        splitNoBtn.place_forget()
        hitBtn.place(x=HIT_BTN_X, y=HIT_BTN_Y)
        standBtn.place(x=STAND_BTN_X, y=STAND_BTN_Y)
        doubleHitBtn.place(x=DH_BTN_X, y=DH_BTN_Y)
        doubleStandBtn.place(x=DS_BTN_X, y=DS_BTN_Y)
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
    count += 1

def changeToSplits():
    global play_token, count
    play_token = "splits"
    count = 0
    splitsBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hitBtn.place_forget()
    standBtn.place_forget()
    doubleHitBtn.place_forget()
    doubleStandBtn.place_forget()
    splitYesBtn.place(x=SPLIT_YES_BTN_X, y=SPLIT_YES_BTN_Y)
    splitNoBtn.place(x=SPLIT_NO_BTN_X, y=SPLIT_NO_BTN_Y)
    nextSplit()
def changeToSofts():
    global play_token, count
    play_token = "softs"
    count = 0
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    splitYesBtn.place_forget()
    splitNoBtn.place_forget()
    hitBtn.place(x=HIT_BTN_X, y=HIT_BTN_Y)
    standBtn.place(x=STAND_BTN_X, y=STAND_BTN_Y)
    doubleHitBtn.place(x=DH_BTN_X, y=DH_BTN_Y)
    doubleStandBtn.place(x=DS_BTN_X, y=DS_BTN_Y)
    nextSoft()

def changeToHards():
    global play_token, count
    play_token = "hards"
    count = 0
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    allBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    splitYesBtn.place_forget()
    splitNoBtn.place_forget()
    hitBtn.place(x=HIT_BTN_X, y=HIT_BTN_Y)
    standBtn.place(x=STAND_BTN_X, y=STAND_BTN_Y)
    doubleHitBtn.place(x=DH_BTN_X, y=DH_BTN_Y)
    doubleStandBtn.place(x=DS_BTN_X, y=DS_BTN_Y)
    nextHard()
def changeToAll():
    global play_token, count
    play_token = "all"
    count = 0
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
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is Do Not Split")
        result(False, checkAnswer)

    if(play_token == "splits"):
        if count >= 100:
            resetCards()
        else:
            nextSplit()
    else:
        if count >= 280:
            resetCards()
        else:
            nextAll()

def checkSplitNo():
    global play_token
    print("Split No")
    if(checkAnswer == "N"):
        print("Correct")
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is Split")
        result(False, checkAnswer)

    if(play_token == "splits"):
        if count >= 100:
            resetCards()
        else:
            nextSplit()
    else:
        if count >= 280:
            resetCards()
        else:
            nextAll()

def checkHit():
    global play_token
    print("Hit")
    if(checkAnswer == "H"):
        print("Correct")
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        result(False, checkAnswer)

    if(play_token == "softs"):
        if count >= 80:
            resetCards()
        else:
            nextSoft()
    elif(play_token == "hards"):
        if count >= 100:
            resetCards()
        else:
            nextHard()
    else:
        if count >= 280:
            resetCards()
        else:
            nextAll()

def checkStand():
    print("Stand")
    if(checkAnswer == "S"):
        print("Correct")
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        result(False, checkAnswer)

    if(play_token == "softs"):
        if count >= 80:
            resetCards()
        else:
            nextSoft()
    elif(play_token == "hards"):
        if count >= 100:
            resetCards()
        else:
            nextHard()
    else:
        if count >= 280:
            resetCards()
        else:
            nextAll()

def checkDh():
    print("Double or Hit")
    if(checkAnswer == "Dh"):
        print("Correct")
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        result(False, checkAnswer)

    if(play_token == "softs"):
        if count >= 80:
            resetCards()
        else:
            nextSoft()
    elif(play_token == "hards"):
        if count >= 100:
            resetCards()
        else:
            nextHard()
    else:
        if count >= 280:
            resetCards()
        else:
            nextAll()
def checkDs():
    print("Double or Stand")
    if(checkAnswer == "Ds"):
        print("Correct")
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        result(False, checkAnswer)

    if(play_token == "softs"):
        if count >= 80:
            resetCards()
        else:
            nextSoft()
    elif(play_token == "hards"):
        if count >= 100:
            resetCards()
        else:
            nextHard()
    else:
        if count >= 280:
            resetCards()
        else:
            nextAll()

window = tk.Tk()
window.title("Joshy's BlackJack Basic Strategy Trainer")
window.geometry("1920x1080")
window.geometry("+0+0")
icon = tk.PhotoImage(file="bitcoin.png")
window.iconphoto(True, icon)
window.configure(background="#3aa31a")

splitsBtn = tk.Button(window, text="Play Splits", font=("Arial", BUTTON_FONT), command=changeToSplits)
splitsBtn.place(x=SPLITS_BTN_X, y=SPLITS_BTN_Y)

softsBtn = tk.Button(window, text="Play Soft Totals", font=("Arial", BUTTON_FONT), command=changeToSofts)
softsBtn.place(x=SOFTS_BTN_X, y=SOFTS_BTN_Y)

hardsBtn = tk.Button(window, text="Play Hard Totals", font=("Arial", BUTTON_FONT), command=changeToHards)
hardsBtn.place(x=HARDS_BTN_X, y=HARDS_BTN_Y)

allBtn = tk.Button(window, text="Play All", font=("Arial", BUTTON_FONT), command=changeToAll)
allBtn.place(x=ALL_BTN_X, y=ALL_BTN_Y)

dealerCard = tk.Label(window, text="Dealer Card: ", font=("Arial", BUTTON_FONT))
dealerCard.place(x=100, y=300)

playerCard = tk.Label(window, text="Player Card: ", font=("Arial", BUTTON_FONT))
playerCard.place(x=100, y=350)

curr_count = tk.Label(window, text="Count: ", font=("Arial", BUTTON_FONT))
curr_count.place(x=100, y=400)

randBtn = tk.Button(window, text="Play Random Hands", font=("Arial", BUTTON_FONT), command=playRandom)
inOrderBtn = tk.Button(window, text="Play Hands In Order", font=("Arial", BUTTON_FONT), command=playInOrder)
randBtn.place(x=RAND_BTN_X, y=RAND_BTN_Y)
inOrderBtn.place(x=INORDER_BTN_X, y=INORDER_BTN_Y)
randBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)

splitYesBtn = tk.Button(window, text="Split", font=("Arial", BUTTON_FONT), command=checkSplitYes)
splitNoBtn = tk.Button(window, text="Do Not Split", font=("Arial", BUTTON_FONT), command=checkSplitNo)

hitBtn = tk.Button(window, text="Hit", font=("Arial", BUTTON_FONT), command=checkHit)
standBtn = tk.Button(window, text="Stand", font=("Arial", BUTTON_FONT), command=checkStand)
doubleHitBtn = tk.Button(window, text="Double or Hit", font=("Arial", BUTTON_FONT), command=checkDh)
doubleStandBtn = tk.Button(window, text="Double or Stand", font=("Arial", BUTTON_FONT), command=checkDs)

dealerCardCanvas = tk.Canvas(window, width=DEALER_CARD_CANVAS_WIDTH, height=DEALER_CARD_CANVAS_HEIGHT, bg="white")
dealerCardCanvas.place(x=DEALER_CARD_CANVAS_X, y=DEALER_CARD_CANVAS_Y)

playerCard1Canvas = tk.Canvas(window, width=PLAYERCARD1_CANVAS_WIDTH, height=PLAYERCARD1_CANVAS_HEIGHT, bg="white")
playerCard1Canvas.place(x=PLAYERCARD1_CANVAS_X, y=PLAYERCARD1_CANVAS_Y)
playerCard2Canvas = tk.Canvas(window, width=PLAYERCARD2_CANVAS_WIDTH, height=PLAYERCARD2_CANVAS_HEIGHT, bg="white")
playerCard2Canvas.place(x=PLAYERCARD2_CANVAS_X, y=PLAYERCARD2_CANVAS_Y)

dealerCardValue = tk.Label(dealerCardCanvas, text="X", font=("Arial", CARD_FONT, "bold"), bg="white")
dealerSuitValue = tk.Label(dealerCardCanvas, text="O", font=("Arial", CARD_FONT, "bold"), bg="white")
# dealerCardValue.place(x=875, y=100)
# dealerSuitValue.place(x=950, y=240)
dealerCardValue.place(x=DEALER_CARD_VALUE_X, y=DEALER_CARD_VALUE_Y)
dealerSuitValue.place(x=DEALER_SUIT_VALUE_X, y=DEALER_SUIT_VALUE_Y)

playerCard1Value = tk.Label(playerCard1Canvas, text="X", font=("Arial", CARD_FONT, "bold"), bg="white")
playerCard2Value = tk.Label(playerCard2Canvas, text="X", font=("Arial", CARD_FONT, "bold"), bg="white")
playerCard1SuitValue = tk.Label(playerCard1Canvas, text="O", font=("Arial", CARD_FONT, "bold"), bg="white")
playerCard2SuitValue = tk.Label(playerCard2Canvas, text="O", font=("Arial", CARD_FONT, "bold"), bg="white")

playerCard1Value.place(x=PLAYERCARD1_VALUE_X, y=PLAYERCARD1_VALUE_Y)
playerCard2Value.place(x=PLAYERCARD2_VALUE_X, y=PLAYERCARD2_VALUE_Y)
playerCard1SuitValue.place(x=PLAYERCARD1_SUIT_X, y=PLAYERCARD1_SUIT_Y)
playerCard2SuitValue.place(x=PLAYERCARD2_SUIT_X, y=PLAYERCARD2_SUIT_Y)

chart_btn = tk.Button(window, text="Basic Strategy Chart", font=("Arial", BUTTON_FONT), command=vischart.runMain)
chart_btn.place(x=CHART_BTN_X, y=CHART_BTN_Y)

window.mainloop()