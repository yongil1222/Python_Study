mat_a = [[1,1,2],[2,1,1]]
mat_b = [[1,1],[2,1],[1,3]]

result = [[sum(a*b for a,b in zip(row_a, col_b)) for col_b in zip(*mat_b)] for row_a in mat_a]

for row_a in mat_a:
    print(row_a, type(row_a))

for col_b in zip(*mat_b):
    print(col_b,type(col_b))

print(result)