# Solution force brute - Recherche de toutes les solutions
def sac_a_dos_force_brute(capacite, elements, elements_selection=None):
    if elements_selection is None:
        elements_selection = []
    if elements:
        val1, lst_val1 = sac_a_dos_force_brute(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lst_val2 = sac_a_dos_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lst_val2

        return val1, lst_val1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection


# Nom
# poids
# Valeur
ele = [('Montre à gousset', 2, 6),
       ('Boule de bowling', 3, 10),
       ('Portrait de tata Germaine', 4, 12)]

print('Algo force', sac_a_dos_force_brute(5, ele))


def read_shares():
    with open('test_shares.csv') as csv:
        pass
