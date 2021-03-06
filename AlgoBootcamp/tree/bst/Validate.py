from AlgoBootcamp.tree.bst.BinarySearchTree import Node

def validate(node, down_constrain = float("-inf"), top_constrain = float("inf")):
    if node.data <= down_constrain or node.data >= top_constrain:
        return False
    elif node.left is None and node.right is None:
        return True

    if node.left and not validate(node.left, down_constrain, node.data):
        return False
    if node.right and not validate(node.right, node.data, top_constrain):
        return False

    return True


node = Node(10)
node.insert(20)
node.insert(30)
node.insert(5)
node.insert(1)
assert validate(node) == True

node = Node(10)
assert validate(node) == True

node = Node(10)
node.left = Node(20)
assert validate(node) == False

node = Node(10)
node.right = Node(-1)
assert validate(node) == False

node = Node(10)
node.insert(20)
node.insert(30)
node.insert(5)
node.insert(1)
node.left.left.data = 100
assert validate(node) == False

node = Node(2)
node.right = Node(2)
node.left = Node(2)
assert validate(node) == False