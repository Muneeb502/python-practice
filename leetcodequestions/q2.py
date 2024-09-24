"""
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.


Example:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
"""
# Define the input lists
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# Combine both lists
combined_list = list1 + list2

# Sort the combined list
sorted_list = sorted(combined_list)

# Print the sorted list
print(sorted_list)