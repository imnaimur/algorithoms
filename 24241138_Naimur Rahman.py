import random,math

class Node:
    def __init__(self,value,children=None):
        self.value = value
        self.children = children if children is not None else []

def strength(x):
    return math.log2(x+1)+(x/10)

def utility(maxv,minv):
    i = random.choice([0,1])
    return strength(maxv) - strength(minv) + ((-1)**i) *(random.randint(1,10)/10)


def minimax_algo(node, depth, alpha, beta, maximizing_player,maxV,minV):
    if depth == 0 :
        return utility(maxV,minV)
    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax_algo(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax_algo(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def create_tree(depth):
    if depth == 0:
        return Node(0)
    
    left_child = create_tree(depth - 1)
    right_child = create_tree(depth - 1)
    return Node(0, [left_child, right_child])


#--------------------- Game 1-------------------------- #


player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
carlsen_strength = int(input("Enter base strength for Carlsen: "))
caruana_strength = int(input("Enter base strength for Caruana: "))
carlsen_score = 0
caruana_score = 0
for i in range(4):
    parent = create_tree(5)

    if(player == 0):
        player = 1
        val = minimax_algo(parent,0,-math.inf,math.inf,True,carlsen_strength,caruana_strength)
        if val>0:
            carlsen_score+=1
            print(f"Game {i+1} Winner: Magnus Carlsen (Max) (Utility value: {round(val, 2)})")

        elif val<0:
            print(f"Game {i+1} Winner: Fabiano Caruana (Min) (Utility value: {round(val, 2)})")
            caruana_score += 1
        else:
            print(f"Game {i+1} Result: Draw (Utility value: {round(val, 2)})")

    else:
        player = 0
        val = minimax_algo(parent,0,-math.inf,math.inf,True,caruana_strength,carlsen_strength)
        if val >0:
            caruana_score+=1
            print(f"Game {i+1} Winner: Fabiano Caruana (Max) (Utility value: {round(val, 2)})")

        elif val<0: 
            carlsen_score += 1
            print(f"Game {i+1} Winner: Magnus Carlsen (Min) (Utility value: {round(val, 2)})")

        else:
            print(f"Game {i+1} Result: Draw (Utility value: {round(val, 2)})")






print("Overall Results:")
print("Magnus Carlsen Wins:",carlsen_score)
print("Fabiano Caruana Wins: ",caruana_score)
print("Draws:", 4-carlsen_score-caruana_score)
print()

if carlsen_score>caruana_score:
    print("Overall winner : Magnus Carlsen")
elif caruana_score>caruana_score:
    print("Overall Winner : Fabiano Caruana")
else:
    print("Overall Winner : Draw")


#--------------------- Game 2-------------------------- #





player = int(input("Enter starting player for game 1 (0 for Light, 1 for L): "))
cost = float(input("Enter the cost of using Mind Control: "))
light_strength = int(input("Enter base strength for Light: "))
l_strength = int(input("Enter base strength for L: "))


parent = create_tree(5)

if(player == 0):
    val = minimax_algo(parent,0,-math.inf,math.inf,True,light_strength,l_strength)
    magic = minimax_algo(parent, 3, -math.inf, math.inf, False, light_strength, l_strength)
    balanced = magic - cost

else:
    val = minimax_algo(parent,0,-math.inf,math.inf,True,l_strength,light_strength)
    magic = minimax_algo(parent,3,-math.inf,math.inf,False,l_strength,light_strength)
    balanced = magic - cost



print("Minimax value without Mind Control:", round(val,2))
print("Minimax value with Mind Control: ",round(magic,2))
print("Minimax value with Mind Control after incurring the cost: ", round(balanced,2))

if player == 0:
    player = "Light"
else:
    player = "L"

if val>0 and balanced > 0:
    print(f"{player} should NOT use Mind Control as the position is already winning.")
elif val>0 and balanced < 0:
    print(f"{player} should NOT use Mind Control as it backfires.")
elif val<0 and balanced < 0:
    print(f"{player} should NOT use Mind Control as the position is losing either way.")
else:
    print(f"{player} Light should use Mind Control.")



"""

Q1: In the first problem, will the stronger player always win? Does having the first move matter? First
come up with an answer through reasoning only. Then run the algorithm with several inputs and
see what happens.

Answer: No its not necessary that the first player will always win.Because there is an uncertainity because of the random value in the utility function.Having the first move matter because the first player can take the winning path first.

Q2: In the first problem, the utility function includes a random component. Do you think it is a wise
choice? Why or why not? How much can the random factor affect the outcomes?

Answer: Well, It is wise choice.Because the outcomes are uncertain which is similar to real world.The random factor affect quite a bit because it doesn't let us predict the exact outcomes

Q3: Consider the implications of increasing the game tree depth or changing the branching factor. How
would these changes affect the performance of the alpha-beta pruning algorithm and the accuracy
of the final outcome?

Answer:  We know the runtime is O(b^d) where b is branching factor and d is depth.so the runtime will increase and the performance will become slower.but the more state we have,we can predict the nearest result of the actual outcome mean high accuracy.

Q4: In minimax algorithms, is the first player always a maximizer? Can you think of any scenario where
it will not be the case?

Answer: If we we reverse the minimax algorithm then the first player could be a minimizer.In tic-tac-toe the first 


"""