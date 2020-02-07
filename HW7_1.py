class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        my = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for el in range(len(self.list_1)):

            for i in range(len(self.list_2[el])):
                my[el][i] = self.list_1[el][i] + self.list_2[el][i]

        return str('\n'.join(['\t'.join([str(j) for j in el]) for el in my]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in el]) for el in my]))


my_matrix = Matrix([
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8]],
    [[31, 22, 37],
     [43, 51, 86],
     [3, 5, 8]])

print(my_matrix.__add__())