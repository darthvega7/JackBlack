import tkinter as tk
import trainer

checkAnswer = ""

def nextSplit():
    global checkAnswer
    dealer_card, player_card, answer = trainer.playSplits(False)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))
    checkAnswer = answer

def nextSoft():
    dealer_card, player_card, answer = trainer.playSofts(False)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))

def nextHard():
    dealer_card, player_card, answer = trainer.playHards(False)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))

def nextAll():
    dealer_card, player_card, answer = trainer.playAll(False)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))

def changeToSplits():
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
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    nextAll()
def checkSplitYes():
    print("Split Yes")
    if(checkAnswer == "Y"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is Do Not Split")
    nextSplit()

def checkSplitNo():
    print("Split No")
    if(checkAnswer == "N"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is Split")
    nextSplit()

def checkHit():
    print("Hit")
    if(checkAnswer == "H"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

def checkStand():
    print("Stand")
    if(checkAnswer == "S"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

def checkDh():
    print("Double or Hit")
    if(checkAnswer == "Dh"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

def checkDs():
    print("Double or Stand")
    if(checkAnswer == "Ds"):
        print("Correct")
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)

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

# nextBtn = tk.Button(window, text="Next Card", command=nextSplit)
# nextBtn.place(x=800, y=300)

splitYesBtn = tk.Button(window, text="Split", command=checkSplitYes)
splitNoBtn = tk.Button(window, text="Do Not Split", command=checkSplitNo)

hitBtn = tk.Button(window, text="Hit", command=checkHit)
standBtn = tk.Button(window, text="Stand", command=checkStand)
doubleHitBtn = tk.Button(window, text="Double or Hit", command=checkDh)
doubleStandBtn = tk.Button(window, text="Double or Stand", command=checkDs)

window.mainloop()