import os
import copy
import random
import heapq
import time
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
            (self.rotate_upper, 1),
            (self.rotate_lower, 2),
            (self.rotate_left, 3),
            (self.rotate_right, 4),
            (self.rotate_front, 5),
            (self.rotate_back, 6),
            (self.rotate_upper_anticlock, 7),
            (self.rotate_lower_anticlock, 8),
            (self.rotate_left_anticlock, 9),
            (self.rotate_right_anticlock, 10),
            (self.rotate_front_anticlock, 11),
            (self.rotate_back_anticlock, 12)
        ]

    def is_solved(self):
        return self.cube == self.solved_cube
    
    def move(self, move_func):
        move_func()
    
    @staticmethod
    def rotar_contra_reloj(matriz):
        matriz = matriz[::-1]
        matriz_rotada = [list(x) for x in zip(*matriz)]
        return matriz_rotada
    
    def rotate_upper(self):
        self.cube[0] = self.rotar_contra_reloj(self.cube[0])
        movements = [2, 3, 4, 5]
        aux = self.cube[movements[0]][0][::-1]
        self.cube[movements[0]][0] = self.cube[movements[1]][0]
        self.cube[movements[1]][0] = self.cube[movements[2]][0]
        self.cube[movements[2]][0] = self.cube[movements[3]][2][::-1]
        self.cube[movements[3]][2] = aux

    def rotate_upper_anticlock(self):
        for _ in range(3):
            self.rotate_upper()
                            
    def rotate_lower(self):
        self.cube[1] = self.rotar_contra_reloj(self.cube[1])
        movements = [4, 3, 2, 5]
        aux = self.cube[movements[0]][2][::-1]
        self.cube[movements[0]][2] = self.cube[movements[1]][2]
        self.cube[movements[1]][2] = self.cube[movements[2]][2]
        self.cube[movements[2]][2] = self.cube[movements[3]][0][::-1]
        self.cube[movements[3]][0] = aux
    
    def rotate_lower_anticlock(self):
        for _ in range(3):
            self.rotate_lower()

    def rotate_left(self):
        self.cube[2] = self.rotar_contra_reloj(self.cube[2])
        movements = [0, 5, 1, 3]
        aux = [self.cube[movements[0]][j][0] for j in range(3)]  
        for i in range(3):
            for j in range(3):  
                self.cube[movements[i]][j][0] = self.cube[movements[i + 1]][j][0]
        for j in range(3):  
            self.cube[movements[3]][j][0] = aux[j]

    def rotate_left_anticlock(self):
        for _ in range(3):
            self.rotate_left()

    def rotate_right(self):
        self.cube[4] = self.rotar_contra_reloj(self.cube[4])
        movements = [3, 1, 5 ,0]
        aux = [self.cube[movements[0]][j][2] for j in range(3)]  
        for i in range(3):
            for j in range(3):  
                self.cube[movements[i]][j][2] = self.cube[movements[i + 1]][j][2]
        for j in range(3):  
            self.cube[movements[3]][j][2] = aux[j]

    def rotate_right_anticlock(self):
        for _ in range(3):
            self.rotate_right()

    def rotate_front(self):
        self.cube[3] = self.rotar_contra_reloj(self.cube[3])
        movements = [4, 0, 2, 1]
        aux = [self.cube[movements[0]][j][0] for j in range(3)]  
        for i in range(3):
            self.cube[movements[0]][i][0] = self.cube[movements[1]][2][i]
        for i in range(3):
            self.cube[movements[1]][2][i] = self.cube[movements[2]][2 -i][2]
        for i in range(3):
            self.cube[movements[2]][i][2] = self.cube[movements[3]][0][i]
        for i in range(3):
            aux = aux[::-1]
            self.cube[movements[3]][0][i] = aux[i]

    def rotate_front_anticlock(self):
        for _ in range(3):
            self.rotate_front()

    def rotate_back(self):
        self.cube[5] = self.rotar_contra_reloj(self.cube[5])
        movements = [1, 2, 0, 4]
        aux = [self.cube[movements[0]][2][j] for j in range(3)]  
        for i in range(3):
            self.cube[movements[0]][2][i] = self.cube[movements[1]][i][0]
        for i in range(3):
            self.cube[movements[1]][i][0] = self.cube[movements[2]][0][2 - i]
        for i in range(3):
            self.cube[movements[2]][0][i] = self.cube[movements[3]][i][2]
        for i in range(3):
            aux = aux[::-1]
            self.cube[movements[3]][i][2] = aux[i]

    def rotate_back_anticlock(self):
        for _ in range(3):
            self.rotate_back()

    def list_shuffle(self, moves_list):
        print("List shuffle:\n")
        for move_num in moves_list:
            move, _ = next((m for m in self.movements if m[1] == move_num), None)
            if move:
                move_name = self.get_move_name(move_num)
                print("Movimiento:", move_num, "-", move_name, "\n")
                move() 
            else:
                print("Movimiento inválido:", move_num)

    def random_shuffle(self, num_moves):
        print("Random shuffle:\n")
        for _ in range(num_moves):
            move, move_num = random.choice(self.movements)
            move_name = self.get_move_name(move_num)
            print("Movimiento:", move_num, "-", move_name, "\n")
            move()  

    def get_move_name(self, move_num):
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
        
    
class Node:
    def __init__(self, cube):
        self.cube = cube
        self.path = []

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
    
    
class RubikSolver:
    def __init__(self, cube):
        self.cube = cube
        self.path = []

    def breadth_first_search(self):
        cube = self.cube
        start_node = Node(copy.deepcopy(cube.cube))
        final_node = Node(copy.deepcopy(cube.solved_cube))
        
        visited = set()
        
        queue = deque([start_node])
        
        while queue:
            current_node = queue.popleft()
            if current_node.cube == final_node.cube:
                path = [move_num for _, move_num in current_node.path]
                return len(path), [num for _, num in current_node.path]
            
            visited.add(current_node)
            
            for move_func, move_num in cube.movements:
                if move_func:
                    new_cube = copy.deepcopy(current_node.cube)
                    cube.cube = new_cube
                    cube.move(move_func) 
                    neighbor_node = Node(cube.cube)
                    neighbor_node.path = current_node.path + [(move_func, move_num)]
                    
                    if neighbor_node not in visited:
                        queue.append(neighbor_node)
                        visited.add(neighbor_node)
        
        return False

    def best_first_search(self, heuristic):
        cube = self.cube
        start_node = Nodeh(copy.deepcopy(cube.cube))
        goal_node = Node(copy.deepcopy(cube.solved_cube))
        
        visited = set()
        
        priority_queue = []
        
        heapq.heappush(priority_queue, (start_node.value_heuristic, start_node))

        while priority_queue:
            current_node = heapq.heappop(priority_queue)[1]
            if current_node.cube == goal_node.cube:
                path = [move_num for _, move_num in current_node.path]
                return len(path), [num for _, num in current_node.path]
                
            visited.add(current_node)
            
            for move_func, move_num in cube.movements:
                new_cube_state = copy.deepcopy(current_node.cube)
                cube.cube = new_cube_state
                cube.move(move_func)
                neighbor_node = Nodeh(cube.cube)
                neighbor_node.path = current_node.path + [(move_func, move_num)] 
                neighbor_node.calculate_heuristic(heuristic)

                if neighbor_node not in visited:
                    heapq.heappush(priority_queue, (neighbor_node.value_heuristic, neighbor_node))
                else:
                    for _, node in priority_queue:
                        if node == neighbor_node and node.value_heuristic > neighbor_node.value_heuristic:
                            node.value_heuristic = neighbor_node.value_heuristic
        
        return False

    # Implementación del algoritmo A*
    def a_star(self, heuristic):
        cube = self.cube
        start_node = NodeAStar(copy.deepcopy(cube.cube))
        goal_node = Node(copy.deepcopy(cube.solved_cube))
        
        visited = set()
        
        pq = PriorityQueue()
        
        pq.put(start_node)

        while not pq.empty():
            current_node = pq.get()
            if current_node.cube == goal_node.cube:
                path = [move_num for _, move_num in current_node.path]
                return len(path), [num for _, num in current_node.path]

            if current_node in visited:
                continue

            visited.add(current_node)
            for move_func, move_num in cube.movements:
                new_cube_state = copy.deepcopy(current_node.cube)
                cube.cube = new_cube_state
                cube.move(move_func)
                neighbor_node = NodeAStar(copy.deepcopy(cube.cube))
                neighbor_node.path = current_node.path + [(move_func, move_num)]
                neighbor_node.calculate_heuristic(heuristic)
                neighbor_node.distance = current_node.distance + 1
                pq.put(neighbor_node)

        return False

    def ida_star(self, heuristic):
        depth_limit = 1
        while True:
            found, solution = self.ida_star_search(heuristic, depth_limit, [])
            if found:
                return len(solution), solution
            depth_limit += 1

    def ida_star_search(self, heuristic, depth_limit, path):
        if depth_limit == 0:
            if self.cube.is_solved():
                return True, path
            else:
                return False, None

        for move_func, move_num in self.cube.movements:
            new_cube = copy.deepcopy(self.cube)
            new_cube.move(move_func)
            new_path = path + [move_num]
            found, solution = self.__recursive_search(new_cube, heuristic, depth_limit - 1, new_path)
            if found:
                return True, solution

        return False, None

    def __recursive_search(self, cube, heuristic, depth_limit, path):
        if depth_limit == 0:
            if cube.is_solved():
                return True, path
            else:
                return False, None

        for move_func, move_num in cube.movements:
            new_cube = copy.deepcopy(cube)
            new_cube.move(move_func)
            new_path = path + [move_num]
            found, solution = self.__recursive_search(new_cube, heuristic, depth_limit - 1, new_path)
            if found:
                return True, solution

        return False, None


