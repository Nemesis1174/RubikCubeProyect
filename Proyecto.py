import os


class RubikCube:
    def __init__(self):
        self.front = [['0' for _ in range(3)] for _ in range(3)]  # Cara frontal
        self.back = [['1' for _ in range(3)] for _ in range(3)]   # Cara trasera
        self.left = [['2' for _ in range(3)] for _ in range(3)]   # Cara izquierda
        self.right = [['3' for _ in range(3)] for _ in range(3)]  # Cara derecha
        self.up = [['4' for _ in range(3)] for _ in range(3)]     # Cara superior
        self.down = [['5' for _ in range(3)] for _ in range(3)]   # Cara inferior
        
    def rotate_in_x_upper(self):
        # Guardar el estado actual de las caras afectadas
        temp_front = [row[:] for row in self.front]
        temp_up = [row[:] for row in self.up]
        temp_back = [row[:] for row in self.back]
        temp_down = [row[:] for row in self.down]

        # Rotar las filas de las caras afectadas
        self.front[0] = temp_down[0]
        self.up[0] = temp_front[0]
        self.back[0] = temp_up[0]
        self.down[0] = temp_back[0]

        # También necesitas rotar las caras izquierda y derecha
        self.rotate_side_clockwise(self.left)
        self.rotate_side_counterclockwise(self.right)

    def rotate_in_x_middle(self):
        # Guardar el estado actual de las caras afectadas
        temp_front = [row[:] for row in self.front]
        temp_left = [row[:] for row in self.left]
        temp_back = [row[:] for row in self.back]
        temp_right = [row[:] for row in self.right]

        # Rotar las filas de las caras afectadas
        self.front[1] = temp_right[1]
        self.left[1] = temp_front[1]
        self.back[1] = temp_left[1]
        self.right[1] = temp_back[1]

    def rotate_in_x_lower(self):
        # Guardar el estado actual de las caras afectadas
        temp_front = [row[:] for row in self.front]
        temp_down = [row[:] for row in self.down]
        temp_back = [row[:] for row in self.back]
        temp_up = [row[:] for row in self.up]

        # Rotar las filas de las caras afectadas
        self.front[2] = temp_up[2]
        self.down[2] = temp_front[2]
        self.back[2] = temp_down[2]
        self.up[2] = temp_back[2]

        # También necesitas rotar las caras izquierda y derecha
        self.rotate_side_counterclockwise(self.left)
        self.rotate_side_clockwise(self.right)

    def rotate_in_y_upper(self):
        # Guardar el estado actual de las caras afectadas
        temp_front = [row[:] for row in self.front]
        temp_right = [row[:] for row in self.right]
        temp_back = [row[:] for row in self.back]
        temp_left = [row[:] for row in self.left]
        
        # Rotar las columnas de las caras afectadas
        for i in range(3):
            self.front[i][0] = temp_right[i][0]
            self.right[i][0] = temp_back[2-i][2]
            self.back[2-i][2] = temp_left[i][0]
            self.left[i][0] = temp_front[i][0]
        
        # También necesitas rotar la cara superior
        self.rotate_side_clockwise(self.up)
        
    def rotate_in_y_middle(self):
        # Guardar el estado actual de las caras afectadas
        temp_front = [row[:] for row in self.front]
        temp_right = [row[:] for row in self.right]
        temp_back = [row[:] for row in self.back]
        temp_left = [row[:] for row in self.left]
        
        # Rotar las columnas de las caras afectadas
        for i in range(3):
            self.front[i][1] = temp_right[i][1]
            self.right[i][1] = temp_back[2-i][1]
            self.back[2-i][1] = temp_left[i][1]
            self.left[i][1] = temp_front[i][1]
        
    def rotate_in_y_lower(self):
        # Guardar el estado actual de las caras afectadas
        temp_front = [row[:] for row in self.front]
        temp_right = [row[:] for row in self.right]
        temp_back = [row[:] for row in self.back]
        temp_left = [row[:] for row in self.left]
        
        # Rotar las columnas de las caras afectadas
        for i in range(3):
            self.front[i][2] = temp_right[i][2]
            self.right[i][2] = temp_back[2-i][0]
            self.back[2-i][0] = temp_left[i][2]
            self.left[i][2] = temp_front[i][2]
        
        # También necesitas rotar la cara inferior
        self.rotate_side_counterclockwise(self.down)
        
    def rotate_in_z_upper(self):
        # Guardar el estado actual de las caras afectadas
        temp_up = [row[:] for row in self.up]
        temp_front = [row[:] for row in self.front]
        temp_down = [row[:] for row in self.down]
        temp_back = [row[:] for row in self.back]
        
        # Rotar las filas de las caras afectadas
        for i in range(3):
            self.up[0][i] = temp_front[0][i]
            self.front[0][i] = temp_down[0][i]
            self.down[0][i] = temp_back[0][i]
            self.back[0][i] = temp_up[0][i]
        
        # También necesitas rotar la cara derecha
        self.rotate_side_clockwise(self.right)
        
    def rotate_in_z_middle(self):
        # Guardar el estado actual de las caras afectadas
        temp_up = [row[:] for row in self.up]
        temp_front = [row[:] for row in self.front]
        temp_down = [row[:] for row in self.down]
        temp_back = [row[:] for row in self.back]
        
        # Rotar las filas de las caras afectadas
        for i in range(3):
            self.up[1][i] = temp_front[1][i]
            self.front[1][i] = temp_down[1][i]
            self.down[1][i] = temp_back[1][i]
            self.back[1][i] = temp_up[1][i]
        
    def rotate_in_z_lower(self):
        # Guardar el estado actual de las caras afectadas
        temp_up = [row[:] for row in self.up]
        temp_front = [row[:] for row in self.front]
        temp_down = [row[:] for row in self.down]
        temp_back = [row[:] for row in self.back]
        
        # Rotar las filas de las caras afectadas
        for i in range(3):
            self.up[2][i] = temp_front[2][i]
            self.front[2][i] = temp_down[2][i]
            self.down[2][i] = temp_back[2][i]
            self.back[2][i] = temp_up[2][i]
        
        # También necesitas rotar la cara izquierda
        self.rotate_side_counterclockwise(self.left)
    
    def rotate_side_clockwise(self, side):
        side[:] = [list(x) for x in zip(*side[::-1])]
        
    def rotate_side_counterclockwise(self, side):
        side[:] = [list(x) for x in zip(*side)][::-1]
    
    def random_shuffle(self):
        pass
    
    def list_shuffle(self):
        pass
    
    def print_cube(self):
        print("\t\t", self.up[0])
        print("\t\t", self.up[1])
        print("\t\t", self.up[2])
        print()
        print("", self.left[0], self.front[0], self.right[0], self.back[0])
        print("", self.left[1], self.front[1], self.right[1], self.back[1])
        print("", self.left[2], self.front[2], self.right[2], self.back[2])
        print()
        print("\t\t", self.down[0])
        print("\t\t", self.down[1])
        print("\t\t", self.down[2])



