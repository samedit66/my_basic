variables = {}


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
    elif "mul" in code_line:
        components = code_line.split(" ")
        variable_name = components[1]
        value = components[2]
        value = int(value)
        instruction = {"operation": "multiply", "variable_name": variable_name, "value": value}

    elif 'sub' in code_line:
        components = code_line.split(' ')
        variable_name = components[1]
        value = int(components[2])
        instruction = {"operation": "sub", "variable_name": variable_name, "value": value}


    elif  'if' in code_line:
        components = code_line.split(" ")
        variable_1_name = int(components[1])
        variable_2_name = int(components[3])
        instruction = {"operation": 'if', "variable_1_name": variable_1_name, "variable_2_name": variable_2_name}

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
    elif instruction["operation"] == "multiply":
        variable_name = instruction["variable_name"]
        value = instruction["value"]
        variables[variable_name] *= value

    elif  instruction['operation'] == 'sub':
        variable_name = instruction['variable_name']
        value = instruction["value"]
        variables[variable_name] -= value

    elif instruction['operation'] == 'if':
        variable_1_name = instruction['variable_1_name']
        variable_2_name = instruction['variable_2_name']
        if variable_1_name > variable_2_name: print('variable_1_name > variable_2_name')
        if variable_1_name == variable_2_name: print('variable_1_name = variable_2_name')
        else:  print('variable_1_name < variable_2_name')






if __name__ == '__main__':
    print("Вас приветствует консоль! Удивительно, не правда ли? Вводите команды.")
    # Бесконечно просим пользователя вводить команды и исполняем их
    while True:
        command = input(">>> ")
        execute(command)
