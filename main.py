import tkinter as tk
import trainer

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

def nextSplit():
    global checkAnswer, play_random
    dealer_card, player_card, answer = trainer.playSplits(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer

def nextSoft():
    global checkAnswer, play_random
    dealer_card, player_card, answer = trainer.playSofts(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer

def nextHard():
    global checkAnswer, play_random
    dealer_card, player_card, answer = trainer.playHards(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer

def nextAll():
    global checkAnswer, play_random
    dealer_card, player_card, answer, check_mode = trainer.playAll(play_random)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer
    if(check_mode == "splits"):
        hitBtn.place_forget()
        standBtn.place_forget()
        doubleHitBtn.place_forget()
        doubleStandBtn.place_forget()
        splitYesBtn.place(x=800, y=300)
        splitNoBtn.place(x=900, y=300)
    else:
        splitYesBtn.place_forget()
        splitNoBtn.place_forget()
        hitBtn.place(x=720, y=300)
        standBtn.place(x=775, y=300)
        doubleHitBtn.place(x=850, y=300)
        doubleStandBtn.place(x=975, y=300)

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
    splitYesBtn.place(x=800, y=300)
    splitNoBtn.place(x=900, y=300)
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
    hitBtn.place(x=720, y=300)
    standBtn.place(x=775, y=300)
    doubleHitBtn.place(x=850, y=300)
    doubleStandBtn.place(x=975, y=300)
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
    hitBtn.place(x=720, y=300)
    standBtn.place(x=775, y=300)
    doubleHitBtn.place(x=850, y=300)
    doubleStandBtn.place(x=975, y=300)
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
    else:
        print("Incorrect. Correct answer is Do Not Split")

    if(play_token == "splits"):
        nextSplit()
    else:
        nextAll()

def checkSplitNo():
    global play_token
    print("Split No")
    if(checkAnswer == "N"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is Split")

    if(play_token == "splits"):
        nextSplit()
    else:
        nextAll()

def checkHit():
    global play_token
    print("Hit")
    if(checkAnswer == "H"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

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
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

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
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

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
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

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

splitsBtn = tk.Button(window, text="Play Splits", command=changeToSplits)
splitsBtn.place(x=650, y=25)

softsBtn = tk.Button(window, text="Play Soft Totals", command=changeToSofts)
softsBtn.place(x=750, y=25)

hardsBtn = tk.Button(window, text="Play Hard Totals", command=changeToHards)
hardsBtn.place(x=885, y=25)

allBtn = tk.Button(window, text="Play All", command=changeToAll)
allBtn.place(x=1025, y=25)

dealerCard = tk.Label(window, text="Dealer Card: ", font=("Arial", 20))
dealerCard.place(x=800, y=100)

playerCard = tk.Label(window, text="Player Card: ", font=("Arial", 20))
playerCard.place(x=800, y=150)

correctAnswer = tk.Label(window, text="Correct Answer: ", font=("Arial", 20))
correctAnswer.place(x=800, y=200)

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

window.mainloop()