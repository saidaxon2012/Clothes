clothes = input("Qanday kiyim olisiz?\n>>> ")
men = 'erkak'
women = 'ayol'
children = 'bolalar'
man = 'Svitra - 185000\nShim - 112000\nFutbolka - 456000\nKastyum - 890000'
woman = 'Ko`ylak - 67000\nYubka - 23000\nShlyapa - 34000'
child = 'Nimcha - 45000\nIshton - 34000\nKalgotka - 12000'
if clothes == men:
    print(f"Erkaklar uchun kiyimlar:\n{man}")
elif clothes == women:
    print(f"Ayollar uchun kiyimlar:\n{woman}")
elif clothes == children:
    print(f"Bolalar uchun kiyimlar:\n{child}")