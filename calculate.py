import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'circle': 1,
    'square': 1,
    'triangle': 3
}


def calc(fig, func, size):
    """
    Выводит результат вычислений в зависимости от входных данных.

    Входное значение:
        fig (string) : фигура, над которой совершается действие
        func (string) : действие
        size (string) : размер фигуры

    Выходное значение:
        * (void)
    """

    if fig not in figs:
        raise ValueError(f"Invalid figure!")

    needed_size = sizes.get(fig)

    if needed_size != len(size):
        raise ValueError(f"Invalid number of size attributes!")

    if func not in funcs:
        raise ValueError(f"Invalid function!")

    if fig == 'triangle':
        a, b, c = size
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")

    try:
        result = eval(f'{fig}.{func}(*{size})')
    except:
        raise ValueError(f"Error calculating!")

    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(fig):
        size_input = input(f"Input figure sizes separated by space, 1 for circle and square:\n")

        try:
            size = list(map(int, size_input.split(' ')))
        except ValueError:
            print("Input numbers are not valid.")
            size = []

    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
