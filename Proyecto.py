import os
import copy
import random
import heapq
from queue import PriorityQueue
from collections import deque


class RubikCube:
    def __init__(self):
        # Lado 0 - Amarillo / Lado 1 - Blanco / Lado 2 - Naranja / Lado 3 - Azul / Lado 4 - Rojo / Lado 5 - Verde
        self.cube = [
            [['0', '0', '0'], 
             ['0', '0', '0'], 
             ['0', '0', '0']],  

            [['1', '1', '1'], 
             ['1', '1', '1'], 
             ['1', '1', '1']],  

            [['2', '2', '2'], 
             ['2', '2', '2'], 
             ['2', '2', '2']], 

            [['3', '3', '3'], 
             ['3', '3', '3'], 
             ['3', '3', '3']], 

            [['4', '4', '4'], 
             ['4', '4', '4'], 
             ['4', '4', '4']], 
             
            [['5', '5', '5'], 
             ['5', '5', '5'], 
             ['5', '5', '5']]   
        ]

        self.solved_cube = copy.deepcopy(self.cube)
        
        self.movements = [
            (self.rotate_in_x_upper, 1),
            (self.rotate_in_x_lower, 2),
            (self.rotate_in_y_upper, 3),
            (self.rotate_in_y_lower, 4),
            (self.rotate_in_z_upper, 5),
            (self.rotate_in_z_lower, 6),
            (self.rotate_in_x_upper_anticlock, 7),
            (self.rotate_in_x_lower_anticlock, 8),
            (self.rotate_in_y_upper_anticlock, 9),
            (self.rotate_in_y_lower_anticlock, 10),
            (self.rotate_in_z_upper_anticlock, 11),
            (self.rotate_in_z_lower_anticlock, 12)
        ]

    def is_solved(self):
        return self.cube == self.solved_cube
    
    def move(self, move_func):
        # La función de movimiento se pasa como argumento, así que la llamamos directamente
        move_func()
    
    def rotate_in_x_upper(self):
        # Copy the affected sides to temporary matrices
        temp0 = [row[:] for row in self.cube[0]]
        temp1 = [row[:] for row in self.cube[1]]
        temp2 = [row[:] for row in self.cube[2]]
        temp4 = [row[:] for row in self.cube[4]]

        # Rotate the elements in the temporary matrices clockwise
        for i in range(len(temp0)):
            for j in range(len(temp0)):
                self.cube[0][i][j] = temp1[i][j]
                self.cube[1][i][j] = temp2[i][j]
                self.cube[2][i][j] = temp4[i][j]
                self.cube[4][i][j] = temp0[i][j]

    def rotate_in_x_upper_anticlock(self):
        for _ in range(3):
            self.rotate_in_x_upper()
                            
    def rotate_in_x_lower(self):
        # Copy the affected sides to temporary matrices
        temp0 = [row[:] for row in self.cube[0]]
        temp1 = [row[:] for row in self.cube[1]]
        temp3 = [row[:] for row in self.cube[3]]
        temp5 = [row[:] for row in self.cube[5]]

        # Rotate the elements in the temporary matrices counter-clockwise
        for i in range(len(temp0)):
            for j in range(len(temp0)):
                self.cube[0][i][j] = temp3[i][j]
                self.cube[1][i][j] = temp0[i][j]
                self.cube[3][i][j] = temp5[i][j]
                self.cube[5][i][j] = temp1[i][j]
    
    def rotate_in_x_lower_anticlock(self):
        for _ in range(3):
            self.rotate_in_x_lower()

    def rotate_in_y_upper(self):
        # Copy the affected sides to temporary matrices
        temp0 = [row[:] for row in self.cube[0]]
        temp2 = [row[:] for row in self.cube[2]]
        temp1 = [row[:] for row in self.cube[1]]
        temp3 = [row[:] for row in self.cube[3]]

        # Rotate the elements in the temporary matrices clockwise
        for i in range(len(temp0)):
            for j in range(len(temp0)):
                self.cube[0][i][j] = temp3[i][j]
                self.cube[2][i][j] = temp0[i][j]
                self.cube[1][i][j] = temp2[i][j]
                self.cube[3][i][j] = temp1[i][j]

    def rotate_in_y_upper_anticlock(self):
        for _ in range(3):
            self.rotate_in_y_upper()

    def rotate_in_y_lower(self):
        # Copy the affected sides to temporary matrices
        temp0 = [row[:] for row in self.cube[0]]
        temp2 = [row[:] for row in self.cube[2]]
        temp1 = [row[:] for row in self.cube[1]]
        temp3 = [row[:] for row in self.cube[3]]

        # Rotate the elements in the temporary matrices counter-clockwise
        for i in range(len(temp0)):
            for j in range(len(temp0)):
                self.cube[0][i][j] = temp2[i][j]
                self.cube[2][i][j] = temp1[i][j]
                self.cube[1][i][j] = temp3[i][j]
                self.cube[3][i][j] = temp0[i][j]

    def rotate_in_y_lower_anticlock(self):
        for _ in range(3):
            self.rotate_in_y_lower()

    def rotate_in_z_upper(self):
        # Copy the affected sides to temporary matrices
        temp2 = [row[:] for row in self.cube[2]]
        temp3 = [row[:] for row in self.cube[3]]
        temp4 = [row[:] for row in self.cube[4]]
        temp5 = [row[:] for row in self.cube[5]]

        # Rotate the elements in the temporary matrices clockwise
        for i in range(len(temp2)):
            for j in range(len(temp2)):
                self.cube[2][i][j] = temp5[i][j]
                self.cube[3][i][j] = temp2[i][j]
                self.cube[4][i][j] = temp3[i][j]
                self.cube[5][i][j] = temp4[i][j]

    def rotate_in_z_upper_anticlock(self):
        for _ in range(3):
            self.rotate_in_z_upper()

    def rotate_in_z_lower(self):
        # Copy the affected sides to temporary matrices
        temp2 = [row[:] for row in self.cube[2]]
        temp3 = [row[:] for row in self.cube[3]]
        temp4 = [row[:] for row in self.cube[4]]
        temp5 = [row[:] for row in self.cube[5]]

        # Rotate the elements in the temporary matrices counter-clockwise
        for i in range(len(temp2)):
            for j in range(len(temp2)):
                self.cube[2][i][j] = temp3[i][j]
                self.cube[3][i][j] = temp4[i][j]
                self.cube[4][i][j] = temp5[i][j]
                self.cube[5][i][j] = temp2[i][j]

    def rotate_in_z_lower_anticlock(self):
        for _ in range(3):
            self.rotate_in_z_lower()

    def list_shuffle(self, moves_list):
        for move_num in moves_list:
            move, _ = next((m for m in self.movements if m[1] == move_num), None)
            if move:
                move_name = self.get_move_name(move_num)
                print("Movimiento:", move_num, "-", move_name, "\n")
                move()  # Ejecutar el movimiento
                self.print_cube()
                print()
            else:
                print("Movimiento inválido:", move_num)

    def random_shuffle(self, num_moves):
        # Realizar un shuffle aleatorio
        for _ in range(num_moves):
            move, move_num = random.choice(self.movements)
            move_name = self.get_move_name(move_num)
            print("Movimiento:", move_num, "-", move_name, "\n")
            move()  # Ejecutar el movimiento
            self.print_cube()
            print()

    def get_move_name(self, move_num):
        # Retorna la descripción del movimiento según el número asignado
        if move_num == 1:
            return "Rotación en el eje X (arriba)"
        elif move_num == 2:
            return "Rotación en el eje X (abajo)"
        elif move_num == 3:
            return "Rotación en el eje Y (izquierda)"
        elif move_num == 4:
            return "Rotación en el eje Y (derecha)"
        elif move_num == 5:
            return "Rotación en el eje Z (frontal)"
        elif move_num == 6:
            return "Rotación en el eje Z (trasero)"
        elif move_num == 7:
            return "Rotación en el eje X antihorario (arriba)"
        elif move_num == 8:
            return "Rotación en el eje X antihorario (abajo)"
        elif move_num == 9:
            return "Rotación en el eje Y antihorario (izquierda)"
        elif move_num == 10:
            return "Rotación en el eje Y antihorario (derecha)"
        elif move_num == 11:
            return "Rotación en el eje Z antihorario (frontal)"
        elif move_num == 12:
            return "Rotación en el eje Z antihorario (trasero)"        

    def get_state(self):
        return self.cube

    def print_cube(self):
        # Imprimir la cara superior
        for row in self.cube[0]:
            print("                ", row)
        
        # Imprimir las caras laterales
        for i in range(3):
            print("", self.cube[4][i], self.cube[1][i], self.cube[2][i], self.cube[3][i])

        # Imprimir la cara inferior
        for row in self.cube[5]:
            print("                ", row)


