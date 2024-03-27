
rows = 29
columns = 11

chart_array = [[0 for _ in range(columns)] for _ in range(rows)]

# Dealer Up Cards:
chart_array[0][0] = 'X' # NEXUS
chart_array[0][1] = 2 # VS Dealer 2
chart_array[0][2] = 3 # VS Dealer 3
chart_array[0][3] = 4 # VS Dealer 4
chart_array[0][4] = 5 # VS Dealer 5
chart_array[0][5] = 6 # VS Dealer 6
chart_array[0][6] = 7 # VS Dealer 7
chart_array[0][7] = 8 # VS Dealer 8
chart_array[0][8] = 9 # VS Dealer 9
chart_array[0][9] = 10 # VS Dealer 10
chart_array[0][10] = 'A' # VS Dealer Ace

### PLAYER SPLIT CARDS ###

chart_array[1][0] = 'A,A' # Player Ace Split
chart_array[2][0] = '10,10' # Player 10 Split
chart_array[3][0] = '9,9' # Player 9 Split
chart_array[4][0] = '8,8' # Player 8 Split
chart_array[5][0] = '7,7' # Player 7 Split
chart_array[6][0] = '6,6' # Player 6 Split
chart_array[7][0] = '5,5' # Player 5 Split
chart_array[8][0] = '4,4' # Player 4 Split
chart_array[9][0] = '3,3' # Player 3 Split
chart_array[10][0] = '2,2' # Player 2 Split

# Always Split Aces
for col in range(1, 11):
    chart_array[1][col] = 'Y'

# Never Split 10's:
for col in range(1, 11):
    chart_array[2][col] = 'N'

# Split 9's 2 through 9 except for 7
for col in range(1, 11):
    chart_array[3][col] = 'Y'
chart_array[3][6] = 'N'
chart_array[3][9] = 'N'
chart_array[3][10] = 'N'

# Always Split 8's
for col in range(1, 11):
    chart_array[4][col] = 'Y'

# Split 7's 2 through 7
for col in range(1, 7):
    chart_array[5][col] = 'Y'
for col in range(7, 11):
    chart_array[5][col] = 'N'

# Split 6's 2 through 6
for col in range(1, 6):
    chart_array[6][col] = 'Y'
for col in range(6, 11):
    chart_array[6][col] = 'N'

# Never Split 5's
for col in range(1, 11):
    chart_array[7][col] = 'N'

# Split 4's against 5 and 6
for col in range(1, 11):
    chart_array[8][col] = 'N'
chart_array[8][4] = 'Y'
chart_array[8][5] = 'Y'

# Split 3's and 2's against 2 through 7
for col in range(1, 7):
    chart_array[9][col] = 'Y'
    chart_array[10][col] = 'Y'
for col in range(7, columns):
    chart_array[9][col] = 'N'
    chart_array[10][col] = 'N'

### PLAYER SOFT CARDS ###

chart_array[11][0] = 'A,9'
chart_array[12][0] = 'A,8'
chart_array[13][0] = 'A,7'
chart_array[14][0] = 'A,6'
chart_array[15][0] = 'A,5'
chart_array[16][0] = 'A,4'
chart_array[17][0] = 'A,3'
chart_array[18][0] = 'A,2'

# Always Stand on A,9
for col in range(1, 11):
    chart_array[11][col] = 'S'

# A,8 Double or stand on 6, stand on rest
for col in range(1, 11):
    chart_array[12][col] = 'S'
chart_array[12][5] = 'Ds'

# A,7 Double or stand on 2-6, Stand on 7-8, Hit on 9-A
for col in range(1, 6):
    chart_array[13][col] = 'Ds'
for col in range(6, 8):
    chart_array[13][col] = 'S'
for col in range(8, 11):
    chart_array[13][col] = 'H'

# A,6 Double or Hit on 3-6, Hit on rest
for col in range(1, 11):
    chart_array[14][col] = 'H'
for col in range(2, 6):
    chart_array[14][col] = 'Dh'

# A,5 and A,4 Double or Hit on 4-6, Hit on rest
for col in range(1, 11):
    chart_array[15][col] = 'H'
    chart_array[16][col] = 'H'
for col in range(3, 6):
    chart_array[15][col] = 'Dh'
    chart_array[16][col] = 'Dh'

# A,3 and A,2 Double or Hit on 5-6, Hit on rest
for col in range(1, 11):
    chart_array[17][col] = 'H'
    chart_array[18][col] = 'H'
for col in range(4, 6):
    chart_array[17][col] = 'Dh'
    chart_array[18][col] = 'Dh'

### PLAYER HARD TOTALS ###

chart_array[19][0] = '17'
chart_array[20][0] = '16'
chart_array[21][0] = '15'
chart_array[22][0] = '14'
chart_array[23][0] = '13'
chart_array[24][0] = '12'
chart_array[25][0] = '11'
chart_array[26][0] = '10'
chart_array[27][0] = '9'
chart_array[28][0] = '8'

# Always Stand on 17
for col in range(1, 11):
    chart_array[19][col] = 'S'

# 16 - 13 Stand on 2 - 6, Hit on 7 - A
for col in range(1, 6):
    for row in range(20, 24):
        chart_array[row][col] = 'S'
for col in range(6, 11):
    for row in range(20, 24):
        chart_array[row][col] = 'H'

# 12 Stand on 4 - 6, Hit the rest
for col in range(1, 11):
    chart_array[24][col] = 'H'
for col in range(3, 6):
    chart_array[24][col] = 'S'

# 11 always Double Down or Hit
for col in range(1, 11):
    chart_array[25][col] = 'Dh'

# 10 Double Down 2-9, otherwise Hit
for col in range(1, 9):
    chart_array[26][col] = 'Dh'
for col in range(9, 11):
    chart_array[26][col] = 'H'

# 9 Double down 3-6, otherwise hit
for col in range(2, 6):
    chart_array[27][col] = 'Dh'
for col in range(6, 11):
    chart_array[27][col] = 'H'
chart_array[27][1] = 'H'

# 8 and below always Hit
for col in range(1, 11):
    chart_array[28][col] = 'H'

# for row in chart_array:
#    print(row)