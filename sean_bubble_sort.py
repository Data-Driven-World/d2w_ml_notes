

l = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1, 56, 56,69,4,24,1,4]
l1 = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1, 56, 56,69,4,24,1,4]
l2 = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1, 56, 56,69,4,24,1,4]



# ======================
# BUBBLE SORT
# ======================
"""
How does bubble sort work:
    Iterate through the list of l
    If number on left index > right => swap places
    By the end of the first iteration => biggest number flushed to the right

    Start with the first index again 
    Iterate to the last index - 1 (since last number already sorted)
"""
swap = True
bubble_counter = 1
while swap:
    swap = False
    for j in range(len(l) - bubble_counter):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                bubble_counter += 1
                swap = True

# print(l)
# print(bubble_counter)


while swap:
    swap = False
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            bubble_counter += 1
            swap = True

# print("#################")
# print(l)
# print(bubble_counter)


# ======================
# INSERTION SORT
# ======================
"""
How does insertion sort work

Comparing current iteration item to previously iterated items

If current iteration val < element to its left => swap 
iterate based on a counter which reflects the number of iterated items


"""


swap = True
c = 0
print(f"Original list: {l1}")
while swap:
    insertion_counter = 1
    swap = False
    for i in range(len(l1) - 1):
        for j in range(insertion_counter):
            if l1[i] < l1[i-insertion_counter]:
                l1[i-insertion_counter], l1[i] = l1[i], l1[i-insertion_counter]
                insertion_counter += 1
                swap = True
                c += 1
                print(f"Iteration {c} list: {l1}")

# print(f"Final list: {l1}")
# print(c)


# ======================
# SELECTION SORT
# ======================
"""
How does selection sort work

Rmb the current index
The current index is the minimum index

Iterate through all the elements to the right of the min index
If right index element < min index element:
    remember new index 
    at the end of the whole iteration => swap the places between the min index element and the new index element
"""

selection_counter = 0
finder_index = 0
found_index = 0
swap = True

while swap:
    swap = False
    for i in range(len(l2)-1): # first iteration is to iterate through the whole 
        for j in range():
            ...
        ...