class Heuristics:
    @staticmethod
    def manhattan_distance(cube):
        distance = 0
        for face in cube:
            for i in range(3):
                for j in range(3):
                    if face[i][j] != face[1][1]:
                        distance += abs(i - 1) + abs(j - 1)
        return distance

    @staticmethod
    def incorrect_orientations(cube):
        count = 0
        for face in cube:
            for i in range(3):
                for j in range(3):
                    if face[i][j] != face[1][1]:
                        count += 1
        return count

    @staticmethod
    def hamming_distance(cube):
        goal_cube = [
            [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']],  # Lado 0 - Amarillo
            [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']],  # Lado 1 - Blanco
            [['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']],  # Lado 2 - Naranja
            [['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']],  # Lado 3 - Azul
            [['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']],  # Lado 4 - Rojo
            [['5', '5', '5'], ['5', '5', '5'], ['5', '5', '5']]   # Lado 5 - Verde
        ]

        distance = 0
        for face, goal_face in zip(cube, goal_cube):
            for row, goal_row in zip(face, goal_face):
                for cubie, goal_cubie in zip(row, goal_row):
                    if cubie != goal_cubie:
                        distance += 1
        return distance
    
    
#Basic Nodes
class Node:
    def __init__(self, cube):
        self.cube = cube
        self.path = []

#Nodes with heuristic value
class Nodeh:
    def __init__(self, cube):
        self.cube = cube
        self.value_heuristic = -1
        self.path = []
        
    def calculate_heuristic(self, heuristic):
        self.value_heuristic = heuristic(self.cube)
    
    def __lt__(self, other):
        return self.value_heuristic < other.value_heuristic

class NodeAStar(Nodeh):
    def __init__(self, cube):
        super().__init__(cube)
        self.distance = 0

    def __lt__(self, other):
        return self.value_heuristic + self.distance < other.value_heuristic + other.distance  
    
    def __eq__(self, other):
        return isinstance(other, NodeAStar) and self.cube == other.cube
    
    def __hash__(self) -> int:
        cube_tuple = tuple(map(lambda x: tuple(map(tuple, x)), self.cube))
        return hash(cube_tuple)
    
    
# Definición de la clase Solver para resolver el Cubo de Rubik
class RubikSolver:
    def __init__(self, cube):
        self.cube = cube
        self.path = []

    # Implementación del algoritmo BFS
    def breadth_first_search(self):
        cube = self.cube
        start_node = Node(copy.deepcopy(cube.cube))
        final_node = Node(copy.deepcopy(cube.solved_cube))
        
        visited = set()
        
        queue = deque([start_node])
        
        num_moves = 0
        
        while queue:
            current_node = queue.popleft()
            if current_node.cube == final_node.cube:
                return num_moves, self.path
            
            visited.add(current_node)
            
            for move_num in cube.movements:
                move_func, _ = next((m for m in cube.movements if m[1] == move_num[1]), None)
                self.path.append(move_num[1])
                if move_func:
                    new_cube = copy.deepcopy(current_node.cube)
                    cube.cube = new_cube
                    cube.move(move_func) 
                    neighbor_node = Node(cube.cube)
                    neighbor_node.path = current_node.path + [move_num]
                    
                    if neighbor_node not in visited:
                        queue.append(neighbor_node)
                        visited.add(neighbor_node)
                        num_moves += 1
        
        return False
   
    # Implementación del algoritmo Best-First Search (similar a Greedy Best-First)
    def best_first_search(self, heuristic):
        cube = self.cube
        start_node = Nodeh(copy.deepcopy(cube.cube))
        goal_node = Node(copy.deepcopy(cube.solved_cube))
        visited = set()
        priority_queue = []
        
        heapq.heappush(priority_queue, (start_node.value_heuristic, start_node))
        
        num_moves = 0

        while priority_queue:
            current_node = heapq.heappop(priority_queue)[1]
            if current_node.cube == goal_node.cube:
                return num_moves, current_node.path
            
            visited.add(current_node)
            
            for move_func, _ in cube.movements:
                new_cube_state = copy.deepcopy(current_node.cube)
                cube.cube = new_cube_state
                cube.move(move_func)
                num_moves += 1
                neighbor_node = Nodeh(cube.cube)
                neighbor_node.path = current_node.path + [move_func]
                neighbor_node.calculate_heuristic(heuristic)

                if neighbor_node not in visited:
                    heapq.heappush(priority_queue, (neighbor_node.value_heuristic, neighbor_node))
                    visited.add(neighbor_node)
                    
        return False

    # Implementación del algoritmo A*
    def a_star(self, heuristic):
        pass

    def ida_star(self):
        pass


os.system('cls')

# Ejemplo de uso
if __name__ == "__main__":
    # Se crea un objeto de la clase RubikCube para representar el estado inicial del.cube
    cube = RubikCube()
    
    print("Estado inicial del.cube:\n")
    cube.print_cube()
    print()
    # Se hace un shuffle aleatorio en el.cube
    cube.random_shuffle(3)  # Por ejemplo, hacer 5 movimientos aleatorios

    # Crear un objeto de la clase RubikSolver
    solver = RubikSolver(cube)
    
    '''
    # Probar el algoritmo de búsqueda en amplitud (BFS)
    print("Breadth First Search:")
    num_moves, moves = solver.breadth_first_search()
    print("\nNúmero de movimientos:", num_moves)
    print("Secuencia de movimientos:", moves)
    print()
    '''

    # Probar el algoritmo de búsqueda en amplitud (BFS)
    print("Best First Search:")
    num_moves, moves = solver.best_first_search(Heuristics.manhattan_distance)
    if num_moves:
        print("\nNúmero de movimientos:", num_moves)
        print("Secuencia de movimientos:", moves)
    else:
        print("No se encontró solución.")
    print()
