import tkinter as tk
import trainer_engine as trainer
import visual_chart as vischart
import random
from card_movement import moveCardsOffScreen, moveCardsOnScreen

ANIMATION = True
FIRST_CARD = True

BG_COLOR = "#135900"
SPLIT_YES_BG_COLOR = "#3aa31a"
SPLIT_NO_BG_COLOR = "#d1544b"
HIT_BG_COLOR = "#d1544b"
STAND_BG_COLOR = "#efc514"
DH_BG_COLOR = "#24b670"
DS_BG_COLOR = "#3ebab4"

SPLIT_YES_ACTIVE_BG = "#246311"
SPLIT_NO_ACTIVE_BG = "#9c332c"
HIT_ACTIVE_BG = "#9c332c"
STAND_ACTIVE_BG = "#b59510"
DH_ACTIVE_BG = "#248556"
DS_ACTIVE_BG = "#1e706c"

BUTTON_FONT = 20
CARD_FONT = 75
ANSWER_FONT = 30
CORRECT_ANSWER_CANVAS_WIDTH = 500
CORRECT_ANSWER_CANVAS_HEIGHT = 100
INCORRECT_ANSWER_CANVAS_WIDTH = 500
INCORRECT_ANSWER_CANVAS_HEIGHT = 200
ANSWER_CANVAS_X = 705
ANSWER_CANVAS_Y = 370
SPLITS_BTN_X = 510
SPLITS_BTN_Y = 25
SOFTS_BTN_X = 710
SOFTS_BTN_Y = 25
HARDS_BTN_X = 960
HARDS_BTN_Y = 25
ALL_BTN_X = 1220
ALL_BTN_Y = 25
RAND_BTN_X = 20
RAND_BTN_Y = 25
INORDER_BTN_X = 20
INORDER_BTN_Y = 90
DEALER_CARD_CANVAS_X = 850
DEALER_CARD_CANVAS_Y = 100
DEALER_CARD_CANVAS_Y_OFFSCREEN = -400
DEALER_CARD_CANVAS_WIDTH = 200
DEALER_CARD_CANVAS_HEIGHT = 300
DEALER_CARD_VALUE_X = 25
DEALER_CARD_VALUE_Y = 25
DEALER_SUIT_VALUE_X = 100
DEALER_SUIT_VALUE_Y = 165
PLAYERCARD1_CANVAS_X = 735
PLAYERCARD1_CANVAS_Y = 450
PLAYERCARD1_CANVAS_Y_OFFSCREEN = 1180
PLAYERCARD1_CANVAS_WIDTH = 200
PLAYERCARD1_CANVAS_HEIGHT = 300
PLAYERCARD2_CANVAS_X = 985
PLAYERCARD2_CANVAS_Y = 450
PLAYERCARD2_CANVAS_Y_OFFSCREEN = 1180
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
CHART_BTN_X = 20
CHART_BTN_Y = 400
SPLIT_YES_BTN_X = 1250
SPLIT_YES_BTN_Y = 365
SPLIT_NO_BTN_X = 1250
SPLIT_NO_BTN_Y = 440
HIT_BTN_X = 1250
HIT_BTN_Y = 290
STAND_BTN_X = 1250
STAND_BTN_Y = 365
DH_BTN_X = 1250
DH_BTN_Y = 440
DS_BTN_X = 1250
DS_BTN_Y = 515
ACTION_BUTTON_WIDTH = 15
ACTION_BUTTON_HEIGHT = 2
ACTION_BUTTON_BORDER = 5
CLOSE_BTN_X = 860
CLOSE_BTN_Y = 875

checkAnswer = ""
play_token = "none"
play_random = True
count = 0
correct_count = 0
incorrect_count = 0
last_card_played = False


def resetCards():
    global play_token, count
    if not ANIMATION:
        dealerCardValue.config(text="")
        dealerSuitValue.config(text="")
        playerCard1Value.config(text="")
        playerCard2Value.config(text="")
        playerCard1SuitValue.config(text="")
        playerCard2SuitValue.config(text="")
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


def disable_action_buttons():
    splitYesBtn.config(state=tk.DISABLED)
    splitNoBtn.config(state=tk.DISABLED)
    hitBtn.config(state=tk.DISABLED)
    standBtn.config(state=tk.DISABLED)
    doubleHitBtn.config(state=tk.DISABLED)
    doubleStandBtn.config(state=tk.DISABLED)
    splitsBtn.config(state=tk.DISABLED)
    softsBtn.config(state=tk.DISABLED)
    hardsBtn.config(state=tk.DISABLED)
    allBtn.config(state=tk.DISABLED)
    randBtn.config(state=tk.DISABLED)
    inOrderBtn.config(state=tk.DISABLED)


