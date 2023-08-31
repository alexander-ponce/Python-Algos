#iterative binary search

def binary_itr(arr, start, end , target):
    while start <= end:

        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return start

arr = [2, 5, 8, 10, 16, 22, 25]
target = 10

result = binary_itr(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print ("Element is present in array")




# Bubble Sort - Optimized vs. Unoptimized
#Optimized

def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range (len(A)-i-1):
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] =  A[j+1], A[j]
    return A, iterations

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_optimized(A))


#insertion sort - Shifting Elements
def insert_sort(A):
    for j in range (1, len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]> key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

A = [5, 2, 4, 6, 1, 3]
print(insert_sort(A))


#ADVANCED- LINKED LISTS:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False
    
    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

# family.traversal()
family.insert_new_header("Dave")
# print(family.search("Bob"))
family.delete_node("Bob")
# family.delete_node("Amy")
family.delete_tail()
family.traversal()

