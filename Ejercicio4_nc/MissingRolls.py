#4. You have observations of $n + m$ 6-sided dice rolls with
#each face numbered from $1$ to $6$. $n$ of the observations went missing,
#and you only have the observations of $m$ rolls. Fortunately, you have also calculated
#the average value of the $n + m$ rolls.
#You are given an integer array rolls of length m where  roll[i] is the value of ith the  observation.
#You are also given the two integers  mean and n.
#Return an array of length n  containing the missing observations such that the average value of the n+m rolls is
#exactly mean .If there are multiple valid answers, return any of them. If no such array exists, return an empty
# array
#The average value of a set of k numbers is the sum of the numbers divided by k.
#Note that mean is an integer, so the sum of the n+m rolls should be divisible by n+m .
import sys



def MissingRolls( rolls, mean, n) :

    m = len(rolls)
    total = (n + m) * mean
    observed = sum(rolls)
    missed = total - observed

    if n==0 or mean==0 :
        raise ValueError ("No se permite valores de 0 en m o n")

    else:

        min_val = missed // n
        remain = missed - min_val * n
        rest_rolls = [min_val] * (n - remain) + [1 + min_val] * remain
        return rest_rolls





