from models.Poma import Poma
from models.Serp import Serp

#crear un objecte de poma
poma = Poma(1,1,10,10,None)
#mostrar dades de la poma
print("x_poma: ",poma.x)
print("y_poma: ",poma.y)

#posicionar la poma en la posició (9,9)
poma.moure(9,9)
print("x_poma: ",poma.x)
print("y_poma: ",poma.y)
