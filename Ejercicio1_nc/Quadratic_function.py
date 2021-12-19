
#1. Given a sorted integer array $nums$ and three integers $a$, $b$ and $c$,
#apply a quadratic function of the form $f(x) = ax2 + bx + c$ to each element $nums[i]$
#in the array, and return the array in a sorted order

import sys


# Function to sort an array
# after applying given equation.
def sortArray(arr, A, B, C):
    #Aquí es donde pondremos la ecuación  A*x*x + B*x + C en el arreglo que tengamos.
    for i in range(len(arr)):
        arr[i] = (A * arr[i] * arr[i] +
                  B * arr[i] + C)

# Aquí usamos insertion sort para ponerlo del mas pequeno al mas grande.
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while (j >= 0) and (key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr
#def show_array():

   # sortArray(arr, A, B, C)
    #print("Arreglo despues de ordenarlo:")
    #for i in range(len(arr)):
        #print(arr[i], end=" ")


