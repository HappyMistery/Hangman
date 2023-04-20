import random

#Lists
llista_paraules = [
    "ordinador", "cotxe", "llibre", "xocolata", "plat", "motxila", "mascareta", "flor", "laboratori", "promesa", "terrassa",
    "estanteria", "jersei", "ulleres", "enciam", "endoll", "tovallola", "sabates", "taula", "teclat", "bufanda", "videojoc",
    "gos", "edifici", "biologia", "gol", "butxaca", "cabells", "baca", "vaca", "beca", "cavall", "flauta", "centenari", "xop",
    "rentadora", "disfressa", "diari", "musculatura", "aigua", "pelatge", "perenne", "iogurt", "horari", "esclops", "carruatge",
    "gelat", "caca", "cul", "pet", "pis", "escrot", "persona", "extintor", "falç", "infermera", "llauna", "hipopotomonstroesquipedaliofobia",
    "supercalifragilisticoespialidoso", "esternocleidomastoidal", "desoxiribonucleic"
]

#Classes
class paraula:
    def word_picking(self, list):
        num = random.randint(0, len(llista_paraules)-1)
        pick = llista_paraules[num]
        return pick

    def n_char(self, pick):
        spaces = ""
        for letter in pick:
            spaces+=("_")
        return spaces
    
    def num_lletres(self, pick):
        total = 0
        for letter in pick:
            total+=1
        return total