def enable_action_buttons():
    global play_token, play_random

    splitYesBtn.config(state=tk.NORMAL)
    splitNoBtn.config(state=tk.NORMAL)
    hitBtn.config(state=tk.NORMAL)
    standBtn.config(state=tk.NORMAL)
    doubleHitBtn.config(state=tk.NORMAL)
    doubleStandBtn.config(state=tk.NORMAL)
    if play_token == "splits":
        softsBtn.config(state=tk.NORMAL)
        hardsBtn.config(state=tk.NORMAL)
        allBtn.config(state=tk.NORMAL)
    elif play_token == "softs":
        splitsBtn.config(state=tk.NORMAL)
        hardsBtn.config(state=tk.NORMAL)
        allBtn.config(state=tk.NORMAL)
    elif play_token == "hards":
        splitsBtn.config(state=tk.NORMAL)
        softsBtn.config(state=tk.NORMAL)
        allBtn.config(state=tk.NORMAL)
    elif play_token == "all":
        splitsBtn.config(state=tk.NORMAL)
        softsBtn.config(state=tk.NORMAL)
        hardsBtn.config(state=tk.NORMAL)
    if play_random:
        inOrderBtn.config(state=tk.NORMAL)
    else:
        randBtn.config(state=tk.NORMAL)


def result(corr, answer):
    def show(time):
        global should_continue
        should_continue = False
        disable_action_buttons()
        answer_label.place(relx=0.5, rely=0.5, anchor="center")
        window.after(time, hide)
        while not should_continue:
            window.update()

    def hide():
        global should_continue
        answer_canvas.place_forget()
        answer_label.place_forget()
        should_continue = True
        if not ANIMATION:
            enable_action_buttons()
        # if ANIMATION:
            # moveCardsOffScreen([dealerCardCanvas, playerCard1Canvas, playerCard2Canvas], window,
            #                    updateCardValuesAndMoveCardsOnScreen, constants)

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
            answer_label = tk.Label(answer_canvas, text="INCORRECT\nCorrect Answer Is:\nSPLIT",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "N":
            answer_label = tk.Label(answer_canvas, text="INCORRECT\nCorrect Answer Is:\nDO NOT SPLIT",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "H":
            answer_label = tk.Label(answer_canvas, text="INCORRECT\nCorrect Answer Is:\nHIT",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "S":
            answer_label = tk.Label(answer_canvas, text="INCORRECT\nCorrect Answer Is:\nSTAND",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "Dh":
            answer_label = tk.Label(answer_canvas, text="INCORRECT\nCorrect Answer Is:\nDOUBLE OR HIT",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        elif answer == "Ds":
            answer_label = tk.Label(answer_canvas, text="INCORRECT\nCorrect Answer Is:\nDOUBLE OR STAND",
                                    font=("Arial", ANSWER_FONT), fg="white", bg="red")
        else:
            print("Error in Answer")
        show(4000)


def playRandom():
    global play_random, play_token, count, correct_count, incorrect_count
    play_random = True
    count = 0
    correct_count = 0
    incorrect_count = 0
    if ANIMATION:
        startCardAnimations()
    correct_label.config(text="Correct: " + str(correct_count))
    incorrect_label.config(text="Incorrect: " + str(incorrect_count))
    if play_token == "splits" or play_token == "hards":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    elif play_token == "softs":
        curr_count.config(text="Cards Played: " + str(count) + "/80")
    elif play_token == "all":
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    else:
        curr_count.config(text="Cards Played: ")
    trainer.resetMode()
    randBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    inOrderBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    if not ANIMATION:
        if play_token == "splits":
            nextSplit()
        elif play_token == "softs":
            nextSoft()
        elif play_token == "hards":
            nextHard()
        elif play_token == "all":
            nextAll()

def playInOrder():
    global play_random, play_token, count, correct_count, incorrect_count
    play_random = False
    count = 0
    correct_count = 0
    incorrect_count = 0
    if ANIMATION:
        startCardAnimations()
    correct_label.config(text="Correct: " + str(correct_count))
    incorrect_label.config(text="Incorrect: " + str(incorrect_count))
    if play_token == "splits" or play_token == "hards":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    elif play_token == "softs":
        curr_count.config(text="Cards Played: " + str(count) + "/80")
    elif play_token == "all":
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    else:
        curr_count.config(text="Cards Played: ")
    trainer.resetMode()
    randBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    inOrderBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    if not ANIMATION:
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
            dealerSuitValue.config(text="♥", fg="red")
            dealerCardValue.config(fg="red")
        case 2:
            dealerSuitValue.config(text="♠", fg="black")
            dealerCardValue.config(fg="black")
        case 3:
            dealerSuitValue.config(text="♣", fg="green")
            dealerCardValue.config(fg="green")
        case 4:
            dealerSuitValue.config(text="♦", fg="blue")
            dealerCardValue.config(fg="blue")
        case _:
            print("ERROR choosing dealer suit")

    random_p1_suit = random.randint(1, 4)
    random_p2_suit = random.randint(1, 4)
    match(random_p1_suit):
        case 1:
            playerCard1SuitValue.config(text="♥", fg="red")
            playerCard1Value.config(fg="red")
        case 2:
            playerCard1SuitValue.config(text="♠", fg="black")
            playerCard1Value.config(fg="black")
        case 3:
            playerCard1SuitValue.config(text="♣", fg="green")
            playerCard1Value.config(fg="green")
        case 4:
            playerCard1SuitValue.config(text="♦", fg="blue")
            playerCard1Value.config(fg="blue")
        case _:
            print("ERROR choosing p1 suit")

    match(random_p2_suit):
        case 1:
            playerCard2SuitValue.config(text="♥", fg="red")
            playerCard2Value.config(fg="red")
        case 2:
            playerCard2SuitValue.config(text="♠", fg="black")
            playerCard2Value.config(fg="black")
        case 3:
            playerCard2SuitValue.config(text="♣", fg="green")
            playerCard2Value.config(fg="green")
        case 4:
            playerCard2SuitValue.config(text="♦", fg="blue")
            playerCard2Value.config(fg="blue")
        case _:
            print("ERROR choosing p2 suit")


def nextSplit():
    global checkAnswer, play_random, count
    dealer_card, player_card, answer = trainer.playSplits(play_random)
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = player_card.split(",")
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()
    if ANIMATION:
        moveCardsOnScreen([dealerCardCanvas, playerCard1Canvas, playerCard2Canvas], window, constants)


def nextSoft():
    global checkAnswer, play_random, count
    dealer_card, player_card, answer = trainer.playSofts(play_random)
    curr_count.config(text="Cards Played: " + str(count) + "/80")
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = player_card.split(",")
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()
    if ANIMATION:
        moveCardsOnScreen([dealerCardCanvas, playerCard1Canvas, playerCard2Canvas], window, constants)


def nextHard():
    global checkAnswer, play_random, count
    dealer_card, player_card, answer = trainer.playHards(play_random)
    curr_count.config(text="Cards Played: " + str(count) + "/100")
    checkAnswer = answer
    dealerCardValue.config(text=dealer_card)
    p1, p2 = trainer.hardTotalToCards(player_card)
    playerCard1Value.config(text=p1)
    playerCard2Value.config(text=p2)
    randomSuit()
    if ANIMATION:
        moveCardsOnScreen([dealerCardCanvas, playerCard1Canvas, playerCard2Canvas], window, constants)


def nextAll():
    global checkAnswer, play_random, count
    dealer_card, player_card, answer, check_mode = trainer.playAll(play_random)
    curr_count.config(text="Cards Played: " + str(count) + "/280")
    checkAnswer = answer
    if check_mode == "splits":
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
    if check_mode == "splits":
        dealerCardValue.config(text=dealer_card)
        p1, p2 = player_card.split(",")
        playerCard1Value.config(text=p1)
        playerCard2Value.config(text=p2)
    elif check_mode == "softs":
        dealerCardValue.config(text=dealer_card)
        p1, p2 = player_card.split(",")
        playerCard1Value.config(text=p1)
        playerCard2Value.config(text=p2)
    elif check_mode == "hards":
        dealerCardValue.config(text=dealer_card)
        p1, p2 = trainer.hardTotalToCards(player_card)
        playerCard1Value.config(text=p1)
        playerCard2Value.config(text=p2)
    else:
        print("ERROR in All Mode: Mode Not Found")
    randomSuit()
    if ANIMATION:
        moveCardsOnScreen([dealerCardCanvas, playerCard1Canvas, playerCard2Canvas], window, constants)


def changeToSplits():
    global play_token, count, correct_count, incorrect_count, FIRST_CARD
    play_token = "splits"
    count = 0
    correct_count = 0
    incorrect_count = 0
    if ANIMATION:
        disable_action_buttons()
        startCardAnimations()
    correct_label.config(text="Correct: " + str(correct_count))
    incorrect_label.config(text="Incorrect: " + str(incorrect_count))
    curr_count.config(text="Cards Played: " + str(count) + "/100")
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
    if not ANIMATION or FIRST_CARD:
        nextSplit()
    if FIRST_CARD:
        FIRST_CARD = False
        if ANIMATION:
            window.after(900, enable_action_buttons)


def changeToSofts():
    global play_token, count, correct_count, incorrect_count, FIRST_CARD
    play_token = "softs"
    count = 0
    correct_count = 0
    incorrect_count = 0
    if ANIMATION:
        disable_action_buttons()
        startCardAnimations()
    correct_label.config(text="Correct: " + str(correct_count))
    incorrect_label.config(text="Incorrect: " + str(incorrect_count))
    curr_count.config(text="Cards Played: " + str(count) + "/80")
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
    if not ANIMATION or FIRST_CARD:
        nextSoft()
    if FIRST_CARD:
        FIRST_CARD = False
        if ANIMATION:
            window.after(900, enable_action_buttons)

def changeToHards():
    global play_token, count, correct_count, incorrect_count, FIRST_CARD
    play_token = "hards"
    count = 0
    correct_count = 0
    incorrect_count = 0
    if ANIMATION:
        disable_action_buttons()
        startCardAnimations()
    correct_label.config(text="Correct: " + str(correct_count))
    incorrect_label.config(text="Incorrect: " + str(incorrect_count))
    curr_count.config(text="Cards Played: " + str(count) + "/100")
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
    if not ANIMATION or FIRST_CARD:
        nextHard()
    if FIRST_CARD:
        FIRST_CARD = False
        if ANIMATION:
            window.after(900, enable_action_buttons)

def changeToAll():
    global play_token, count, correct_count, incorrect_count, FIRST_CARD
    play_token = "all"
    count = 0
    correct_count = 0
    incorrect_count = 0
    if ANIMATION:
        disable_action_buttons()
        startCardAnimations()
    correct_label.config(text="Correct: " + str(correct_count))
    incorrect_label.config(text="Incorrect: " + str(incorrect_count))
    curr_count.config(text="Cards Played: " + str(count) + "/280")
    splitsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    softsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    hardsBtn.config(relief=tk.RAISED, state=tk.NORMAL)
    allBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)
    if not ANIMATION or FIRST_CARD:
        nextAll()
    if FIRST_CARD:
        FIRST_CARD = False
        if ANIMATION:
            window.after(900, enable_action_buttons)

def checkSplitYes():
    global play_token, count, correct_count, incorrect_count, last_card_played
    print("Split Yes")
    count += 1
    if play_token == "splits":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    else:
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    if checkAnswer == "Y":
        print("Correct")
        correct_count += 1
        correct_label.config(text="Correct: " + str(correct_count))
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is Do Not Split")
        incorrect_count += 1
        incorrect_label.config(text="Incorrect: " + str(incorrect_count))
        result(False, checkAnswer)
    if(play_token == "splits"):
        if count >= 100:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextSplit()
            else:
                startCardAnimations()
    else:
        if count >= 280:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextAll()
            else:
                startCardAnimations()

def checkSplitNo():
    global play_token, count, correct_count, incorrect_count, last_card_played
    print("Split No")
    count += 1
    if play_token == "splits":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    else:
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    if checkAnswer == "N":
        print("Correct")
        correct_count += 1
        correct_label.config(text="Correct: " + str(correct_count))
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is Split")
        incorrect_count += 1
        incorrect_label.config(text="Incorrect: " + str(incorrect_count))
        result(False, checkAnswer)
    if(play_token == "splits"):
        if count >= 100:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextSplit()
            else:
                startCardAnimations()
    else:
        if count >= 280:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextAll()
            else:
                startCardAnimations()

def checkHit():
    global play_token, count, correct_count, incorrect_count, last_card_played
    print("Hit")
    count += 1
    if play_token == "softs":
        curr_count.config(text="Cards Played: " + str(count) + "/80")
    elif play_token == "hards":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    elif play_token == "all":
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    if checkAnswer == "H":
        print("Correct")
        correct_count += 1
        correct_label.config(text="Correct: " + str(correct_count))
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        incorrect_count += 1
        incorrect_label.config(text="Incorrect: " + str(incorrect_count))
        result(False, checkAnswer)
    if(play_token == "softs"):
        if count >= 80:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextSoft()
            else:
                startCardAnimations()
    elif(play_token == "hards"):
        if count >= 100:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextHard()
            else:
                startCardAnimations()
    else:
        if count >= 280:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextAll()
            else:
                startCardAnimations()


def checkStand():
    global play_token, count, correct_count, incorrect_count, last_card_played
    print("Stand")
    count += 1
    if play_token == "softs":
        curr_count.config(text="Cards Played: " + str(count) + "/80")
    elif play_token == "hards":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    elif play_token == "all":
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    if checkAnswer == "S":
        print("Correct")
        correct_count += 1
        correct_label.config(text="Correct: " + str(correct_count))
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        incorrect_count += 1
        incorrect_label.config(text="Incorrect: " + str(incorrect_count))
        result(False, checkAnswer)
    if(play_token == "softs"):
        if count >= 80:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextSoft()
            else:
                startCardAnimations()
    elif(play_token == "hards"):
        if count >= 100:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextHard()
            else:
                startCardAnimations()
    else:
        if count >= 280:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextAll()
            else:
                startCardAnimations()

def checkDh():
    global play_token, count, correct_count, incorrect_count, last_card_played
    print("Double or Hit")
    count += 1
    if play_token == "softs":
        curr_count.config(text="Cards Played: " + str(count) + "/80")
    elif play_token == "hards":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    elif play_token == "all":
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    if checkAnswer == "Dh":
        print("Correct")
        correct_count += 1
        correct_label.config(text="Correct: " + str(correct_count))
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        incorrect_count += 1
        incorrect_label.config(text="Incorrect: " + str(incorrect_count))
        result(False, checkAnswer)
    if(play_token == "softs"):
        if count >= 80:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextSoft()
            else:
                startCardAnimations()
    elif(play_token == "hards"):
        if count >= 100:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextHard()
            else:
                startCardAnimations()
    else:
        if count >= 280:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextAll()
            else:
                startCardAnimations()

def checkDs():
    global play_token, count, correct_count, incorrect_count, last_card_played
    print("Double or Stand")
    count += 1
    if play_token == "softs":
        curr_count.config(text="Cards Played: " + str(count) + "/80")
    elif play_token == "hards":
        curr_count.config(text="Cards Played: " + str(count) + "/100")
    elif play_token == "all":
        curr_count.config(text="Cards Played: " + str(count) + "/280")
    if checkAnswer == "Ds":
        print("Correct")
        correct_count += 1
        correct_label.config(text="Correct: " + str(correct_count))
        result(True, checkAnswer)
    else:
        print("Incorrect. Correct answer is: " + checkAnswer)
        incorrect_count += 1
        incorrect_label.config(text="Incorrect: " + str(incorrect_count))
        result(False, checkAnswer)
    # if ANIMATION:
    #     startCardAnimations()
    if(play_token == "softs"):
        if count >= 80:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextSoft()
            else:
                startCardAnimations()
    elif(play_token == "hards"):
        if count >= 100:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextHard()
            else:
                startCardAnimations()
    else:
        if count >= 280:
            last_card_played = True
            startCardAnimations()
            resetCards()
        else:
            if not ANIMATION:
                nextAll()
            else:
                startCardAnimations()

def close_window():
    window.destroy()


# <--------------------------   Updates Functions ---------------------------------->

def updateCardValuesAndMoveCardsOnScreen():
    global last_card_played, FIRST_CARD
    updateCardValues()
    if last_card_played:
        last_card_played = False
        FIRST_CARD = True
    else:
        moveCardsBackOnScreen()

def updateCardValues():
    global play_token
    if play_token == "splits":
        nextSplit()
    elif play_token == "softs":
        nextSoft()
    elif play_token == "hards":
        nextHard()
    elif play_token == "all":
        nextAll()


def moveCardsBackOnScreen():
    moveCardsOnScreen([dealerCardCanvas, playerCard1Canvas, playerCard2Canvas], window, constants)
    #enable_action_buttons()
    window.after(900, enable_action_buttons)


def startCardAnimations():
    #disable_action_buttons()
    moveCardsOffScreen([dealerCardCanvas, playerCard1Canvas, playerCard2Canvas], window,
                       updateCardValuesAndMoveCardsOnScreen, constants)


# <--------------------------   Updates Functions ---------------------------------->


window = tk.Tk()
window.title("Joshy's BlackJack Basic Strategy Trainer")
window.geometry("1920x1080")
window.geometry("+0+0")
icon = tk.PhotoImage(file="bitcoin.png")
window.iconphoto(True, icon)
window.configure(background=BG_COLOR)

splitsBtn = tk.Button(window, text="Play Splits", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                      command=changeToSplits)
splitsBtn.place(x=SPLITS_BTN_X, y=SPLITS_BTN_Y)

softsBtn = tk.Button(window, text="Play Soft Totals", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                     command=changeToSofts)
softsBtn.place(x=SOFTS_BTN_X, y=SOFTS_BTN_Y)

hardsBtn = tk.Button(window, text="Play Hard Totals", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                     command=changeToHards)
hardsBtn.place(x=HARDS_BTN_X, y=HARDS_BTN_Y)

allBtn = tk.Button(window, text="Play All", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                   command=changeToAll)
allBtn.place(x=ALL_BTN_X, y=ALL_BTN_Y)

curr_count = tk.Label(window, text="Cards Played: ", font=("Arial", BUTTON_FONT))
curr_count.place(x=50, y=600)
correct_label = tk.Label(window, text="Correct: 0", font=("Arial", BUTTON_FONT), fg="green")
correct_label.place(x=50, y=650)
incorrect_label = tk.Label(window, text="Incorrect: 0", font=("Arial", BUTTON_FONT), fg="red")
incorrect_label.place(x=50, y=700)

randBtn = tk.Button(window, text="Play Random Hands", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                    command=playRandom)
inOrderBtn = tk.Button(window, text="Play Hands In Order", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                       command=playInOrder)
randBtn.place(x=RAND_BTN_X, y=RAND_BTN_Y)
inOrderBtn.place(x=INORDER_BTN_X, y=INORDER_BTN_Y)
randBtn.config(relief=tk.SUNKEN, state=tk.DISABLED)

splitYesBtn = tk.Button(window, text="Split", width=ACTION_BUTTON_WIDTH, height=ACTION_BUTTON_HEIGHT,
                        font=("Arial", BUTTON_FONT), bg=SPLIT_YES_BG_COLOR, bd=ACTION_BUTTON_BORDER,
                        activebackground=SPLIT_YES_ACTIVE_BG, command=checkSplitYes)

splitNoBtn = tk.Button(window, text="Do Not Split", width=ACTION_BUTTON_WIDTH, height=ACTION_BUTTON_HEIGHT,
                       font=("Arial", BUTTON_FONT), bg=SPLIT_NO_BG_COLOR, bd=ACTION_BUTTON_BORDER,
                       activebackground=SPLIT_NO_ACTIVE_BG, command=checkSplitNo)

hitBtn = tk.Button(window, text="Hit", width=ACTION_BUTTON_WIDTH, height=ACTION_BUTTON_HEIGHT,
                   font=("Arial", BUTTON_FONT), bg=HIT_BG_COLOR, bd=ACTION_BUTTON_BORDER,
                   activebackground=HIT_ACTIVE_BG, command=checkHit)
standBtn = tk.Button(window, text="Stand", width=ACTION_BUTTON_WIDTH, height=ACTION_BUTTON_HEIGHT,
                     font=("Arial", BUTTON_FONT), bg=STAND_BG_COLOR, bd=ACTION_BUTTON_BORDER,
                     activebackground=STAND_ACTIVE_BG, command=checkStand)
doubleHitBtn = tk.Button(window, text="Double or Hit", width=ACTION_BUTTON_WIDTH, height=ACTION_BUTTON_HEIGHT,
                         font=("Arial", BUTTON_FONT), bg=DH_BG_COLOR, bd=ACTION_BUTTON_BORDER,
                         activebackground=DH_ACTIVE_BG, command=checkDh)
doubleStandBtn = tk.Button(window, text="Double or Stand", width=ACTION_BUTTON_WIDTH, height=ACTION_BUTTON_HEIGHT,
                           font=("Arial", BUTTON_FONT), bg=DS_BG_COLOR, bd=ACTION_BUTTON_BORDER,
                           activebackground=DS_ACTIVE_BG, command=checkDs)

dealerCardCanvas = tk.Canvas(window, width=DEALER_CARD_CANVAS_WIDTH, height=DEALER_CARD_CANVAS_HEIGHT, bg="white")
playerCard1Canvas = tk.Canvas(window, width=PLAYERCARD1_CANVAS_WIDTH, height=PLAYERCARD1_CANVAS_HEIGHT, bg="white")
playerCard2Canvas = tk.Canvas(window, width=PLAYERCARD2_CANVAS_WIDTH, height=PLAYERCARD2_CANVAS_HEIGHT, bg="white")

if ANIMATION:
    dealerCardCanvas.place(x=DEALER_CARD_CANVAS_X, y=DEALER_CARD_CANVAS_Y_OFFSCREEN)
    playerCard1Canvas.place(x=PLAYERCARD1_CANVAS_X, y=PLAYERCARD1_CANVAS_Y_OFFSCREEN)
    playerCard2Canvas.place(x=PLAYERCARD2_CANVAS_X, y=PLAYERCARD2_CANVAS_Y_OFFSCREEN)
else:
    dealerCardCanvas.place(x=DEALER_CARD_CANVAS_X, y=DEALER_CARD_CANVAS_Y)
    playerCard1Canvas.place(x=PLAYERCARD1_CANVAS_X, y=PLAYERCARD1_CANVAS_Y)
    playerCard2Canvas.place(x=PLAYERCARD2_CANVAS_X, y=PLAYERCARD2_CANVAS_Y)

dealerCardValue = tk.Label(dealerCardCanvas, text="", font=("Arial", CARD_FONT, "bold"), bg="white")
dealerSuitValue = tk.Label(dealerCardCanvas, text="", font=("Arial", CARD_FONT, "bold"), bg="white")
dealerCardValue.place(x=DEALER_CARD_VALUE_X, y=DEALER_CARD_VALUE_Y)
dealerSuitValue.place(x=DEALER_SUIT_VALUE_X, y=DEALER_SUIT_VALUE_Y)

playerCard1Value = tk.Label(playerCard1Canvas, text="", font=("Arial", CARD_FONT, "bold"), bg="white")
playerCard2Value = tk.Label(playerCard2Canvas, text="", font=("Arial", CARD_FONT, "bold"), bg="white")
playerCard1SuitValue = tk.Label(playerCard1Canvas, text="", font=("Arial", CARD_FONT, "bold"), bg="white")
playerCard2SuitValue = tk.Label(playerCard2Canvas, text="", font=("Arial", CARD_FONT, "bold"), bg="white")

playerCard1Value.place(x=PLAYERCARD1_VALUE_X, y=PLAYERCARD1_VALUE_Y)
playerCard2Value.place(x=PLAYERCARD2_VALUE_X, y=PLAYERCARD2_VALUE_Y)
playerCard1SuitValue.place(x=PLAYERCARD1_SUIT_X, y=PLAYERCARD1_SUIT_Y)
playerCard2SuitValue.place(x=PLAYERCARD2_SUIT_X, y=PLAYERCARD2_SUIT_Y)

chart_btn = tk.Button(window, text="Basic Strategy Chart", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                      command=vischart.runMain)
chart_btn.place(x=CHART_BTN_X, y=CHART_BTN_Y)

close_btn = tk.Button(window, text="Close Window", font=("Arial", BUTTON_FONT), bd=ACTION_BUTTON_BORDER,
                      command=close_window)
close_btn.place(x=CLOSE_BTN_X, y=CLOSE_BTN_Y)

constants = {
    'DEALER_CARD_CANVAS_Y_OFFSCREEN': DEALER_CARD_CANVAS_Y_OFFSCREEN,
    'PLAYERCARD1_CANVAS_Y_OFFSCREEN': PLAYERCARD1_CANVAS_Y_OFFSCREEN,
    'PLAYERCARD2_CANVAS_Y_OFFSCREEN': PLAYERCARD2_CANVAS_Y_OFFSCREEN,
    'DEALER_CARD_CANVAS_Y': DEALER_CARD_CANVAS_Y,
    'PLAYERCARD1_CANVAS_Y': PLAYERCARD1_CANVAS_Y,
    'PLAYERCARD2_CANVAS_Y': PLAYERCARD2_CANVAS_Y,
}

window.mainloop()