os.system('cls')

'''
cube = RubikCube()

print("Estado inicial del.cube:\n")
cube.print_cube()
print()

cube.random_shuffle(3)

solver = RubikSolver(cube)
'''

# Número de ejecuciones
num_executions = 20

# Lista para almacenar los tiempos de ejecución
execution_times = []


# Bucle para ejecutar el algoritmo 20 veces y medir el tiempo
for i in range(num_executions):
    cube = RubikCube()  # Creamos un nuevo cubo Rubik
    cube.random_shuffle(3)  # Barajamos aleatoriamente el cubo
 
    solver = RubikSolver(cube)  # Creamos un solucionador con el cubo barajado
    
    # Probar el algoritmo de búsqueda en amplitud (BFS)
    print("Best First Search:")
    # Obtener el tiempo de inicio
    start_time = time.time()
    num_moves, moves = solver.a_star(Heuristics.hamming_distance)
    # Obtener el tiempo de finalización
    end_time = time.time()
    # Calcular el tiempo transcurrido
    execution_time = end_time - start_time
    print("\nNúmero de movimientos:", num_moves)
    print("Secuencia de movimientos:", moves)
    print("Tiempo de ejecución:", execution_time, "segundos")
    print()
    
    execution_times.append(execution_time)  # Agregar el tiempo a la lista

