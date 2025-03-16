import math,random



def strength(x):
    return math.log(x + 1,2) + (x / 10)

def utility(mx, mn):
    i = random.choice([0, 1])
    return strength(mx) - strength(mn) + ((-1) ** i) * random.randint(1, 10) / 10

def minimax(depth, flag, alpha, beta, mx, mn):
    if depth == 5:
        return utility(mx, mn)
    
    if flag:
        max_val = -math.inf
        for i in range(2):
            val = minimax(depth + 1, False, alpha, beta, mx, mn)
            max_val = max(max_val, val)
            alpha = max(alpha, val)
            if  alpha >= beta:
                break 
        return max_val
    else:
        min_val = math.inf
        for i in range(2):
            val = minimax(depth + 1, True, alpha, beta, mx, mn)
            min_val = min(min_val, val)
            beta = min(beta, val)
            if alpha >= beta:
                break
        return min_val

# def play_game(starting_player, mx, mn):
#     result = minimax(0, True, -math.inf, math.inf, mx, mn)
#     return result

# def main():
#     starting_player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
#     carlsen_strength = int(input("Enter base strength for Carlsen: "))
#     caruana_strength = int(input("Enter base strength for Caruana: "))
    
#     results = []
#     for game in range(4):
#         if (starting_player + game) % 2 == 0:
#             mx, mn = carlsen_strength, caruana_strength
#             winner = "Carlsen"
#         else:
#             mx, mn = caruana_strength, carlsen_strength
#             winner = "Caruana"
        
#         result = play_game(starting_player, mx, mn)
#         results.append(result)
        
#         if result > 0:
#             print(f"Game {game + 1}: {winner} wins")
#         elif result < 0:
#             print(f"Game {game + 1}: {('Carlsen' if winner == 'Caruana' else 'Caruana')} wins")
#         else:
#             print(f"Game {game + 1}: Draw")
    
#     # Determine overall winner
#     carlsen_wins = sum(1 for r in results if r > 0)
#     caruana_wins = sum(1 for r in results if r < 0)
    
#     if carlsen_wins > caruana_wins:
#         print("Overall Winner: Carlsen")
#     elif carlsen_wins < caruana_wins:
#         print("Overall Winner: Caruana")
#     else:
#         print("Overall Result: Draw")

# if __name__ == "__main__":
#     main()

player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
carlsen_strength = int(input("Enter base strength for Carlsen: "))
caruana_strength = int(input("Enter base strength for Caruana: "))
carlsen_score = 0
caruana_score = 0
for i in range(4):
    if(player == 0):
        player = 1
        if minimax(0,True,-math.inf,math.inf,carlsen_strength,caruana_strength)>=0:
            carlsen_score+=1
        else:
            caruana_score += 1
    else:
        player = 0
        if minimax(0,True,-math.inf,math.inf,carlsen_strength,caruana_strength)>=0:
            caruana_score+=1
        else:
            carlsen_score += 1
print("Overall Results:")
print("Magnus Carlsen Wins:",carlsen_score)
print("Fabiano Caruana Wins: ",caruana_score)
print("Draws:", 0)
print()
if carlsen_score>caruana_score:
    print("Overall winner : Magnus Carlsen")
elif caruana_score>caruana_score:
    print("Overall Winner : Fabiano Caruana")
else:
    print("Overall Winner : Draw")