def main():
    tic_tac_toe_defautl_values = ['1','2','3','4','5','6','7','8','9']
    print('X player will start')
    next_player = 'x'
    i = 0
    while i < 9:
        tic_tac_toe_grid(tic_tac_toe_defautl_values)
        position = input(f"Please enter the Possition for {next_player} : ")
        is_available = check_available_position(position,tic_tac_toe_defautl_values)
        if is_available == True:
            tic_tac_toe_defautl_values[int(position)-1] = next_player
            i +=1
        else:
            print('This is not a valid input')
            i -= -1
        next_player = check_next_player(next_player)


def check_next_player(next_player):
    if next_player.lower() == 'x':
        next_player = 'o'
    else:
        next_player = 'x'
    return next_player

def check_available_position(position, defaults):
    for i in range(9):
        if position == defaults[i]:
            available_position = True
            break
        else:
            available_position = False   
    return available_position

def tic_tac_toe_grid(defaults):
    print("\n")
    print("\t     |     |")
    print(f"\t   {defaults[0]} |   {defaults[1]} |  {defaults[2]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t   {defaults[3]} |   {defaults[4]} |  {defaults[5]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t   {defaults[6]} |   {defaults[7]} |  {defaults[8]}")
    print("\t     |     |")
    print("\n")






if __name__ == "__main__":
    main()