# Calcular el promedio, mínimo y máximo de tiempo de ejecución
average_execution_time = sum(execution_times) / num_executions
min_execution_time = min(execution_times)
max_execution_time = max(execution_times)

# Imprimir los resultados
print("Promedio de tiempo de ejecución:", average_execution_time, "segundos")
print("Tiempo mínimo de ejecución:", min_execution_time, "segundos")
print("Tiempo máximo de ejecución:", max_execution_time, "segundos")


'''
# Probar el algoritmo de la mejor primer búsqueda (BFS)
print("Best First Search:")
num_moves, moves = solver.best_first_search(Heuristics.hamming_distance)
print("\nNúmero de movimientos:", num_moves)
print("Secuencia de movimientos:", moves)
print()
'''

'''
# Probar el algoritmo de búsqueda A* 
print("A* Search:")
num_moves, moves = solver.a_star(Heuristics.hamming_distance)
print("\nNúmero de movimientos:", num_moves)
print("Secuencia de movimientos:", moves)
print()
'''

'''
# Probar el algoritmo IDA*
print("IDA* Search:")
# Llamar al método IDA* con la heurística deseada
num_moves, moves = solver.ida_star(Heuristics.hamming_distance)
print("\nNúmero de movimientos:", num_moves)
print("Secuencia de movimientos:", moves)
print()
'''


