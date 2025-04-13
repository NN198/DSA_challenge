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
# set the parameters for the search method 
def search(root, x): 
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

if __name__ == "__main__":
    sorted_array = [4, 8, 10, 12, 14, 20, 22]
    root = sorted_array_to_bst(sorted_array, 0, len(sorted_array) - 1)

    x = 12
    print(search(root, x))  # True

    print(search(root, 99)) 

        