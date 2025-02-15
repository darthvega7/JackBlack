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
    elif(row >= 11 and row < 19):
        check_mode = "softs"
    elif(row >= 19 and row < 29):
        check_mode = "hards"
    else:
        check_mode = "none"

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