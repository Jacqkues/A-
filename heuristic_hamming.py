from heuristic import Heuristic


class Heuristic_Hamming(Heuristic):
    def calculer_heuristic(self, a, b):
        distance = 0
        size = len(a)
        
        for i in range(size):
            for j in range(size):
                value = a[i][j]
                if value != 0:
                    goal_i, goal_j = self.find_goal_position(value, b)
                    if i != goal_i or j != goal_j:
                        distance += 1
        
        return distance

    def find_goal_position(self, value, b):
        size = len(b)
        for i in range(size):
            for j in range(size):
                if b[i][j] == value:
                    return i, j
        return None