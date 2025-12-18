from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Style

def main():
    N = 5

    rect = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(Fore.BLUE + str(rect))
    print(Fore.GREEN + str(circle))
    print(Fore.RED + str(square))
    print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
