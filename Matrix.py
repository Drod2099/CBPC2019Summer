from Vector import *


class Matrix(object):
    def __init__(self, contents, rows, columns):
        """
        Creates a Matrix object.
        :param contents: list of values
        :param rows: # of rows in matrix
        :param columns: # of columns in matrix
        """
        self.data = contents
        self.dim = (rows, columns)

    def __str__(self):
        """
        Prints Matrix in desired format
        :return: Custom Matrix format
        """
        s = ""
        s += "/"
        row = 1
        column = 1
        for i in range(len(self.data)):
            if column == 1 and (row != 1 and row != self.dim[0]):
                s += "|"
            elif row == self.dim[0] and column == 1:
                s += "\\"
            s += str(self.data[i])
            if i < self.dim[1] * row - 1:
                s += ", "
                column += 1
            else:
                if (row == self.dim[0] and column == 1) or (row == 1 and column == self.dim[1]):
                    s += "\\\n"
                    row += 1
                    column = 1
                elif i == len(self.data) - 1:
                    s += "/"
                    column += 1
                elif column == self.dim[1] and (row != 1 and row != self.dim[0]):
                    s += "|\n"
                    row += 1
                    column = 1
        return s

    def __getitem__(self, coords):
        """
        Returns a certain matrix value
        :param coords: (row, column) location of desired value
        :return: desired value
        """
        index = coords[0] * coords[1] - 1
        return self.data[index]

    def __setitem__(self, coords, newval):
        """
        Sets desired value to specified value
        :param coords: (row, column) location of desired value
        :param newval: new value to be changed
        :return: None
        """
        index = coords[0] * coords[1] - 1
        self.data[index] = newval

    def get_row(self, row_num):
        """
        Gets and returns a specified row in Vector format
        :param row_num: desired row #
        :return: Desired row in Vector format
        """
        row = []
        for i in range(len(self.data)):
            if row_num <= i / self.dim[0] < row_num + 1:
                row.append(self.data[i])
        return Vector(*row)

    def get_column(self, col_num):
        """
        Gets and returns a specified column in Vector format
        :param col_num: desired column #
        :return: Desired column in Vector format
        """
        col = []
        row = 0
        column = 0
        for i in range(len(self.data)):
            if column == col_num:
                col.append(self.data[i])
            column += 1
            if column / self.dim[1] == 1:
                row += 1
                column = 0
        return Vector(*col)

    def __add__(self, other_mat):
        """
        Adds two matrices together
        :param other_mat: matrix to be added
        :return: sum of two matrices
        """
        new_mat_con = []
        for i in range(len(self.data)):
            new_mat_con.append(self.data[i] + other_mat.data[i])
        return Matrix(new_mat_con, self.dim[0], self.dim[1])

    def __sub__(self, other_mat):
        """
        Subtracts one matrix from another
        :param other_mat: matrix to be subtracted
        :return: difference of two matrices
        """
        new_mat_con = []
        for i in range(len(self.data)):
            new_mat_con.append(self.data[i] - other_mat.data[i])
        return Matrix(new_mat_con, self.dim[0], self.dim[1])

    def __mul__(self, other):
        """
        Multiplies a matrix by a scalar, another matrix, or a Vector object
        :param other: other value or object to be multiplied
        :return: New matrix or Vector
        """
        new_vals = []
        if other.__class__ == int or other.__class__ == float:
            for i in range(len(self.data)):
                new_vals.append(self.data[i] * other)
            return Matrix(new_vals, self.dim[0], self.dim[1])

        elif other.__class__ == Matrix:
            new_con = []
            cur_col = 0
            cur_row = 0
            for i in range(len(self.data)):
                x = self.get_row(cur_row)
                y = other.get_column(cur_col)
                value = dot(x, y)
                new_con.append(value)
                if cur_col == other.dim[1] - 1:
                    cur_row += 1
                    cur_col = 0
                else:
                    cur_col += 1
            return Matrix(new_con, self.dim[0], other.dim[1])

        elif other.__class__ == Vector or Vector2 or Vector3:
            new_con = []
            cur_row = 0
            for i in range(other.dim):
                x = self.get_row(cur_row)
                value = dot(x, other)
                new_con.append(value)
                cur_row += 1
            return Vector(*new_con)

    def __rmul__(self, other):
        """
        Multiplies a matrix by a scalar, another matrix, or a Vector object
        :param other: other value or object to be multiplied
        :return: New matrix or Vector
        """
        new_vals = []
        if other.__class__ == int or other.__class__ == float:
            for i in range(len(self.data)):
                new_vals.append(self.data[i] * other)
            return Matrix(new_vals, self.dim[0], self.dim[1])

        if other.__class__ == Vector or Vector2 or Vector3:
            new_con = []
            cur_col = 0
            for i in range(other.dim):
                x = self.get_row(cur_col)
                value = dot(x, other)
                new_con.append(value)
                cur_col += 1
            return Vector(*new_con)

    def __eq__(self, other_mat):
        """
        Checks if two matrices are equal
        :param other_mat: other matrix to be checked for equality
        :return: True or False
        """
        for i in range(len(self.data)):
            if self.data[i] != other_mat.data[i]:
                return False
        return True

    def copy(self):
        """
        Creates a deep copy of the desired matrix
        :return: deep copy of matrix
        """
        copy = []
        for i in range(len(self.data)):
            copy.append(self.data[i])
        return Matrix(copy, self.dim[0], self.dim[1])

    def inverse(self):
        """
        Creates an inverse of the matrix
        :return: Inverse of desired matrix
        """
        if self.dim[0] == 2 and self.dim[1] == 2:
            a = self.data[0]
            b = self.data[1]
            c = self.data[2]
            d = self.data[3]
            a1 = self.data[0]
            d1 = self.data[3]
            a = d1
            b = b * -1
            c = c * -1
            d = a1
            contents = [a, b, c, d]
            return Matrix(contents, 2, 2)

    def transpose(self):
        """
        Creates a transpose of the matrix
        :return: Transpose of desired matrix
        """
        new_con = []
        for i in range(self.dim[1]):
            cur_col = self.get_column(i)
            add = [*cur_col]
            for j in range(len(add)):
                new_con.append(add[j])
        return Matrix(new_con, self.dim[1], self.dim[0])

    def identity(self):
        """
        Creates an identity matrix
        :return: identity matrix of desired matrix
        """
        a = self.data[0]
        b = self.data[1]
        c = self.data[2]
        d = self.data[3]
        denom = (a * d) - (b * c)
        new_a = d / denom
        new_b = -b / denom
        new_c = -c / denom
        new_d = a / denom
        new_con = [new_a, new_b, new_c, new_d]
        return Matrix(new_con, 2, 2)

    def zero(self):
        """
        Creates a zero matrix
        :return: zero matrix
        """
        new_con = []
        for i in range(len(self.data)):
            value = -self.data[i]
            new_con.append(value)
        return Matrix(new_con, self.dim[0], self.dim[1])

    @property
    def is_zero(self):
        """
        Checks if specific matrix is a zero matrix
        :return: True or False
        """
        for i in range(len(self.data)):
            if self.data[i] != 0:
                return False
        return True

    @property
    def is_identity(self):
        """
        Checks if specific matrix is an identity matrix
        :return: True or False
        """
        identity = [1, 0, 0, 1]
        if self.data == identity:
            return True
        return False


con = [1, 2, 3, 4]
con2 = [-1, -2, -3, -4]
m = Matrix(con, 2, 2)
n = Matrix(con2, 2, 2)
new = m * n
print(new)


# list1 = [[1, 2], [3, 4], [5, 6]]
# copy = []
# #### GOOD ####
# for i in range(len(list1)):
#     temp = []
#     for j in range(len(list1[i])):
#         temp.append(list1[i][j])
#     copy.append(temp)

#### BAD ####
# for i in range(len(list1)):
#     copy.append(list1[i])
# print(copy)
# copy[1] = [8, 9]
# print(copy)
# print(list1)
# copy[0][1] = 99
# print(copy)
# print(list1)

#### BAD ####
# copy = [*list1]
# print(copy)
# copy[1] = [8, 9]
# print(copy)
# print(list1)
# copy[0][1] = 99
# print(copy)
# print(list1)
