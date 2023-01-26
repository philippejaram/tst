# philippe jara 1621225

import turtle as t
import random as r
import time

class teste2:
    asdf=  []
    def __init__(self):
        v = 1

class test:
    abc = []

    def __init__(self) -> None:
        pass


def ex1():
    n_sides = r.randint(3, 10)
    g = t.Turtle()
    size = 100
    if n_sides % 2 == 0:
        color = "green"
    else:
        color = "red"
    angle = 360 / n_sides
    g.down()
    g.fillcolor(color)
    g.begin_fill()
    iter = 0
    g.fd(size)
    while iter < n_sides - 1:
        g.right(angle)
        g.fd(size)
        iter += 1
    g.end_fill()
    time.sleep(2)

    return


def ex2():
    num = r.randint(1, 10)
    print(f"tabuada {num}")
    for el in range(1, 11):
        print(f"\t{num} * {el} = {num*el}")
    print(f"tabuada de (1,{num}(")
    for num in range(1, num):
        print(f"\ttabuada {num}")
        for el in range(1, 11):
            print(f"\t\t{num} * {el} = {num*el}")

    return


def ex3():
    g1 = t.Turtle()
    g2 = t.Turtle()
    g1.color("blue")
    g2.color("red")
    g1.up()
    g2.up()
    g1.setpos(-300, +40)
    g2.setpos(-300, +20)
    g1.down()
    g2.down()
    while (g1.pos()[0] < -300 + 500) and (g2.pos()[0] < -300 + 500):
        roll = r.randint(1, 6)
        g1.fd(roll)
        roll = r.randint(1, 6)
        g2.fd(roll)
    if g1.pos()[0] >= -300 + 500:
        print(f"bldue is the winner")
    else:
        print(f"red is the winner")
    time.sleep(2)

    return


# ex3()


def ex4():
    iter = 0
    user = 0
    machine = 0

    for iter in range(0, 9):

        hp = int(input("Qtd de dedos:"))
        hc = r.randint(0, 10)
        print(f"user levantou {hp} dedos, machine {hc} dedos")
        if (hp + hc) % 2 == 0:
            machine += 1
            print("machine ganhou round")
        else:
            user += 1
            print("user ganhou round")

    if user > machine:
        winner = "user"
    elif user == machine:
        winner = "draw"
    else:
        winner = "machine"
    print(f"vencedor foi {winner}")
    return


ex1()
print("TABUADAS")
ex2()
ex3()
print("PAR OU ÍMPAR:")
ex4()
