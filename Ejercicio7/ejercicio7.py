from itertools import combinations

def num_of_arths(nums = []):
    if len(nums) < 3:
        raise ValueError("Arreglo vacío")
    num_of_as = 0
    for elements in range(3, len(nums)+1):
        c = list(combinations(nums, elements))
        for sub_seq in c:
            i = 0
            while i < len(sub_seq) - 2:
                is_as = True
                if sub_seq[i+1] - sub_seq[i] != sub_seq[i+2] - sub_seq[i+1]:
                    is_as = False
                    break
                i += 1
            if is_as:
                num_of_as += 1
    return num_of_as