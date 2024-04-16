# Given sets
set1 = {1, 3, 5, 7, 9}
set2 = {1, 2, 3, 4, 5}

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference (set1 - set2)
difference_set1 = set1.difference(set2)
print("Difference (set1 - set2):", difference_set1)

# Difference (set2 - set1)
difference_set2 = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2)

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)
