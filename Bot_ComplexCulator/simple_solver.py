# простой вычислитель занчений +-*/ для комплексных чисел

def solver2operand(expression): # тут ждем 3 элемента в списке, из которых первый и последний - числа,
                                # а средний - операнд (просто операция над 2-мя числами)
    match expression[1]:
        case '+': return [float(expression[0][0]) + float(expression[2][0]),float(expression[0][1]) + float(expression[2][1])]
        case '-': return [float(expression[0][0]) - float(expression[2][0]),float(expression[0][1]) - float(expression[2][1])]
        case '*': return [float(expression[0][0]) * float(expression[2][0]) - float(expression[0][1]) * float(expression[2][1]), \
                          float(expression[0][1]) * float(expression[2][0]) + float(expression[0][0]) * float(expression[2][1])]
        case '/': return [(float(expression[0][0]) * float(expression[2][0]) + float(expression[0][1]) * float(expression[2][1])) / \
                          (float(expression[2][0])**2 + float(expression[2][1])**2), 
                          (float(expression[0][1]) * float(expression[2][0]) - float(expression[0][0]) * float(expression[2][1])) / \
                          (float(expression[2][0])**2 + float(expression[2][1])**2)]
        case _  : 
            print('Ошибка в выражении (1)')
            exit()
