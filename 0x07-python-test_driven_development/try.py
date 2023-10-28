matrix = [[1, 2], [1]]
div = 2
sub_matrix  = []
new_matrix = []
for list in matrix:
    for i in range(0, len(list)):
        num = round((list[i] / div), 2)
        sub_matrix.insert(i, num)
    new_matrix.append(sub_matrix[:])
print(new_matrix)
print (matrix)

