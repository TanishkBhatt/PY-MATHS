class Matrix:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.matrix: list[list] = [[0] * self.col for _ in range(self.row)]


    def __str__(self) -> str:
        return f"MATRIX: {self.matrix}"


    def fillMatrix(self, data: list[list]) -> None:
        if len(data) != self.row:
            raise ValueError("'Row' count mis-match")

        for row in data:
            if len(row) != self.col:
                raise ValueError("'Column' count mis-match")

        self.matrix = [row[:] for row in data]


    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Addition allowed only between 'Matrix' objects")

        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrices must have same 'dimensions'")

        result = Matrix(self.row, self.col)

        for i in range(self.row):
            for j in range(self.col):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return result
    
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Subtraction allowed only between 'Matrix' objects")

        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrices must have same 'dimensions'")

        result = Matrix(self.row, self.col)

        for i in range(self.row):
            for j in range(self.col):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]

        return result
