def lista_de_la_compra_borrador (menu):
    
    # BORRADOR
    # ------------------
    # COSAS A RESOLVER:

    # Tengo que incluir el nombre del plato, con lo cual debo meter una nueva capa de diccionarios.
    # Hay que resolver cómo se pueden incluir las unidades de medida en este diccionario 
    # o me podría ver de pronto con 500 solomillos de cerdo en la cocina, en lugar de con 500g.
    # Tal vez sea necesario crear una nueva capa de diccionarios que recoja la unidad de medida y la cantidad: 
    #                   {"Solomillo a la pimienta":{"Solomillo": {"gramos": 500}}}.
    # Lo veo demasiado farragoso...

    # También puedo hacer que el valor de la segunda capa de diccionarios sea una lista, 
    # de la cual extraemos, por un lado, los enteros (para sumarlos si se trata de un ingrediente repetido),
    # y, por otro, una cadena con la unidad de medida:
    #                    {"Solomillo a la pimienta": {"solomillo":[500, "gramos"]}}
    # También farragoso. Vaya lío. 
    
    # Defino la variable  'lista_de_la_compra' (un diccionario vacío, que pueda recibir los ingredientes y las cantidades).
    # Recorro y almaceno las claves de la lista de diccionarios 'menú' en 'lista_de_la_compra'.   

    # A continuación, recorro los valores de dichas claves y los almaceno también en 'lista_de_la_compra'; 
    # si ya ha aparecido la clave, simplemente le sumo el valor.

    lista_de_la_compra = {}

    for receta in menu:
        for ingrediente in receta:
            if ingrediente in lista_de_la_compra:
                lista_de_la_compra[ingrediente] = lista_de_la_compra[ingrediente] + receta[ingrediente]
            else:
                lista_de_la_compra[ingrediente]=receta[ingrediente]
    
    return lista_de_la_compra

menu_comida = [{"solomillo": 500, "brandy": 30, "calabacín": 600}, {"solomillo": 100, "ajo": 5}, {"chocolate":300, "ajo":4}, {"ajo":3, "puerro":1, "cebolla": 3}]

print(lista_de_la_compra_borrador(menu_comida))