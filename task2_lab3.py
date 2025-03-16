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
            eval = minimax_algo(child, depth-1, alpha, beta, False,maxV,minV)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax_algo(child, depth-1, alpha, beta, True,maxV,minV)
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

