#Iterative approach
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def sorted_array_to_bst(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = Node(arr[mid])

    node.left = sorted_array_to_bst(arr, start, mid - 1)
    node.right = sorted_array_to_bst(arr, mid + 1, end)

    return node
# ITERATIVE APPROACH
def iterative_search(root, x): 
    current_node = root

    #iterating through the loop with the intial condition
    while current_node  is not None: 
        if current_node.data == x:
            return True
        elif current_node.data < x:
            current_node = current_node.right
        else:
            current_node = current_node.left
    return False

#RECURSIVE APPROACH
def recursive_search(root, x):

    if root is None or root.data == x:
        return root
    if root.data < x:
        return recursive_search(root.right, x)
    
    return recursive_search(root.left, x)


if __name__ == "__main__":
    sorted_array = [4, 8, 10, 12, 14, 20, 22]
    root = sorted_array_to_bst(sorted_array, 0, len(sorted_array) - 1)

    x = 12
    print(iterative_search(root, x))  # True

    print(iterative_search(root, 99)) 
    
    x = 20
    print("True" if recursive_search(root, x) else "False")  # True

    print("True" if recursive_search(root, 73) else "False") 

        