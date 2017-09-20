import random

# Question 1
# Given two strings s and t, determine whether some anagram of t is a
# substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a
# boolean True or False.


def question1(s, t):
    if len(s) < len(t):
        return False

    temp = t

    # Iterate through s
    for character in s:
        if character in t:
            # If character is in s and t, mark out that character
            temp = temp.replace(character, "", 1)
            # Anagram has been found, with all characters in t, marked out
            if len(temp) == 0:
                return True
        else:
            temp = t
    return False

print "Question 1 Test Cases"
print question1('hello', 'loh')
# False
print question1('udacity', 'ad')
# True
print question1('udacity', 'aduaca')
# False


# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.


def longestPalindrome(str):
    # Return
    largestPal = ""

    # Iterate through length of input
    for x in range(len(str)):
        workingStr = str[x:]
        end = len(workingStr)

        # loop through creating smaller substrings of the working string
        while end != 0:
            # reverse of the working string
            reverse = workingStr[-1:-1-len(workingStr)-1:-1]

            if workingStr == reverse:
                if (len(workingStr)) > len(largestPal):
                    largestPal = workingStr
            end -= 1
            workingStr = workingStr[:end]


    if len(largestPal) == 0 or len(largestPal) == 1:
        return None
    else:
        return largestPal

print "Question 2 Test Case"

print longestPalindrome("bbbbbbbbbbbbbbrracecarxxxxxxxxxxxxxxxxxxxx")
# xxxxxxxxxxxxxxxxxxxx
print longestPalindrome("sdaasdfracecarbbb")
# racecar
print longestPalindrome("abracadabra")
# aca
print longestPalindrome("bbasdraceecarasdfa")
# racecar
print longestPalindrome("abcdefghijklmnopqrstuvwxyz")
# None

# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return an
# adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)


def question3(G):
    min_spanning_tree = {}
    visted_vertices = []
    # Initialize minimum spanning tree with vertices from G
    for i, vertex in enumerate(G):
        min_spanning_tree[vertex] = []

    # Choose a random vertex to begin
    start_vertex = random.choice(G.keys())
    visted_vertices.append(start_vertex)

    # Iterate through graph until all vertices are visted
    prev_e = None
    while len(visted_vertices) < len(G):
        for vertex in visted_vertices:
            for edge in G[vertex]:
                # iterate through edge list for a vertex
                # selects edge that has the lowest weight
                if not prev_e or edge[1] < prev_e[1]:
                    if edge[0] not in visted_vertices:
                        prev_e = edge
                        to_vertex = edge[0]
                        from_vertex = vertex
                        edge_weight = edge[1]


        # store selected lowest weight edge visted list
        # store lowest weight edge into tree and visit node
        visted_vertices.append(to_vertex)
        min_spanning_tree[from_vertex].append((to_vertex, edge_weight))
        min_spanning_tree[to_vertex].append((from_vertex, edge_weight))

        # since next vertex is stored in visited list, reset variables
        prev_e = None
        edge = None
        to_vertex = None
        from_vertex = None


    return min_spanning_tree




print "Question 3 Test Cases"
print question3({'A': [('B', 2)],
                'B': [('A', 2), ('C', 5), ('D', 3)],
                'C': [('B', 5), ('E', 6)],
                'D': [('B', 3), ('E', 1)],
                'E': [('D', 1), ('C', 6)]
            })

# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5), ('D', 3)],
#  'C': [('B', 5)],
#  'D': [('B', 3), ('E', 1)],
#  'E': [('D', 1)]
# }

print question3({'A': [('B', 6)],
                'B': [('A', 2), ('C', 1)],
                'C': [('B', 1), ('D', 1)],
                'D': [('A', 1), ('C', 1)]
            })

 # {'A': [('D',1)],
#   'B': [('C', 1)],
#   'C': [('B', 1), ('D', 1)],
#   'D': [('A', 1), ('C', 1)]
# }
print question3({'A': [('C', 6), ('D', 6), ('E', 1)],
                 'B': [('C', 6), ('D', 6), ('E', 1)],
                 'C': [('A', 6), ('B', 6), ('E', 1)],
                 'D': [('A', 6), ('B', 6), ('E', 1)],
                 'E': [('A', 1), ('B', 1), ('C', 1), ('D', 1)]
            })

 # {'A': [('E',1)],
#   'B': [('E', 1)],
#   'C': [('E', 1)],
#   'D': [('E', 1)],
#   'E': [('A', 1), ('B', 1), ('C', 1), ('D', 1)]
# }

# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
#For example, the root is a common ancestor of all nodes on the tree, but if both nodes are
# descendents of the root's left child, then that left child might be the lowest common ancestor.
# You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2), where T is the tree represented
# as a matrix, where the index of the list is equal to the integer stored in that node and a 1
# represents a child node, r is a non-negative integer representing the root, and n1 and n2
# are non-negative integers representing the two nodes in no particular order. For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

def question4(T, r, n1, n2):


    def search(r, node):
        """ A subfunction to find a path from root to node"""

        # Initialize variables and pointers
        current_node = r
        path = []
        isFound = False
        path.append(r)
        prev_node = None

        while current_node != prev_node:
            if  node == current_node:
                isFound = True
                break

            # Check if node is to the left in BST
            # Find next child
            if node < current_node:
                prev_node = current_node
                for child in range(0, current_node):
                    if T[current_node][child] == 1:
                        current_node = child
                        path.append(child)
                        break

            # Check if node is to the right in BST
            if node > current_node:
                prev_node = current_node
                for child in range(node, len(T)):
                    if T[current_node][child] == 1:
                        current_node = child
                        path.append(child)
                        break
        if isFound:
            return path
        else:
            return None

    path1 = search(r, n1)
    path2 = search(r, n2)


    # default ancestor as root
    foundAncestor = r

    for i1 in range(len(path1) - 1, 0, -1):
        for i2 in range(len(path2) - 1, 0, -1):

            # iterate through n1 path and compare against n2 path
            #  to find least common ancestor
            if (path1[i1] == path2[i2]):
                foundAncestor = path1[i1]
                break

    return foundAncestor

print "Question 4 Test Case"
print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4
            )
# 3
print question4([[0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0]],
                4,
                0,
                3
            )
# 1

print question4( [[0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0]],
                4,
                0,
                3
            )
#2

# Question 5
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end
# is the 3rd element. The function definition should look like
# question5(ll, m), where ll is the first node of a linked list and m is
# the "mth number from the end". You should copy/paste the Node class below
# to use as a representation of a node in the linked list. Return the value
# of the node at that position.
#

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


def question5(ll, m):
    head_pointer = ll
    while m > 0:
        if head_pointer == None:
            return None
        head_pointer = head_pointer.next
        m -= 1

    tail_pointer = ll
    while head_pointer != None:
        head_pointer = head_pointer.next
        tail_pointer = tail_pointer.next
    return tail_pointer.data


print "Question 5 Test Cases"

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six

print question5(one, 3)
# 4
print question5(one, 6)
# 1
print question5(one, 7)
# None
