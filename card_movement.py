import tkinter as tk

WINDOW_AFTER_SPEED = 2

def moveCardsOffScreen(canvases, window, callback, constants):
    def animate_dealer_card():
        new_y = canvases[0].winfo_y() - 5
        canvases[0].place(y=new_y)
        if new_y > constants['DEALER_CARD_CANVAS_Y_OFFSCREEN']:
            window.after(WINDOW_AFTER_SPEED, animate_dealer_card)
        else:
            animate_player_card1()

    def animate_player_card1():
        new_y = canvases[1].winfo_y() + 5
        canvases[1].place(y=new_y)
        if new_y < constants['PLAYERCARD1_CANVAS_Y_OFFSCREEN']:
            window.after(WINDOW_AFTER_SPEED, animate_player_card1)
        else:
            animate_player_card2()

    def animate_player_card2():
        new_y = canvases[2].winfo_y() + 5
        canvases[2].place(y=new_y)
        if new_y < constants['PLAYERCARD2_CANVAS_Y_OFFSCREEN']:
            window.after(WINDOW_AFTER_SPEED, animate_player_card2)
        else:
            if callback:
                callback()  # Call the callback function

    if canvases[0].winfo_y() > constants['DEALER_CARD_CANVAS_Y_OFFSCREEN']:
        animate_dealer_card()
    elif canvases[1].winfo_y() < constants['PLAYERCARD1_CANVAS_Y_OFFSCREEN']:
        animate_player_card1()
    elif canvases[2].winfo_y() < constants['PLAYERCARD2_CANVAS_Y_OFFSCREEN']:
        animate_player_card2()

def moveCardsOnScreen(canvases, window, constants):
    def animate_dealer_card():
        new_y = canvases[0].winfo_y() + 5
        canvases[0].place(y=new_y)
        if new_y < constants['DEALER_CARD_CANVAS_Y']:
            window.after(WINDOW_AFTER_SPEED, animate_dealer_card)
        else:
            animate_player_card1()

    def animate_player_card1():
        new_y = canvases[1].winfo_y() - 5
        canvases[1].place(y=new_y)
        if new_y > constants['PLAYERCARD1_CANVAS_Y']:
            window.after(WINDOW_AFTER_SPEED, animate_player_card1)
        else:
            animate_player_card2()

    def animate_player_card2():
        new_y = canvases[2].winfo_y() - 5
        canvases[2].place(y=new_y)
        if new_y > constants['PLAYERCARD2_CANVAS_Y']:
            window.after(WINDOW_AFTER_SPEED, animate_player_card2)

    if canvases[0].winfo_y() < constants['DEALER_CARD_CANVAS_Y']:
        animate_dealer_card()
    elif canvases[1].winfo_y() > constants['PLAYERCARD1_CANVAS_Y']:
        animate_player_card1()
    elif canvases[2].winfo_y() > constants['PLAYERCARD2_CANVAS_Y']:
        animate_player_card2()