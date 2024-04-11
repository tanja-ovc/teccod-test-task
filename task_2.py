def get_integers_range(minimum: int, maximum: int):
    """Принимает на вход два целых числа (минимум и максимум) и
    возвращает список всех простых чисел в заданном диапазоне.
    """
    try:
        validate_min_and_max_are_integers(minimum, maximum)
        validate_min_is_less_than_max(minimum, maximum)
        integers_range = [number for number in range(minimum, maximum + 1)]
        print(f'Возвращаемый диапазон простых чисел: {integers_range}')
        return integers_range
    except ValueError as error:
        print(error)


def validate_min_and_max_are_integers(minimum, maximum):
    if not isinstance(minimum, int) or not isinstance(maximum, int):
        raise ValueError(
            'Ошибка: Границы диапазона должны быть целыми числами.'
        )


def validate_min_is_less_than_max(minimum, maximum):
    if minimum > maximum:
        raise ValueError(
            'Ошибка: Начало числового диапазона должно быть меньше его конца '
            'либо равно ему.'
        )


if __name__ == '__main__':
    get_integers_range(1, 4)
    get_integers_range(4, 4)
    get_integers_range(4, 1)
    get_integers_range('k', 1)
