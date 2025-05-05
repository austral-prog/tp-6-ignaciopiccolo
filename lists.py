def remove_elements(list_to_remove_elements):
    # Crear una copia para no modificar la original
    result = list_to_remove_elements[:]
    # Eliminar el sexto, luego quinto, luego primero (en orden inverso para no cambiar índices antes)
    for index in sorted([0, 4, 5], reverse=True):
        if index < len(result):
            result.pop(index)
    return result

def add_elements(list_to_add_elements):
    result = list_to_add_elements[:]  # copia para no modificar la original
    result.insert(0, 'Pink')
    result.append('Yellow')
    return result

def is_empty(list_to_check):
    return len(list_to_check) == 0

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    return list_to_compare1[2] == list_to_compare2[2]

def list_of_lists(list_of_lists_to_modify):
    result = []
    if len(list_of_lists_to_modify) >= 1:
        result.append(list_of_lists_to_modify[0][:2])
    if len(list_of_lists_to_modify) >= 2:
        result.append(list_of_lists_to_modify[1][1:4])
    if len(list_of_lists_to_modify) >= 3:
        result.append(list_of_lists_to_modify[2][-2:])
    return result

