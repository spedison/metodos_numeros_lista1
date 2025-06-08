import math

def calculaF(x):
    return math.log(5+6*x)

def calculaP1(x):
    return math.log(5) + x * 6. / 5.

def calculaP2(p1, x):
    return p1 - (x**2 * ( 36./50.))

def calculaP3(p2, x):
    return p2 + (x**3 * (432. / 150.))

def calculaP4(p3, x):
    return p3 - (x**4 * (7776./15000.))

def executaExercicio():

    with open("../dados/exercicio1.csv", "w") as arquivo:

        for i in range(0,25000):

            val = float(i/20000.) - .5

            valFx = calculaF(val)
            valP1 = calculaP1(val)
            valP2 = calculaP2(valP1,val)
            valP3 = calculaP3(valP2,val)
            valP4 = calculaP4(valP3,val)

            str = f"{val};{valFx};{valP1};{valP2};{valP3};{valP4}\n"
            arquivo.write(str)

if __name__ == '__main__':
    executaExercicio()