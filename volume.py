def cube(side):
    return side ** 3

def cylinder(r, h):
    return 22/7*r*r*h

if __name__ == "__main__":
    print(f'cube(2) = {cube(2)}')
    print(f'cylinder(1, 10)={cylinder(1, 10)}')