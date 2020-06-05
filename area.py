def rectangle(w, h):
    return w*h

def triangle(w, h):
    return 1/2*w*h

if __name__ == "__main__":
    print(f'rectangle area = {rectangle(5, 10)}')
    print(f'triangle area =  {triangle(5, 10)}')