
# Функция для перехода из одного стостояния другого. 0 - стартовое сотояние, 5 конечное
def change_state(state, char):
    if state == 0:
        if char == '0':
            return 1
        else:
            return None
    elif state == 1:
        if char == '1':
            return 2
        else:
            return None
    elif state == 2:
        if char == '1':
            return 3
        else:
            return None
    elif state == 3:
        if char == '1':
            return 4
        elif char == '0':
            return 5
        else:
            return None
    elif state == 4:
        if char == '1':
            return 3
        else:
            return None


# Функция по обработке подстроки строки, если она корректная, то истина, иначе ложь
def is_chain(chain):

    current_state = 0

    for i in chain:
        current_state = change_state(current_state, i)
        if current_state is None: # если ушли в пустое множество, то возвращаем ложь
            return False

    return True


inString = str(input())
index = inString.find("10")
stack = list()

first = 0
last = 0
# перебираем строку отлавливая начала 01 и концы 10
while True:
    first = inString.find("01", first)

    last = inString.find("10", first)
    if first == -1 or last == -1:
        break
    if is_chain(inString[first:last+2]):
        stack.append(first)
        stack.append(last + 2)

    first = last + 1

first = 0
while first < len(stack):
    print(f"Correct substring in position {stack[first]}: {inString[stack[first]:stack[first+1]]}")
    first += 2
