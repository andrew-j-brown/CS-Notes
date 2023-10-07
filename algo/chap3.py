# Search algorithms look for data in a data set.
# A data set is a collection of data (shocking, right?)
#
# Linear search iterates through every element in a data set and compares it to the target.
# If the comparison finds a match, the element is in the list; the inverse is also true.
#
a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]

def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

print(linear_search(a_list, 91))

# A linear search's time complexity is O(n)
# Worst case scenario, it will take a step for every single
# item in the data set.
#
# Linear search is best used when looking through unsorted
# data.
#
# Python has built in linear search with the 'in' keyword

print(32 in a_list)
print('a' in 'apple')

# Binary search is another, faster algorithm for searching a sorted list (and only sorted).
#
# Binary search works by splitting a list into halves.

sorted_list = (10, 12, 13, 14, 15, 18, 19)

def binary_search(sorted_list, n):
    # The variables first and last keep track of the beginning and the end of the list
    # we are searching. Set first to zero as it is the first index of any list, and set
    # last to the length of the list minus one (due to lists being zero indexed).
    # These values will change as we divide the list into segments.
    first = 0
    last = len(sorted_list) - 1
    # Loop the algorithm as there are items in the list.
    while last >= first:
        # Locate the middle of the list by adding first and last, and dividing by two
        # // is a floor division operator. It always returns a whole value rounded down.
        # We use this as a list index must always be a whole number.
        mid = (first + last) // 2
        # Check to see if the middle of the list is the target item, if so return True.
        if sorted_list[mid] == n:
            return True
        else:
            # If the target is less than the midpoint, move the top of the segment down.
            if n < sorted_list[mid]:
                last = mid - 1
            # If else (target is more than midpoint), pull the bottom of the segment up.
            else:
                first = mid + 1
        # If we've made it here, the target is not in the list
    return False

print(binary_search(sorted_list, 96))
print(binary_search(sorted_list, 15))

# Binary search is much more efficient than linear search for finding a target in a large
# data set. So much so that sorting a data set and then searching within is more efficient
# than just doing a linear search.
#
# Python has a built in module for binary search by the way

from bisect import bisect_left

sorted_fruits = ['apple', 'banana', 'orange', 'plum']
print(bisect_left(sorted_fruits, 'banana'))

# bisect module sort returns the index of an item even if it's not in the data set. If the
# item is not present, it returns where it would be. Keep this in mind, and if returning
# false is necessary, a custom function will need to be made.
#
# This function is as simple as getting the index from bisect_left, and comparing it
# to the same index of the data set. If they match, then the item was found! If not,
# then the data set does not contain the item.

print(ord('a'))

# the above returns the binary ascii vaue for the character
# used when you need the underlying ascii codes
