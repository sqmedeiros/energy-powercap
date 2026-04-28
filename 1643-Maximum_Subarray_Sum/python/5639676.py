def max_subsequence(list_of_numbers: list) -> int:
    suma = 0 # Сумма
    array_of_sum = [] # Пустой список
    max_in_list = max(list_of_numbers) # Макс. значение в списке

    if max_in_list < 0: # Если макс. значение в списке меньше 0 то его макс сумма равна этому числу
        suma = max_in_list
        return max_in_list
    else:
        for index,number in enumerate(list_of_numbers): # Обход списка
            array_of_sum.append(suma) # добавляю в новый список сумму
            if number < 0 and suma + number < 0:
                # array_of_sum.append(s)
                suma = 0
                continue
            elif number < 0 and number == list_of_numbers[-1]:
                continue
            else:
                suma += number
        array_of_sum.append(suma)
    return max(set(array_of_sum))


if __name__ == "__main__":
    input()
    List_of_numbers = input()  # Ввод чисел
    to_int_list_numbers = list(map(int, List_of_numbers.split())) # создания списка
    print(max_subsequence(to_int_list_numbers)) # Вывод значения вызова функции