import os
import sys
import bjbs_chart
import random
# from playTrainer import playSplits

def quit():
    sys.exit()

# def mainLoop():
#     global arr_index, split_array, soft_array, hard_array, all_array
#     while arr_index < len(split_array):
#         playSplits(True)

    # while arr_index < len(soft_array):
    #     playSofts(True)

    # while arr_index < len(hard_array):
    #     playHards(True)

    # while arr_index < len(all_array):
    #     playAll(True)
    #quit()

def resetMode():
    global play_token, split_array, soft_array, hard_array, all_array
    play_token = 'none'

    split_array = []
    for i in range(1, 11):
        for j in range(1, 11):
            split_array.append([i, j])

    soft_array = []
    for i in range(11, 19):
        for j in range(1, 11):
            soft_array.append([i, j])

    hard_array = []
    for i in range(19, 29):
        for j in range(1, 11):
            hard_array.append([i, j])

    all_array = []
    for i in range(1, 29):
        for j in range(1, 11):
            all_array.append([i, j])

def playSplits(run_random):
    global play_token, split_array, arr_index, correct, incorrect, answer, incorrect_arr
    if play_token != 'splits':
        correct = 0
        incorrect = 0
        incorrect_arr = []
        arr_index = 0
        play_token = 'splits'
        if(run_random):
            random.shuffle(split_array)

    pair = split_array[arr_index]
    row, col = pair
    dealer_card = chart_array[0][col]
    player_card = chart_array[row][0]
    answer = chart_array[row][col]
    print("Dealer Card: %s" % dealer_card)
    print("Player Card: %s" % player_card)
    print("Answer: %s" % answer)
    print("Count: %d" % arr_index)
    arr_index += 1

    if(arr_index == len(split_array)):
        resetMode()

    return dealer_card, player_card, answer

def playSofts(run_random):
    global play_token, soft_array, arr_index, correct, incorrect, answer, incorrect_arr
    if play_token != 'softs':
        correct = 0
        incorrect = 0
        incorrect_arr = []
        arr_index = 0
        play_token = 'softs'
        if(run_random):
            random.shuffle(soft_array)

    pair = soft_array[arr_index]
    row, col = pair
    dealer_card = chart_array[0][col]
    player_card = chart_array[row][0]
    answer = chart_array[row][col]
    print("Dealer Card: %s" % dealer_card)
    print("Player Card: %s" % player_card)
    print("Answer: %s" % answer)
    print("Count: %d" % arr_index)
    arr_index += 1

    if(arr_index == len(soft_array)):
        resetMode()

    return dealer_card, player_card, answer

def playHards(run_random):
    global play_token, hard_array, arr_index, correct, incorrect, answer, incorrect_arr
    if play_token != 'hards':
        correct = 0
        incorrect = 0
        incorrect_arr = []
        arr_index = 0
        play_token = 'hards'
        if(run_random):
            random.shuffle(hard_array)

    pair = hard_array[arr_index]
    row, col = pair
    dealer_card = chart_array[0][col]
    player_card = chart_array[row][0]
    answer = chart_array[row][col]
    print("Dealer Card: %s" % dealer_card)
    print("Player Card: %s" % player_card)
    print("Answer: %s" % answer)
    print("Count: %d" % arr_index)
    arr_index += 1

    if(arr_index == len(hard_array)):
        resetMode()

    return dealer_card, player_card, answer

def playAll(run_random):
    global play_token, all_array, arr_index, correct, incorrect, answer, incorrect_arr
    if play_token != 'all':
        correct = 0
        incorrect = 0
        incorrect_arr = []
        arr_index = 0
        play_token = 'all'
        if(run_random):
            random.shuffle(all_array)

    pair = all_array[arr_index]
    row, col = pair
    dealer_card = chart_array[0][col]
    player_card = chart_array[row][0]
    answer = chart_array[row][col]
    print("Dealer Card: %s" % dealer_card)
    print("Player Card: %s" % player_card)
    print("Answer: %s" % answer)
    print("Count: %d" % arr_index)
    arr_index += 1

    if(arr_index == len(all_array)):
        resetMode()

    check_mode = ""
    if(row > 0 and row < 11):
        check_mode = "splits"
    else:
        check_mode = "not_splits"

    return dealer_card, player_card, answer, check_mode

play_token = 'none'
arr_index = 0
correct = 0
incorrect = 0
answer = ''
incorrect_arr = []

chart_array = bjbs_chart.chart_array

split_array = []
for i in range(1, 11):
    for j in range(1, 11):
        split_array.append([i, j])

soft_array = []
for i in range(11, 19):
    for j in range(1, 11):
        soft_array.append([i, j])

hard_array = []
for i in range(19, 29):
    for j in range(1, 11):
        hard_array.append([i, j])

all_array = []
for i in range(1, 29):
    for j in range(1, 11):
        all_array.append([i, j])

# mainLoop()