class Heuristics:
    @staticmethod
    def heuristic_1(self):
        pass
    
    @staticmethod
    def heuristic_2(self): 
        pass
    
    @staticmethod
    def heuristic_3(self):
        pass


class RubikSolver:
    def __init__(self):
        pass


os.system('cls')

cube = RubikCube()

# Estado inicial
print("Estado inicial:")
print()
cube.print_cube()
print()

# Aplicar movimientos
cube.rotate_in_x_upper()

# Estado después de los movimientos
print("\nEstado después de los movimientos:")
print()
cube.print_cube()
print()
'''
# Aplicar movimientos
cube.rotate_in_y_upper()
cube.rotate_in_y_middle()
cube.rotate_in_y_lower()

# Estado después de los movimientos
print("\nEstado después de los movimientos:")
print()
print("Frontal:", cube.front)
print("Superior:", cube.up)
print("Trasera:", cube.back)
print("Inferior:", cube.down)
print("Izquierda:", cube.left)
print("Derecha:", cube.right)
# Aplicar movimientos
cube.rotate_in_z_upper()
cube.rotate_in_z_middle()
cube.rotate_in_z_lower()

# Estado después de los movimientos
print("\nEstado después de los movimientos:")
print()
print("Frontal:", cube.front)
print("Superior:", cube.up)
print("Trasera:", cube.back)
print("Inferior:", cube.down)
print("Izquierda:", cube.left)
print("Derecha:", cube.right)
print()
'''