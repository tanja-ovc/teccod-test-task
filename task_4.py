def sort_list_by_str_len(original_list: list):
    """Сортирует список строк по возрастанию и убыванию их длины."""
    try:
        validate_list_contains_only_strings(original_list)
        sorted_list_asc = sorted(original_list, key=len)
        sorted_list_desc = sorted(original_list, key=len, reverse=True)
        print(f'Список по возрастанию длины строк: {sorted_list_asc}')
        print(f'Список по убыванию длины строк: {sorted_list_desc}')
        return sorted_list_asc, sorted_list_desc
    except ValueError as error:
        print(error)


def validate_list_contains_only_strings(original_list: list):
    for item in original_list:
        if not isinstance(item, str):
            raise ValueError(
                f'Ошибка: В полученном списке {original_list} найден '
                'элемент, не являющийся строкой.'
            )


if __name__ == '__main__':
    trees = ['берёза', 'клён', 'дуб', 'ясень', 'липа']
    sort_list_by_str_len(trees)

    wrong_list = ['берёза', 1, 'дуб', 2, 'липа']
    sort_list_by_str_len(wrong_list)
