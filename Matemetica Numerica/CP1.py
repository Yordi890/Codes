def toDecimal(number, oldBase, position=0):
    """
    Convierte un número en una base dada a su equivalente en base decimal.

    :param number: El número en la base original.
    :param oldBase: La base original del número.
    :param position: (Opcional) La posición actual en el número.
    :return: El valor del número en base decimal.
    """
    if number != 0:
        next = number // 10
        rest = number % 10
        return toDecimal(next, oldBase, position + 1) + rest * oldBase**position
    return 0

def transform(number, oldBase, newBase, position=0):
    """
    Convierte un número de una base original a una base nueva.

    :param number: El número en la base original.
    :param oldBase: La base original del número.
    :param newBase: La base a la que se desea convertir el número.
    :param position: (Opcional) La posición actual en el número.
    :return: El valor del número en la nueva base.
    """
    number=int(number);
    if number != 0:
        if oldBase != 10:
            decimalFormat = toDecimal(number, oldBase)
            return transform(decimalFormat, 10, newBase)
        next = number // newBase
        rest = number % newBase
        return transform(next, 10, newBase, position + 1) + rest * 10**position
    return 0

def contNumbers(number, approximate):
    """
    Calcula la cantidad de cifras significativas exactas en una aproximación dada.

    :param number: El número real original.
    :param approximate: La aproximación del número real.
    :return: La cantidad de cifras significativas exactas.
    """
    error = str(abs(number - approximate))
    count = 0
    for i in range(len(error)):
        if error[i] == '0':
            count += 1
        elif error[i] == '.':
            continue
        else:
            break
    return count

        
        

print(transform('0101',2,10));
print(transform(transform(52,6,3),3,6));

for i in range(1,100):
    print(temp=transform(i,10,2));

print(contNumbers(1.000303,1.0))

