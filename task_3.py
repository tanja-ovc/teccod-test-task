import math


class Point:
    """Представляет точку в двумерном пространстве."""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distance_to_other_point(self, point_2):
        current_point_coordinates = self.get_coordinates()
        point_2_coordinates = point_2.get_coordinates()
        distance = math.dist(current_point_coordinates, point_2_coordinates)
        return distance

    def get_coordinates(self):
        coordinates = self._x, self._y
        return coordinates

    def change_coordinates(self, new_x, new_y):
        self._x = new_x
        self._y = new_y


if __name__ == '__main__':
    point_one = Point(3, 2)
    point_two = Point(-1, -6)

    print(f'Координаты точки 1: {point_one.get_coordinates()}')
    print('Расстояние от точки 1 до точки 2: '
          f'{point_one.distance_to_other_point(point_two)}')
    point_one.change_coordinates(-9, 10)
    print(f'Координаты точки 1: {point_one.get_coordinates()}')
