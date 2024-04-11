def get_unique_numbers(original_list: list):
    """Принимает на вход список целых чисел и возвращает новый список,
    содержащий только уникальные элементы из исходного списка.
    """
    try:
        validate_list_contains_only_integers(original_list)
        unique_numbers_list = list(set(original_list))
        print(f'Возвращаемый список уникальных чисел: {unique_numbers_list}')
        return unique_numbers_list
    except ValueError as error:
        print(error)


def validate_list_contains_only_integers(original_list: list):
    for item in original_list:
        if not isinstance(item, int) or isinstance(item, bool):
            raise ValueError(
                f'Ошибка: В полученном списке {original_list} найден '
                'элемент, не являющийся целым числом.'
            )


if __name__ == '__main__':
    get_unique_numbers([0, 4, 4, 4, 4, 55, 88])
    get_unique_numbers([0, 4, 'k', 4, 4, 55, 88])
    get_unique_numbers([0, 4, 7.66, 4, 4, 55, 88])
    get_unique_numbers([0, 4, True, 4, 4, 55, 88])
    get_unique_numbers([0, 4, (9, 8), 4, 4, 55, 88])
