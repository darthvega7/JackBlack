import os
import sys
import bjbs_chart
import random
# from playTrainer import playSplits

def quit():
    global correct, total, incorrect, incorrect_arr
    if total != 0:
        score = correct / total * 100
        print("Your score: %d correct out of %d total: Score of: %.3f percent" % (correct, total, score))
        print("You got %d wrong" % incorrect)
        print("Here are the ones you got wrong: ")
        for wrong in incorrect_arr:
            a, b, c, d = wrong
            print("Dealer Card: %s" % a)
            print("Player Card: %s" % b)
            print("Your answer: %s" % c)
            print("Correct answer: %s" % d)
            print("")
    sys.exit()

def mainLoop():
    global total
    splitCheck(False)
    softCheck(False)
    hardCheck(False)
    # while true:
    # if play_token = 'none', reset stuff
    quit()

def splitCheck(run_random):
    global play_token, total, correct, incorrect, incorrect_arr, row, col
    incorrect_arr = []
    if play_token != 'splits':
        row = 1
        col = 1
        correct = 0
        incorrect = 0
        incorrect_arr = []
        total = 0
        play_token = 'splits'

    if run_random:
        split_array = []
        for i in range(1, 11):
            for j in range(1, 11):
                split_array.append([i, j])
        random.shuffle(split_array)
        for pair in split_array:
            row, col = pair
            play_splits = playSplits()
            if(play_splits):
                correct += 1
            else:
                incorrect += 1
            total += 1
            print("Count = %d" % total)
            input("Press ENTER to continue")
            os.system('clear')

    else:
        split_array = []
        for i in range(1, 11):
            for j in range(1, 11):
                split_array.append([i, j])
        for pair in split_array:
            row, col = pair
            play_splits = playSplits()
            if(play_splits):
                correct += 1
            else:
                incorrect += 1
            total += 1
            print("Count = %d" % total)
            input("Press ENTER to continue")
            os.system('clear')

def playSplits():
    global row, col, incorrect_arr
    dealer_card = chart_array[0][col]
    player_card = chart_array[row][0]
    answer = chart_array[row][col]
    print("Dealer Card: %s" % dealer_card)
    print("Player Card: %s" % player_card)
    print("")
    my_choice = input("Split (Y) or Do Not Split (N): ")
    if my_choice.upper() == 'Q':
        quit()
    if my_choice.upper() != answer:
        print("Incorrect. Correct answer is: %s" % answer)
        incorrect_arr.append([chart_array[0][col], chart_array[row][0], my_choice.upper(), chart_array[row][col]])
        return False
    else:
        print("Correct!")
        return True

def softCheck(run_random):
    global play_token, total, correct, incorrect, incorrect_arr, row, col
    if play_token != 'softs':
        row = 11
        col = 1
        correct = 0
        incorrect = 0
        incorrect_arr = []
        total = 0
        play_token = 'softs'

    if run_random:
        soft_array = []
        for i in range(11, 19):
            for j in range(1, 11):
                soft_array.append([i, j])
        random.shuffle(soft_array)
        for pair in soft_array:
            row, col = pair
            play_softs = playSofts()
            if(play_softs):
                correct += 1
            else:
                incorrect += 1
            total += 1
            print("Count = %d" % total)
            input("Press ENTER to continue")
            os.system('clear')

    else:
        soft_array = []
        for i in range(11, 19):
            for j in range(1, 11):
                soft_array.append([i, j])
        for pair in soft_array:
            row, col = pair
            play_softs = playSofts()
            if(play_softs):
                correct += 1
            else:
                incorrect += 1
            total += 1
            print("Count = %d" % total)
            input("Press ENTER to continue")
            os.system('clear')

def playSofts():
    global row, col, incorrect_arr
    dealer_card = chart_array[0][col]
    player_card = chart_array[row][0]
    answer = chart_array[row][col]
    answer = answer.upper()
    print("Dealer Card: %s" % dealer_card)
    print("Player Card: %s" % player_card)
    print("")
    my_choice = input("Double or Stand (Ds), Double or Hit (Dh), Hit (H), Stand (S): ")
    my_choice = my_choice.upper()
    if my_choice == 'Q':
        quit()
    if my_choice.upper() != answer:
        print("Incorrect. Correct answer is: %s" % answer)
        incorrect_arr.append([chart_array[0][col], chart_array[row][0], my_choice.upper(), chart_array[row][col]])
        return False
    else:
        print("Correct!")
        return True

def hardCheck(run_random):
    global play_token, total, correct, incorrect, incorrect_arr, row, col
    if play_token != 'hards':
        row = 19
        col = 1
        correct = 0
        incorrect = 0
        incorrect_arr = []
        total = 0
        play_token = 'hards'

    if run_random:
        hard_array = []
        for i in range(19, 29):
            for j in range(1, 11):
                hard_array.append([i, j])
        random.shuffle(hard_array)
        for pair in hard_array:
            row, col = pair
            play_hards = playHards()
            if(play_hards):
                correct += 1
            else:
                incorrect += 1
            total += 1
            print("Count = %d" % total)
            input("Press ENTER to continue")
            os.system('clear')

    else:
        hard_array = []
        for i in range(19, 29):
            for j in range(1, 11):
                hard_array.append([i, j])
        for pair in hard_array:
            row, col = pair
            play_hards = playHards()
            if(play_hards):
                correct += 1
            else:
                incorrect += 1
            total += 1
            print("Count = %d" % total)
            input("Press ENTER to continue")
            os.system('clear')

def playHards():
    global row, col, incorrect_arr
    dealer_card = chart_array[0][col]
    player_card = chart_array[row][0]
    answer = chart_array[row][col]
    answer = answer.upper()
    print("Dealer Card: %s" % dealer_card)
    print("Player Card: %s" % player_card)
    print("")
    my_choice = input("Double or Hit (Dh), Hit (H), Stand (S): ")
    my_choice = my_choice.upper()
    if my_choice == 'Q':
        quit()
    if my_choice.upper() != answer:
        print("Incorrect. Correct answer is: %s" % answer)
        incorrect_arr.append([chart_array[0][col], chart_array[row][0], my_choice.upper(), chart_array[row][col]])
        return False
    else:
        print("Correct!")
        return True

play_token = 'none'
row = 1
col = 1
correct = 0
incorrect = 0
incorrect_arr = []
total = 0

chart_array = bjbs_chart.chart_array
mainLoop()