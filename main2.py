#exercice2 traité
def chaine_caractere (ch = "alpha", ch2 = "mamadou"):
    m = []
    for i in ch:
        for j in ch2:
            if i == j:
                if i not in m:
                    m.append(i)
    print(m)
    return m
chaine_caractere()


def chaine_caractere (ch = "klbc", ch2 = "kaba"):
    hadia = []
    for i in ch:
         for j in ch2:
             if i == j:
                if i not in hadia:
                    hadia.append(i)
    print(hadia)
    return hadia
chaine_caractere()

