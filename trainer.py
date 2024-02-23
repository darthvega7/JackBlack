import os
import sys
import bjbs_chart
import random

def quit():
    sys.exit()

def mainLoop():
    global arr_index, split_array, soft_array, hard_array
    while arr_index < len(split_array):
        playSplits(False)
    arr_index = 0

    while arr_index < len(soft_array):
        playSofts(False)
    arr_index = 0

    while arr_index < len(hard_array):
        playHards(False)
    #quit()

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

mainLoop()