from random import *
import turtle


class Maze:
    ens = []
    t = turtle.Turtle()

    def __init__(self, d):
        self.d = d
        for i in range(0, d*d):
            self.ens.append(-1)

    def find(self, x):
        if self.ens[x] < 0:
            return x
        else:
            return self.find(self.ens[x])

    def union(self, a, b):
        i = self.find(a)
        j = self.find(b)
        if i != j:
            if self.ens[i] <= self.ens[j]:
                self.ens[i] += self.ens[j]
                self.ens[j] = i
            else:
                self.ens[j] += self.ens[i]
                self.ens[i] = j

    def draw_line(self, x1, y1, x2, y2):
        self.t.penup()
        self.t.goto((x1, y1))
        self.t.pendown()
        self.t.goto((x2, y2))

    def print_external(self):
        self.draw_line(0, 0, self.d * 20, 0)
        self.draw_line(self.d * 20, 20, self.d * 20, self.d * 20)
        self.draw_line(self.d * 20, self.d * 20, 0, self.d * 20)
        self.draw_line(0, (self.d - 1) * 20, 0, 0)
        vs = self.t.getscreen()
        vs.mainloop()

    def print_maze(self, list):
        for t in range(0, len(list)):
            i = list[t]
            if i[1] == i[0] + 1:  # if vertical line
                self.draw_line((i[1] % self.d) * 20, (self.d - (i[1] // self.d)) * 20, (i[1] % self.d) * 20,
                               ((self.d - (i[1] // self.d) - 1) * 20))
            else:
                self.draw_line((i[0] % self.d) * 20, (self.d - (i[1] // self.d) - 1) * 20 + 20, (i[0] % self.d + 1) * 20,
                               ((self.d - (i[1] // self.d) - 1) * 20) + 20)
        self.print_external()


def construct_optional_union_list(d):
    l = []
    for i in range(0, d*d):
        right, bottom = True, True
        if(i + 1) % d == 0:
            right = False
        if i in range(d * (d-1), d**2):
            bottom = False
        if right:
            l.append([i, i + 1])
        if bottom:
            l.append([i, i + d])
    return l


d = 14
m = Maze(d)
optional_union_values = construct_optional_union_list(d)
while len(optional_union_values) != 0:
    if m.ens[m.find(0)] == -d**2 or m.find(0) == m.find(d**2 - 1):
        break
    r = randint(0, len(optional_union_values) - 1)
    m.union(optional_union_values[r][0], optional_union_values[r][1])
    optional_union_values.pop(r)
m.print_maze(optional_union_values)