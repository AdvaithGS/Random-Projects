playerA = input('Name of Player A>> ')
playerB = input('Name of Player B>> ')
key = 'X'  
values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def check(l):
    if l[0] == l[1] and l[1] == l[2] and l[0] != ' ':
        return True
    if l[3] == l[4] and l[4] == l[5] and l[3] != ' ':
        return True
    if l[6] == l[7] and l[7] == l[8] and l[6] != ' ':
        return True
    if l[0] == l[3] and l[3] == l[6] and l[0] != ' ':
        return True
    if l[1] == l[4] and l[4] == l[7] and l[1] != ' ':
        return True
    if l[2] == l[5] and l[5] == l[8] and l[2] != ' ':
        return True
    if l[0] == l[4] and l[4] == l[8] and l[0] != ' ':
        return True
    if l[2] == l[4] and l[4] == l[6] and l[2] != ' ':
        return True
    if l[0] != ' ' and l[2] != ' ' and l[3] != ' ' and l[4] != ' ' and l[5] != ' ' and l[6] != ' ' and l[7] != ' ' and l[8] != ' ' and l[1] != ' ' :
        return 'N'


# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

print_tic_tac_toe(values)         
def run():
    for i in [1,2] :
        def run2(i):    
            global key
            global values
            if i == 1:
                target = input('{}, what is your move? '.format(playerA))
            if i == 2:
                target = input('{}, what is your move? '.format(playerB))
            if not target.isdigit() or int(target) > 9:
                if i == 1:
                    print('Please choose a valid number between 1 and 9')
                    run()
                if i == 2:
                    print('Please choose a valid number between 1 and 9')
                    run2(2)
            if values[int(target)-1] == ' ':
                values[int(target)-1] = key
                if check(values) == 'N':
                    print_tic_tac_toe(values)
                    print('Game Over, It\'s a tie.')
                    exit()
            else:
                if i == 1:
                    print('Please choose a box that is empty')
                    run()
                if i == 2:
                    print('Please choose a box that is empty')
                    run2(2)
            if check(values):
                if i == 1:
                    player = playerA
                else:
                    player = playerB
                print_tic_tac_toe(values)
                print('Game Over, {} wins. Congratulations!!'.format(player))
                exit()
            
            if i == 1:
                key = 'O'
            if i == 2:
                key = 'X'
            print_tic_tac_toe(values)
        run2(i)
    run()

run()
