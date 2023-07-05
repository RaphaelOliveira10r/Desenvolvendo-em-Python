"""Faça um programa, com uma função que necessite de um argumento.
 A função retorna o valor de caractere "P",
 se seu argumento for positivo, e "N", se seu argumento for zero ou negativo."""


def func(x):
    if x > 0:
        print("P")
    else:
        print("N")


func(1)
func(0)
func(-1)