msg_ = [
    "Enter an equation",  # 0
    "Do you even know what numbers are? Stay focused!",  # 1
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",  # 2
    "Yeah... division by zero. Smart move...",  # 3
    "Do you want to store the result? (y / n):",  # 4
    "Do you want to continue calculations? (y / n):",  # 5
    " ... lazy",  # 6
    " ... very lazy",  # 7
    " ... very, very lazy",  # 8
    "You are",  # 9
    "Are you sure? It is only one digit! (y / n)",  # 10
    "Don't be silly! It's just one number! Add to the memory? (y / n)",  # 11
    "Last chance! Do you really want to embarrass yourself? (y / n)"  # 12
]
valid_operators = ['+', '-', '*', '/']
memory = 0


def is_one_digit(v):
    return v == int(v) and -10 < v < 10


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 in valid_operators[:2]):
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


while True:
    calc = input(msg_[0]).split()
    x = calc[0]
    op = calc[1]
    y = calc[2]

    try:
        if x == 'M' and y == 'M':
            x = memory
            y = memory
        elif y == 'M':
            x = float(x)
            y = memory
        elif x == 'M':
            x = memory
            y = float(y)
        else:
            x = float(x)
            y = float(y)
        check(x, y, op)
        if op not in valid_operators:
            print(msg_[2])
            continue
        if op == valid_operators[3] and y == 0:
            print(msg_[3])
            continue
        else:
            if op == valid_operators[0]:
                result = x + y
            elif op == valid_operators[1]:
                result = x - y
            elif op == valid_operators[2]:
                result = x * y
            elif op == valid_operators[3] and y != 0:
                result = x / y
            print(result)
            ans1 = input(msg_[4])
            if ans1 == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while msg_index <= 12:
                        ans = input(msg_[msg_index])
                        if ans == 'y':
                            msg_index += 1
                        else:
                            break
                    if msg_index > 12:
                        memory = result
                else:
                    memory = result
            ans2 = input(msg_[5])
            if ans2 == 'y':
                continue
            else:
                break
    except ValueError:
        print(msg_[1])
        continue
    break
