#This is a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:
    def __init__(self):
        #inicializamos las listas de ambas pilas
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        #para la segunda  pila que ayudará con el valor mínimo
        #si la lista min_stack está vacía, se añade el elemento, sino, se añade el elemento más pequeño
        #minimo ente el nuevo valor a meter y el tope de la pila
        if not self._min_stack:
            self._min_stack.append(val)
        else:
            self._min_stack.append(min(val, self._min_stack[-1]))

    def pop(self) -> None:
        if not self._stack:
            raise IndexError('pop from an empty stack')
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        if not self._stack:
            raise IndexError('top from an empty stack')
        return self._stack[-1]

    def getMin(self) -> int:
        if not self._min_stack:
            raise IndexError('getmin from an empty stack')
        #se regresa el elemento más pequeño de la pila, o sea el que está ultimo en la lista
        return self._min_stack[-1]

