import math

def rectangle(w, h):
    """calculate rectangle area

    Args:
        w (float): width
        h (float): height

    Returns:
        float: rectangle area
    """
    return w*h

def triangle(w: float, h: float)->float:
    """triangle area

    Args:
        w (float): width
        h (float): height

    Returns:
        float: triangle area
    """
    return .5*w*h

def circle(r: float)->float:
    return math.pi * r * r
    
if __name__ == "__main__":
    print(f'rectangle area = {rectangle(5, 10)}')
    print(f'triangle area =  {triangle(5, 10)}')