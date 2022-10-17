# Напишите программу вычисления арифметического выражения заданного строкой.\
# Используйте операции +, -, /, *.приоритет операций стандартный.
# *Пример: *'15 * 6 - 80 / 4' = > 8.5
import math

mult = lambda x, y: float(x) * float(y)
div1 = lambda x, y: round(float(x) / float(y), 2)
plus = lambda x, y: float(x) + float(y)
minus = lambda x, y: float(x) - float(y)

def f(op, x,y):
    return op(x,y)

evaluation = '15 * 6 - 80 / 4'
eval_lst = evaluation.split()
res = 0
i = 1
while len(eval_lst) > 2:
    while '*' in eval_lst or '/' in eval_lst:
        print(i, eval_lst)
        if eval_lst[i] == '*' or eval_lst[i] == '/':
            x = eval_lst[i - 1]
            y = eval_lst[i + 1]
            if eval_lst[i] == '*':
                res = f(mult, x, y)
            elif eval_lst[i] == '/':
                res = f(div1, x, y)
            eval_lst[i] = str(res)
            eval_lst.pop(i + 1)
            eval_lst.pop(i - 1)
            i = 0
            continue
        else:
            i += 1
    if '*' not in eval_lst or '/' not in eval_lst:
        i = 1
        while '+' in eval_lst or '-' in eval_lst:
            print(i, eval_lst)
            if eval_lst[i] == '+' or eval_lst[i] == '-':
                x = eval_lst[i - 1]
                y = eval_lst[i + 1]
                if eval_lst[i] == '+':
                    res = f(plus, x, y)
                elif eval_lst[i] == '-':
                    res = f(minus, x, y)
                eval_lst[i] = str(res)
                eval_lst.pop(i + 1)
                eval_lst.pop(i - 1)
                i = 0
                continue
            else:
                i += 1
    if '+' not in eval_lst or '-' not in eval_lst:
        break
print(res)