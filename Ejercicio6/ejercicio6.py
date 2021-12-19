def num_of_odd_sum(arr = []):
    if len(arr)==0:
        raise ValueError("Arreglo vacío")
    index = 0
    num = 0
    while index != len(arr):
        sub_arr = []
        for j in range(index, len(arr)):
            if arr[j] < 0:
                raise ValueError("No se permiten números negativos")
            sub_arr.append(arr[j])
            sum = 0
            for k in sub_arr:
                sum +=k
            if sum %2 != 0:
                num += 1
        index += 1
    return num%(1e9 + 7)