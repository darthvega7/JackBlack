import os
import sys
import bjbs_chart
# from playTrainer import playSplits

def quit():
    global correct, total
    score = correct / total * 100
    print("Your score: %d correct out of %d total: Score of: %.3f percent" % (correct, total, score))
    sys.exit()

def mainLoop():
    global total
    #splitCheck()
    softCheck()
    quit()

def splitCheck():
    global play_token, total, correct, incorrect, row, col
    if play_token != 'splits':
        row = 1
        col = 1
        correct = 0
        incorrect = 0
        total = 0
        play_token = 'splits'
    while total < 100:
        play_splits = playSplits()
        if(play_splits):
            correct += 1
        else:
            incorrect += 1
        total += 1
        col += 1
        if col > 10:
            col = 1
            row += 1
        input("Press ENTER to continue")
        os.system('clear')

def playSplits():
    global row, col
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
        return False
    else:
        print("Correct!")
        return True

def softCheck():
    global play_token, total, correct, incorrect, row, col
    if play_token != 'softs':
        row = 11
        col = 1
        correct = 0
        incorrect = 0
        total = 0
        play_token = 'softs'
    while total < 80:
        play_softs = playSofts()
        if (play_softs):
            correct += 1
        else:
            incorrect += 1
        total += 1
        col += 1
        if col > 10:
            col = 1
            row += 1
        input("Press ENTER to continue")
        os.system('clear')

def playSofts():
    global row, col
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
        return False
    else:
        print("Correct!")
        return True

play_token = 'none'
row = 1
col = 1
correct = 0
incorrect = 0
total = 0

chart_array = bjbs_chart.chart_array
mainLoop()

# os.system('clear')
# print("Here's how you did, %s!" % yo_name)
# print("")
# print("Hands guessed correctly: %d" % correct_answers)
# print("Hands guessed incorrectly: %d" % incorrect_answers)
# print("Total number of hands: %d" % total_answers)
# print("")
# total_score = correct_answers / total_answers * 100
# print("Your score is %.3f" % total_score)
# print("")