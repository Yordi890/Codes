"""
Clase Práctica # 4
Autor: Lázaro Hernández Pérez
"""

from numpy import diff, all

def xdistant(lista):
    # Calcula las diferencias entre elementos adyacentes.
    diferencias = diff(lista)
    return all(diferencias == diferencias[0])


def trapezoid_method(Xs, Ys):
    assert len(Xs) == len(
        Ys), "Las listas de los valores para x e y tienen una cantidad diferente de valores"
    xdist = xdistant(Xs)
    result = 0.0
    if not xdist:
        for i in range(len(Xs)-1):
            result += (Xs[i+1]-Xs[i])*((Ys[i+1]+Ys[i])/2)
    else:
        result = (Xs[1]-Xs[0])*(sum(Ys)-(Ys[0]/2.0)-(Ys[-1]/2.0))

    return abs(result)


def simpson_method(Xs, Ys):
    assert len(Xs) == len(
        Ys), "Las listas de los valores para x e y tienen una cantidad diferente de valores"
    assert (len(Xs)-1) % 2 == 0 and len(Xs)!=1 , "No existe una cantidad par de subintervalos"
    sum = Ys[0]+Ys[len(Ys)-1]
    for i in range(len(Ys)):
        if i != 0 and i != len(Ys)-1:
            mul = 4
            if i % 2 == 0:
                mul = 2
            sum += mul*Ys[i]
    return abs(((Xs[1]-Xs[0])/3)*sum)


if __name__ == "__main__":
    print(trapezoid_method([0, 10, 20, 30, 40, 50, 60],
          [3.7, 3.0, 2.5, 2.0, 1.7, 1.4, 1.1]))
    print(simpson_method([0, 10, 20, 30, 40, 50, 60],
          [3.7, 3.0, 2.5, 2.0, 1.7, 1.4, 1.1]))
    print(trapezoid_method([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
          [0, 1.5, 3.8, 5.2, 5.7, 6.2, 6.5, 6.4, 5.9, 5.9, 5.5, 3.5, 0]))
    print(simpson_method([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
          [0, 1.5, 3.8, 5.2, 5.7, 6.2, 6.5, 6.4, 5.9, 5.9, 5.5, 3.5, 0]))
