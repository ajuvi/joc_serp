from models.Poma import Poma
from models.Serp import Serp
from ViewModel import ViewModel

#obtenir paràmetres del joc
vm = ViewModel();
tile_width = vm.tile_width;
tile_height = vm.tile_height;
imatge_poma = vm.getTile('poma');
imatge_serp = vm.getTile('serp');
direccio_serp=[1,0]

#crear un objecte de poma
poma = Poma(1,1,tile_width,tile_height,imatge_poma)
print("x_poma: ",poma.x,"y_poma: ",poma.y)

#crear un objecte de serp
serp = Serp(10,10,tile_width,tile_height,direccio_serp, imatge_serp)
print("x_serp: ",serp.x,"y_serp: ",serp.y)
