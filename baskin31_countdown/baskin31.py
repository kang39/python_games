def valid_raise(number):
    if number >= 1 and number <= 3:
        return True
    else:
        return False

def ai_decide(current_num, previous_num):
    winning_num = [6, 10, 14, 18, 22, 26, 30]
    possible_moves = [1, 2, 3]
    possible_moves.remove(previous_num)
    for move in possible_moves:
        if current_num + move in winning_num:
            return move
    if current_num == 28:
        return min(possible_moves)
    else:
        return max(possible_moves)
    
print("*" * 72)
print("Rule: Range from 1 to 31, and whoever says the last number 31 loses.")
print("A player can raise a number only by 1 to 3.")
print("A player can't raise a same number as previous turn.")
print("For instance, if an opponent raise the number by 2, \nthe player should increase the number other than 2.")
print("*" * 30, "GAME START", "*" * 30)
print()

print("Starting From Computer: 1, 2 \tIncrement of 2\n")

current_num = 2
computer_choice = 2
player_choice = 0

while current_num < 31:
##PLAYER PART
    while True:
        player_raise = int(input("Player's Turn. \nEnter a number in between 1 and 3: "))
        if valid_raise(player_raise):
            if player_raise == computer_choice:
                print("A player can't raise a same number as previous turn with computer's.\n")
            else:
                player_choice = player_raise
                current_num += player_raise
                
                if current_num < 31:
                    num_list = [str(i) for i in range(current_num - player_raise + 1, current_num + 1)]
                    num_list_text = ", ".join(num_list)
                    print("Player's Decision:", num_list_text, "\tIncrement of", player_raise, "\n")
                    break

                else:
                    print("BUSTED! YOU LOSE!!!\n")
                    break
        else:
            print("INVALID INPUT!\n")

    if current_num < 31:
        ##COMPUTER PART
        computer_choice = ai_decide(current_num, player_choice)
        current_num += computer_choice

        print("Computer's Turn.")
        if current_num < 31:                
            num_list = [str(i) for i in range(current_num - computer_choice + 1, current_num + 1)]
            num_list_text = ", ".join(num_list)
            print("Computer's Decision:", num_list_text, "\tIncrement of", computer_choice, "\n")

        else:
            print("BUSTED! YOU LOSE!!!\n")
            break
