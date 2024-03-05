
from modules.smartphone import Smartphone
from modules.grass import LawnGrass

def main():
    smartphone = Smartphone('iPhone', 'Smartphone description', 1000, 5, 'iPhone X')
    print(smartphone)

    lawn_grass = LawnGrass('Grass', 'Lawn grass description', 20, 100, 'Ryegrass')
    print(lawn_grass)

if __name__ == "__main__":
    main()
