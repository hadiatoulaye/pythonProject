# exercice3 traité

def table_return(nombre1, nombre2):

    table_return = []
    for hadia in nombre1:
        if hadia not in nombre2:
            if hadia not in table_return:
                table_return.append(hadia)
    for hadia in nombre2 :
        if hadia not in nombre1:
            if hadia not in table_return:
                table_return.append(hadia)
    return table_return
result = table_return([2, 4, 7, 8, 2], [1, 3, 9, 4, 6, 7])
print(result)
