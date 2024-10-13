def lista_de_la_compra(menu):
    """
    Recibe un diccionario ('menú') que contiene cada plato como clave, con su correspondiente lista de ingredientes como valores,
    y devuelve una lista ('lista de la compra') con los ingredientes necesarios.
    En caso de recibir dos veces el mismo ingrediente, lo incluye una sola vez en la lista.
    Si no recibe un diccionario, devuelve un error.
    """    
    # Defino variables; en este caso, solo necesito definir la lista vacía en la que se irán incluyendo los ingredientes. 
    # Me curo en salud e incluyo algún mensaje de error.
    # Iteración: recorro las claves del diccionario 'menú'.   
    # A continuación, recorro las listas que constituyen los valores de dichas claves. 
    # Incluyo los elementos de las listas en lista_de_la_compra, en caso de que no estén ya incluidos.

    lista_compra = []

    if type(menu) != dict:
        return f"Error: '{menu}' no es un diccionario"

    for receta in menu:                               # recorro las claves
        for ingrediente in menu[receta]:                  # diccionario[clave] = valor; como en este caso son listas, los puedo recorrer.
            if ingrediente not in lista_compra:
                lista_compra.append(ingrediente)
                
    return lista_compra

menu_comida = {"Guacamole": ["cilantro fresco", "cebolla", "chile fresco", "ajo", "tomate", "aguacates maduros", "zumo de limón", "sal"], "Pimientos del piquillo rellenos": ["huevo duro", "palitos de cangrejo", "atún en aceite de oliva", "mayonesa", "pimientos del piquillo", "pimiento verde", "pimiento rojo", "cebolla", "vinagre de vino", "sal", "aceite de oliva virgen extra"], "Solomillo de cerdo agridulce": ["aceite de oliva", "ajo", "solomillo de cerdo", "cebolla", "manzana", "tomate concentrado", "calabacines", "brandy", "vino de Oporto", "ciruelas pasas", "orejones de albaricoque", "mostaza", "piñones tostados"], "Brownie de chocolate con helado de turrón": ["chocolate amargo 70 % cacao", "mantequilla sin sal", "azúcar", "huevos", "sal", "harina de trigo", "nueces"]}

print(lista_de_la_compra(8))
print(lista_de_la_compra(menu_comida))