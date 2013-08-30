import numpy

data = numpy.genfromtxt("pokemon.csv"
                        ,skip_header=1
                        ,dtype=None
                        ,delimiter=',')
print(data)

