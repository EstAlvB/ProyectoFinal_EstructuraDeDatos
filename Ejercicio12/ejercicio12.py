import math

def create_coords(num_of_rows):
    queue = [(0, 0)]
    coords = []
    while queue:
        t = queue.pop(0)
        coords.append(t)
        d = [(t[0]-1, t[1]+1), (t[0]+1, t[1]+1)]
        for dir in d:
            if dir[1] < num_of_rows:
                queue.append(dir)
    return coords

def vertical_traverse_tree(root = []):
    num_of_rows = round(math.log(len(root)+1)/math.log(2))
    if 2**num_of_rows != len(root)+1:
        raise ValueError("Longitud del arreglo inválida")
    if len(root) == 0:
        raise ValueError("Arreglo vacío")
    coords = create_coords(num_of_rows)
    dic, keys, vtt = {}, [], []
    for index, num in enumerate(root):
        if num != None:
            if coords[index][0] not in dic.keys():
                dic[coords[index][0]] = [num]
            else:
                l = dic[coords[index][0]]
                l.append(num)
                dic[coords[index][0]] = l
            keys.append(coords[index][0])
    keys.sort()
    for key in keys:
        if dic[key] not in vtt:
            vtt.append(dic[key])
    return vtt