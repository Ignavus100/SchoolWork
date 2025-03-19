tree = {
    "Rose": ("Jasmine", "Trevor", None),
    "Jasmine": ("George", "Naomi", "Rose"),
    "George": (None, None, "Jasmine"),
    "Naomi": (None, None, "Jasmine"),
    "Trevor": ("Stanley", None, "Rose"),
    "Stanley": (None, None, "Trevor")
}

def preOrder(tree, CurrentNode, visited):
    if CurrentNode is None or CurrentNode in visited:
        return
    visited.append(CurrentNode)
    preOrder(tree, tree[CurrentNode][0], visited)
    preOrder(tree, tree[CurrentNode][1], visited)

def inOrder(tree, CurrentNode, visited):
    if CurrentNode is None or CurrentNode in visited:
        return
    inOrder(tree, tree[CurrentNode][0], visited)
    visited.append(CurrentNode)
    inOrder(tree, tree[CurrentNode][1], visited)

def postOrder(tree, CurrentNode, visited):
    if CurrentNode is None or CurrentNode in visited:
        return
    postOrder(tree, tree[CurrentNode][0], visited)
    postOrder(tree, tree[CurrentNode][1], visited)
    visited.append(CurrentNode)

pre_result = []
in_result = []
post_result = []

preOrder(tree, "Rose", pre_result)
inOrder(tree, "Rose", in_result)
postOrder(tree, "Rose", post_result)

print("Preorder:", pre_result)
print("Inorder:", in_result)
print("Postorder:", post_result)