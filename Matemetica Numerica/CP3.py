from matplotlib import pyplot
from numpy import linspace


def showFunc(func, a, b):
    puntos_x = [i for i in range(a, b+1)]
    puntos_y = [func(x) for x in puntos_x]
    funcx = linspace(a, b, 100)
    funcy = func(funcx)

    pyplot.plot(funcx, funcy, label='Función')
    pyplot.scatter(puntos_x, puntos_y, color='red', label='Puntos')

    pyplot.xlabel('Eje X')
    pyplot.ylabel('Eje Y')
    pyplot.title('Gráfico de Función y Puntos')


def lagrange(Xs, Ys):
    def funcAprox(x):
        Ls = 0
        for i in range(len(Xs)):
            Ln = 1
            Ld = 1
            for j in range(len(Xs)):
                if i != j:
                    Ln *= (x-Xs[j])
                    Ld *= (Xs[i]-Xs[j])
            Li = Ln/Ld
            Ls += Ys[i]*Li
        return Ls
    showFunc(funcAprox, Xs[0], Xs[-1])
    pyplot.show()
    return funcAprox


def splitDifference(Xs, Ys):
    if len(Xs) == 2:
        return (Ys[1]-Ys[0])/(Xs[1]-Xs[0])
    elif len(Xs) == 1:
        return Ys[0]
    return (splitDifference(Xs[1:], Ys[1:])-splitDifference(Xs[:-1], Ys[:-1]))/(Xs[-1]-Xs[0])


def newton(Xs, Ys):
    def funcAprox(x):
        p = Ys[0]
        for i in range(1, len(Xs)):
            f = 1
            for j in range(0, i):
                f *= (x-Xs[j])
            p += splitDifference(Xs[0:i+1], Ys[0:i+1])*f
        return p
    showFunc(funcAprox, Xs[0], Xs[-1])
    pyplot.show()
    return funcAprox


if __name__ == '__main__':

    func = lagrange([1, 2, 4], [2, 3, 1])
    print(func(2.5))
    func = newton([1, 2, 4], [2, 3, 1])
    print(func(2.5))
