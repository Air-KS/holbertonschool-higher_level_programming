#!/usr/bin/python3
# add_0.py
if __name__ == "__main__":
    """ Affiche la somme de 1 et 2 du fichier add_0.py """
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
