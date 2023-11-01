class Node():
    def __init__(self, state, open, close):
        self.state = state
        self.open = open
        self.close = close

n = 3
frontier = []
explored = []
answer = []
node = Node("(", 1, 0)
frontier.append(node)



while True:

    if len(frontier) == 0:
        break
    
    else:

        node = frontier.pop()
        

        
        if node.open == node.close and node.open < n and node.close < n:
            
            new_node = Node(f"{node.state}(", node.open+1, node.close)
            print("state: ", new_node.state)
            frontier.append(new_node)
            explored.append(node.state)
        

        elif node.open > node.close:
            
            if node.state not in explored:
                if node.open < n:
                    new_node = Node(f"{node.state}(", node.open+1, node.close)
                    print("state: ", new_node.state)
                    frontier.append(new_node)
                    if new_node.open == n and new_node.close == n:
                        answer.append(new_node.state)
                    

            else:
                if node.close < n:
                    new_node = Node(f"{node.state})", node.open, node.close+1)
                    print("state: ", new_node.state)
                    frontier.append(new_node)
                    if new_node.open == n and new_node.close == n:
                        answer.append(new_node.state)

            explored.append(node.state)

        else:
            print("state: ", new_node.state)
            explored.append(node.state)

print("\n\n\n\n\n\n", answer, "\n\n\n\n\n\n")
