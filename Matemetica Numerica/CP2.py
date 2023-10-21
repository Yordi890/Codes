from matplotlib import pyplot;


def squareFunc(x):
    return  0.2*(x**2)-4;

def squareFunc2(x):
    return  0.1*((x-1)**2)-4;

def func3(x):
    return ((x-2)**5)+(3/2)*(x**2)-10*x;

def derivative(func,x,h):
    return (func(x+h)-func(x-h))/(2*h);

def biseccion(a,b,func,ite):
    if func(a)*func(b)<0:
        aux=1;
        showFunc(func,a,b);
        pyplot.scatter([a,b], [func(a),func(b)], color='green', label='Puntos Biseccion');
        for _ in range(ite):
            m=(a+b)/2;
            if func(a)*func(m)<=0:
                b=m;
            elif func(b)*func(m)<=0:
                a=m;
            pyplot.scatter([a,b], [func(a),func(b)], color='green');
            aux=m;
        else:
            pyplot.legend();
            pyplot.show();
            return aux;
    raise Exception('No se puede aplicar biseccion a este intervalo');

def regulafasi(a,b,func,ite):
    if func(a)*func(b)<0:
        aux=1;
        showFunc(func,a,b);
        pyplot.scatter([a,b], [func(a),func(b)], color='green', label='Puntos Regula Fasi');
        for _ in range(ite):
            m=(func(b)*a-func(a)*b)/(func(b)-func(a));
            if func(a)*func(m)<=0:
                b=m;
            elif func(b)*func(m)<=0:
                a=m;
            aux=m;
            pyplot.scatter([a,b], [func(a),func(b)], color='green');
        else:
            pyplot.legend();
            pyplot.show();
            return aux;
    raise Exception('No se puede aplicar biseccion a este intervalo');

def secantes(a,b,func,ite):
    if func(a)*func(b)<0:
        showFunc(func,a,b);
        pyplot.scatter([a,b], [func(a),func(b)], color='green', label='Puntos Secantes');
        for _ in range(ite):
            pyplot.scatter([a,b], [func(a),func(b)], color='green');
            a,b=b,(func(b)*a-func(a)*b)/(func(b)-func(a));
        else:
            pyplot.legend();
            pyplot.show();
            return b;
    raise Exception('No se puede aplicar biseccion a este intervalo');

def newton(a,b,func,ite):
    showFunc(func,a,b);
    pyplot.scatter([a,b], [func(a),func(b)], color='green',label='Puntos Newton');
    for _ in range(ite):
        b=b-(func(b)/derivative(func,b,0.00000001));
        pyplot.scatter([b], [func(b)], color='green');
    else:
        pyplot.legend();
        pyplot.show();
        return b;

def showFunc(func,a,b):
    puntos_x =[i for i in range(a,b+1)];
    puntos_y = [func(x) for x in puntos_x];

    pyplot.plot(puntos_x, puntos_y, label='Función');
    pyplot.scatter(puntos_x, puntos_y, color='red', label='Puntos');

    pyplot.xlabel('Eje X');
    pyplot.ylabel('Eje Y');
    pyplot.title('Gráfico de Función y Puntos');
    
def pointsX(func):
    showFunc(func, -10, 10);
    extremos = [];
    a=10;
    b=-10;
    for _ in range(10): 
        a = a - (func(a) / derivative(func, a, 0.00000000001));
        b = b - (func(b) / derivative(func, b, 0.00000000001));
    extremos.append(a);
    extremos.append(b);
        
    pyplot.scatter(extremos, [func(e) for e in extremos], color='green', label='Puntos extremos');
    pyplot.legend();
    pyplot.show();

    return extremos;


print(biseccion(1,6,squareFunc,70));
print(regulafasi(1,6,squareFunc,10));
print(secantes(1,6,squareFunc,5));
print(newton(1,12,squareFunc2,5));
print(pointsX(func3));