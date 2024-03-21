import tkinter as tk
import trainer

def nextSplit():
    dealer_card, player_card, answer = trainer.playSplits(False)
    dealerCard.config(text="Dealer Card: " + str(dealer_card))
    playerCard.config(text="Player Card: " + str(player_card))
    correctAnswer.config(text="Correct Answer: " + str(answer))

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
    nextBtn.config(command=nextSplit)
def changeToSofts():
    nextBtn.config(command=nextSoft)

def changeToHards():
    nextBtn.config(command=nextHard)

def changeToAll():
    nextBtn.config(command=nextAll)

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

nextBtn = tk.Button(window, text="Next Card", command=nextSplit)
nextBtn.place(x=800, y=300)

window.mainloop()