# no imports beyond numpy should be used in answering this question
import numpy as np

###############################################################
# TASK 1 Code
# Implement:
# - getChildren
# - getData
# - getID
# - buildTree
###############################################################

### BEGIN YOUR CODE ###
# Feel free to add any code here that may help you to define 
# your tree data structure.

# class Tree():
#     def __init__(self, root, children, data, ID):
#         self.root = root
#         self.children = []
#         self.data = data
#         self.ID = ID 
#     def addNode(self,obj):
#         self.children.append(obj)
class Node():
    def __init__(self, data, ID, children):
        self.data = data
        self.ID = ID
        self.children = children


### END YOUR CODE ###


def getChildren(tree):
    """
    Return a list of children. The list should be either an empty
    list, [], or a list of three tree data stuctures. If the list
    is not empty the three children in the list should be in order.
    See child index information in buildTree for details.
    
    Input:
    tree: an instance of a tree using your chosen data structure

    Return:
    List. Either an empty list or [child0_tree, child1_tree, child2_tree].
    """
    ### BEGIN YOUR CODE ###
    return tree.children
    ### END YOUR CODE ###

def getData(tree):
    """
    Return the Numpy data associated with just the root node in tree    

    Input:
    tree: an instance of a tree using your chosen data structure

    Return:
    NumPy array with shape (N, M) where N is the number of points
        in the data and M is the dimension of a point. N may be 
        zero, so the returned data may be an empty NumPy array 
        with shape (0, M).
    """
    ### BEGIN YOUR CODE ###
    return tree.data 

    ### END YOUR CODE ###
    

def getID(tree):
    """
    Return the integer ID of the root node of the tree.    

    Input:
    tree: an instance of a tree using your chosen data structure

    Return:
    integer
    """
    ### BEGIN YOUR CODE ###
    return tree.ID
    ### END YOUR CODE ###

def buildTree(data, split_list, root_id):
    """
    Build a tree using any tree data structure that you choose.

    The root node of this (sub) tree should store all of data.

    If the data is empty or the split_list is empty,
    len(data) == 0 or len(split_list) == 0,
    the this root node will have no children and it should still 
    store the id and the data (even though it is empty).

    If the data is not empty and the split_list is not empty,
    the root node of this (sub) tree should have three children.
    The children should all be tree stuctures (just like the root).
    The three children should each be given a subset of data.

    Let s = split_list[0], the first integer in split_list.
    Child index 0:
        Should contain a NumPy array with shape (N_0, M)
        that containing all points in data where data[i,s] < -1.
        N_0 is the number of points that fit this criteria.
        If N_0 is zero, this child should store an empty NumPy array
        with shape (0, M), e.g. np.zeros((0,M)).
        This child should have id = root_id*10
    Child index 1:
        The same as child index 0 except:
        Child data is -1 <= data[i,s] <= 1
        Child id = root_id*10 + 1        
    Child index 2:
        The same as child index 2 except:
        Child data is data[i,s] > 1
        Child id = root_id*10 + 2        

    The tree should continue growing where the children split their 
    data based on split_list[1] and the grandchildren split their data
    based on split_list[2] and so on.

    Input:
    data: NumPy ndarray shape (N, M) representing the M-dimensional 
        coordinates of N data points. The data may be an empty NumPy
        array, i.e. len(data) == 0.
    split_index_order: List of integers. Each integer in the list is
        in the range [0,M). The list will have at most M entries.
        The list may be empty, [], in which case, this tree will not
        have any children.
    root_id: Positive integer representing the ID for the root of this
        (sub) tree. The ID for the root any child subtrees should be
        root_id*10 + index_of_that_child. So if the root_id is 7 and 
        there are three children, the IDs of the children should be
        70, 71, 72.

    Return:
    A data structure of your choosing that represents the resulting
        tree.
    """
    ### BEGIN YOUR CODE ###
    if len(data) == 0 or len(split_list) == 0:
        return Node(data,root_id,[])
    else:
        split_index = split_list[0]
        data0 = data[data[:,split_index] < -1]
        data1 = data[(data[:,split_index] >= -1) & (data[:,split_index] <= 1)]
        data2 = data[data[:,split_index] > 1]
        
        root_id0 = root_id*10
        root_id1 = root_id*10 + 1
        root_id2 = root_id*10 + 2
        
        child0 = buildTree(data0, split_list[1:], root_id0)
        child1 = buildTree(data1, split_list[1:], root_id1)
        child2 = buildTree(data2, split_list[1:], root_id2)
       
        return Node(data, root_id, [child0, child1, child2])
        
    ### END YOUR CODE ###


