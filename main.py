variables = {}

def get_digit(number):
    if number.isdigit():
        return int(number)
    return variables[number] 


def get_instruction(code_line: str) -> dict:
    instruction = {}

    # Если в строке кода содержится оператор присваивания
    if ":=" in code_line:
        # Разрезаем строку кода по пробелам
        # Затем извлекаем из неё имя переменной и значение
        components = code_line.split(" ")
        variable_name = components[0]
        value = int(components[2])
        instruction = {"operation": "assign", "variable_name": variable_name, "value": value}

        # Если в строке кода содержится оператор сложения
    elif "add" in code_line:
        # Разрезаем строку кода по пробелам
        # Затем извлекаем из неё значение переменной и числа
        components = code_line.split(" ")
        variable_name = components[1]
        # превращаем строку второго элемента в число
        value = int(components[2])
        instruction = {"operation": "add", "variable_name": variable_name, "value": value}

    # Если в строке кода содержится оператор больше
    elif ">" in code_line:
        # Разрезаем строку кода по пробелам
        components = code_line.split(" ")
        # проверям элементы на число используя функцию is_digit
        # есл иэто числе то извлекаем значения первой и второй переменных
        first_num = get_digit(components[0])
        second_name = get_digit(components[2])
        instruction = {"operation": ">", "variable_name": first_num, "value": second_name}
    return instruction


def execute(code_line: str) -> None:
    instruction = get_instruction(code_line)

    # Если операция - присваивание
    if instruction["operation"] == "assign":
        # Достаём из массива имя переменной и значение
        variable_name = instruction["variable_name"]
        value = instruction["value"]

        # Обращаемся к глобальному словарю переменных, 
        # записываем по имени переменной соответствующее значение
        variables[variable_name] = value


        # Если операция - присваивание
    elif instruction["operation"] == "add":
        # Достаём из массива имя переменной и значение
        variable_name = instruction["variable_name"]
        value = instruction["value"]

        # Обращаемся к глобальному словарю переменных, 
        # записываем по имени переменной соответствующее значение
        sum = variables[variable_name] + value

            # Если операция - присваивание
    elif instruction["operation"] == ">":
        # Достаём из массива значения первого и второго числа
        first_num = instruction["variable_name"]
        second_name = instruction["value"]
        # проверка на больше
        if first_num > second_name:
            return 1
        return 0

if __name__ == '__main__':
    print("Вас приветствует консоль! Удивительно, не правда ли? Вводите команды.")
    # Бесконечно просим пользователя вводить команды и исполняем их
    while True:
        command = input(">>> ")
        execute(command)
