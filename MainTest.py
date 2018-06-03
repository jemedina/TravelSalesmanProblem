from Main import *

def assertThat(expected, result, strr=""):
    if expected == result:
        print(color.GREEN,"Test Ok ",color.END,strr)
    else:
        print(color.RED,"Error, expected <",expected,"> but was <",result,">")

def assertTrue(val,strr=""):
    if val == True:
        print(color.GREEN,"Test Ok ",color.END,strr)
    else:
        print(color.RED,"Error, result False ",strr,color.END)


def assertFalse(val,strr=""):
    if val == False:
        print(color.GREEN,"Test Ok ",color.END,strr)
    else:
        print(color.RED,"Error, result False ",strr,color.END)

print("=== Test initialized! ===")


print("===== Test Ruta =====")
c_origen = Ciudad(1, 2, 2)
c_destino = Ciudad(2, 4, 4)
expected = 2.828427125
ruta = Ruta(c_origen, c_destino)

assertTrue(abs(expected-ruta.distancia) < 0.001,"abs(expected-ruta.distancia) < 0.001")



print("===== Test Ciudades =====")

c = Ciudades()
expectedLength = 0
assertThat(expectedLength, len(c.ciudades),"Ciudades() constructor")

c.genCiudades2()
cd1 = Ciudad(1,5,4)
cd25 = Ciudad(25,12,8)
assertThat(str(cd1), str(c.ciudades[0]),str(cd1) + " == "+ str(c.ciudades[0]))
assertThat(str(cd25), str(c.ciudades[24]),str(cd25) + " == "+ str(c.ciudades[24]))
print("Actualizar orden: === ")
ciudadesOrig = c.ciudades
ciudadesMovido = c.actualizarOrden()
assertFalse(str(ciudadesOrig) == str(ciudadesMovido))

print("Calcular recorrido 1 : === ")
cds = [Ciudad(1,1,1)]
for i in range(2,26):
    cds.append(Ciudad(i,i,i))
cds.append(Ciudad(1,1,1))
expectedReco = 1.4142135623730951*24 + 33.94112549695428
reco = c.calcularRecorrido(cds)
dist = abs(reco - expectedReco)
assertTrue(dist < 0.000001)

print("Calcular recorrido 2 : === ")
cds = [Ciudad(1,1,1),Ciudad(2,1,2),Ciudad(3,2,2),Ciudad(4,2,1),Ciudad(1,1,1)]
expectedReco = 4
reco = c.calcularRecorrido(cds,4)
dist = abs(reco - expectedReco)
assertTrue(dist < 0.0001)