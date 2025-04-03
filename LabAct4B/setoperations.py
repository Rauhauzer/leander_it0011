# Define sets A, B, and C based on the Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'i', 'j', 'k'}

# a. Number of elements in A and B (Union of A and B)
print("a.", len(A | B))  # A union B

# b. Number of elements in B that are not in A and C
print("b.", len(B - (A | C)))  # B minus (A union C)

# c. Set operations for specific outputs

# i. {h, i, j, k}
result_i = (C - A) | {'h'}
print("c.i", result_i)

# ii. {c, d, f}
result_ii = A & C  # Intersection of A and C
print("c.ii", result_ii)

# iii. {b, c, h}
result_iii = (A & B) | {'h'}
print("c.iii", result_iii)

# iv. {d, f}
result_iv = (A & C) - B
print("c.iv", result_iv)

# v. {c}
result_v = A & B & C  # Common in all three sets
print("c.v", result_v)

# vi. {l, m, o}
result_vi = B - (A | C)  # Elements unique to B
print("c.vi", result_vi)
