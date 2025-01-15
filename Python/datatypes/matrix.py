class Matrix:
    _rows: int
    _cols: int
    matrix: list[list[int]] 
    def __init__(self, *args):
        _matrix = []
        # Handles Arguments 
        if len(args) == 1 and isinstance(args[0], list):
            for row in self.matrix:
                if len(row) != len(self.matrix[0]):
                    raise Exception("Invalid Matrix")
            self.matrix = args[0]
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            for row in range(args[0]):
                _ = [0 for _ in range(args[1])]
                _matrix.append(_)
            self._setMatrix(_matrix)
        else:
            raise Exception("Invalid Arguments. Expected (rows: int, cols: int)  or a Two dimensional array denoting the matrix")
        
    def _setMatrix(self, matrix: list[list[int]]):
        self.matrix = matrix

        # Check if the length of the rows are equal

        self._cols = len(self.matrix[0])
        self._rows = len(self.matrix)

    def getDimensions(self):
        return self._rows, self._rows 
    
    # Operator Overloading
    def __add__(self, other):
        if isinstance(other, Matrix):
            # TODO impl
            raise NotImplementedError
        else:
            raise Exception("Invalid Type. Expected Matrix")
        
    def __sub__(self, other):
        if isinstance(other, Matrix):
            # TODO impl
            raise NotImplementedError
        else:
            raise Exception("Invalid Type. Expected Matrix")
            
    def __mul__(self, other):
        if isinstance(other, Matrix):
            # TODO impl
            raise NotImplementedError
        elif isinstance(other, int) or isinstance(other, float):
            # TODO impl
            raise NotImplementedError
        elif isinstance(other, list):
            # TODO impl
            raise NotImplementedError
        else:
            raise Exception("Invalid Type. Expected Matrix")
    
    # GetRow: Matrix[row_index]
    # GetColumn: Not Supported yet
    # GetElement: Matrix[row_index][col_index] or Matrix[(row_index, col_index)] 
    def __getitem__(self, key):
        return self.matrix[key]

matrix = Matrix(3, 3)
print(matrix.getDimensions()) # (3, 3)