# Helps the autograder keep track of what nodes have been printed
# via printNode. You shouldn't ever modify this. It only gets
# updated inside printNode()
PRINT_NODE_LIST = []

def printNode(tree):
    """
    Print information about the just the root node of tree.
    Prints:
    id
    data

    Input:
    tree: an instance of a tree using your chosen data structure

    Return:
    None
    """
    print(getID(tree))
    print(getData(tree))

    # Helps the autograder keep track of what nodes have been printed
    # via printNode. You shouldn't ever modify this. It only gets
    # updated inside printNode()
    PRINT_NODE_LIST.append(getID(tree))


###############################################################
# TASK 2 Code
# Implement:
# - printTreeBF
# - printTreeDF
###############################################################

def printTreeBF(tree):
    """
    Print each node in the whole tree using a breadth-first 
    traversal. To make the autograder happy, print the parent
    before the children and make sure any children are printed 
    in increasing order of their index, i.e., index0, then 
    index1, then index2.

    Autograder details: Use printNode for each node (id then data)
    Don't print another information, and don't print any blank lines.

    Input:
    tree: an instance of a tree using your chosen data structure

    Return:
    None
    """
    ### BEGIN YOUR CODE ###
    

    ### END YOUR CODE ###

def printTreeDF(tree):
    """
    Print each node in the whole tree using a depth-first 
    traversal. To make the autograder happy, print the parent
    before the children and make sure any children are printed 
    in increasing order of their index, i.e., index0, then 
    index1, then index2.

    Autograder details: Use printNode for each node (id then data)
    Don't print another information, and don't print any blank lines.

    Input:
    tree: an instance of a tree using your chosen data structure

    Return:
    None
    """
    ### BEGIN YOUR CODE ###
    if len(getChildren(tree)) == 0:
        printNode(tree)
        
    else:
        printNode(tree)
        
        for child in getChildren(tree):         
            printTreeDF(child)
    
    ### END YOUR CODE ###

###############################################################
# Test code. Feel free to add more test to help get your code 
# working.
###############################################################

def task1_test0():
    data0 = np.zeros((0,3))

    tree0 = buildTree(data0, [0, 1, 2], 5)
    print("tree0 root")
    printNode(tree0)
    print() # Print blank line

def task1_testA(data):
    tree1A = buildTree(data, [], 6)
    print("tree1A root")
    printNode(tree1A)
    print() # Print blank line

def task1_testB(data):
    tree1B = buildTree(data, [0], 1)
    print("tree1B root")
    printNode(tree1B)
    print("tree1B children")
    for child in getChildren(tree1B):
        printNode(child)
    print() # Print blank line

def task1_testC(data):
    tree1C = buildTree(data, [0, 1, 2], 1)
    print("tree1C root")
    printNode(tree1C)

    tree1C_firstChild = getChildren(tree1C)[0]
    print("tree1C first child")
    printNode(tree1C_firstChild)

    tree1C_firstGrandchild = getChildren(tree1C_firstChild)[0]
    print("tree1C first grandchild")
    printNode(tree1C_firstGrandchild)

    print() # Print blank line



def task2_testBF(data):
    tree1D = buildTree(data, [2, 0, 1], 1)

    print("tree BF")
    printTreeBF(tree1D)
    print("Order of printed nodes:", PRINT_NODE_LIST)
    print() # Print blank line

def task2_testDF(data):
    tree1D = buildTree(data, [2, 0, 1], 1)

    print("tree1D DF")
    printTreeDF(tree1D)
    print("Order of printed nodes:", PRINT_NODE_LIST)
    print() # Print blank line

def test_randData():
    N = 40
    M = 5
    depth = 4

    data = np.random.uniform(-2, 2, (N,M))
    split_list = np.random.choice(M, size=depth, replace=False).tolist()

    tree = buildTree(data, split_list, 1)

    print("random data tree BF")
    printTreeBF(tree)
    print("Order of printed nodes:", PRINT_NODE_LIST)
    print() # Print blank line

if __name__ == '__main__':
    
    data1 = np.array([
        [-1.5, -0.5, -0.2],
        [0.3, 1.3, 0.0],
        [-1.3, -1.4, -2.1],
        [0.9, 1.5, -0.6]])

      
             
                     
                      
    task1_test0()
    task1_testA(data1)
    task1_testB(data1)
    task1_testC(data1)

    #PRINT_NODE_LIST = [] # Reset list before printing tree
    #task2_testBF(data1)

    PRINT_NODE_LIST = [] # Reset list before printing tree
    task2_testDF(data1)

    PRINT_NODE_LIST = [] # Reset list before printing tree
    test_randData()
