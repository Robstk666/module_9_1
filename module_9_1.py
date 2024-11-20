def apply_all_func(int_list, *functions):
    """
    Применяет переданные функции к списку чисел и возвращает результаты в виде словаря.

    :param int_list: список чисел (int или float)
    :param functions: неограниченное количество функций
    :return: словарь, где ключ - название функции, значение - результат её вызова
    """
    results = {}
    for func in functions:
        # Запускаем функцию и сохраняем результат с её именем
        results[func.__name__] = func(int_list)
    return results


# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))