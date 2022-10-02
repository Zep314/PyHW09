# обработка очереди из чисел и операндов

from simple_solver import solver2operand

def get_operand_index(expression,op): # возвращаем первый сначала списка индекс элемента op
    try:
        return expression.index(op)
    except ValueError: # а вот тут not op in expression
        return -1

def iterator(expression): # тут обрабатываем список элементов выражения
    if expression[0] == '-': expression.insert(0,'0') # это если в первое число в выражении отрицательное
    match len(expression):
        case 0: return []            # такого не должно быть, но все же...
        case 1: return expression    # такого не должно быть, но все же...
        case 2: return expression[0] # такого не должно быть, но все же...
        case 3: return [solver2operand(expression)] # тут все просто - 3 элемента - просто считаем их
        case _: 
            mypos = get_operand_index(expression,')') # ищем закр. скобку
            if mypos == -1: # скобок нет!

                # вот тут вычисляем приоритеты
                mypos = get_operand_index(expression,'*') 
                if mypos == -1 or \
                   ((get_operand_index(expression,'/') < mypos)       # умножение и деление - равны по приоритету
                   and get_operand_index(expression,'/') > -1):       # но, тут вычисляем, кто из */ стоит первым 
                            mypos = get_operand_index(expression,'/') # вот прям до сюда вычисляем...

                if mypos == -1: mypos = get_operand_index(expression,'-') # если */ не нашли - то + или -
                if mypos == -1: mypos = get_operand_index(expression,'+')

                if mypos > -1:
                    # !!!!!!!!!! тут solver2operand - возвращает строку. Надо, чтобы возвращал один элемент списка,
                    # и обрабатывать его
                    expression[mypos-1] = solver2operand(expression[mypos-1:mypos+2])      # вычисляем операцию
                                                                                           # с наивысшим приоритетом 
                                                                                           # результат пишем в ячейку
                                                                                           # первого операнда 
                    del expression[mypos:mypos+2]  # удаляем из списка операцию и второй операнд
                    return expression
            else: # обработка скобок
                open_bracket = mypos # ищем откр. скобку - берем сначала позицию закр. скобку
                for i in range(mypos,-1,-1): # идем от закр. скобки назад, пока не надем откр. скобку
                    if expression[i] == '(':
                        open_bracket = i # типа нашли
                        break
                
                # делим список на 3 куска
                expr1 = expression[0:open_bracket] # то, что до откр. скобки
                expr3 = expression[mypos+1:] # то, что после закр. скобки

                expr2 = iterator(expression[open_bracket+1:mypos]) # а вот середину без скобок - засовываем
                                                                   # сами в себя (оно там само разберется, что к чему) 
                expression = [] # восстанавливаем наш бедный список

                if len(expr1) > 0: expression.extend(expr1) # вдруг впереди только одна скобка и была 
                expression.extend(expr2)
                if len(expr3) > 0: expression.extend(expr3) # вдруг позади только одна скобка и была
                return expression

# обработчик очереди выражения
def queue_handler(expression):
    while len(expression)>1: # должен остаться один элемент в списке - ответ
        expression = iterator(expression) # за одну итерацию вычисляем одно действие, в соответствии с приоритетами
    return expression
