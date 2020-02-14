from igraph import *

img = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# img = [
#     [0, 1, 2, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]

y, x = 3, 3
size = y * x
acc = 0
vertices = []
weights = []

for pos_i, i in enumerate(img):
    for pos_j, j in enumerate(i):
        # horizontal
        if pos_j + 1 != len(i):
            vertices.append((acc, acc + 1))
            weights.append(j - i[pos_j + 1])
        #vertical
        if pos_i + 1 != y:
            vertices.append((acc, acc + x))
            weights.append(j - img[pos_i + 1][pos_j])
        # diagonal direita
        if pos_j + 1 != len(i) and pos_i + 1 != y:
            vertices.append((acc, acc + x + 1))
            weights.append(j - img[pos_i + 1][pos_j + 1])
        #diagonal esquerda
        if pos_j != 0 and pos_i + 1 != y:
            vertices.append((acc, acc + x - 1))
            weights.append(j - img[pos_i + 1][pos_j - 1])

        acc += 1

g = Graph(vertices)
g.es['weight'] = weights
print(vertices)
print(weights)
print(g.es[0].attributes())
# print(len(vertices))

# g = Graph(vertices)
#
# layout = g.layout("kk")
# plot(g, layout=layout, bbox=(300, 300), margin=20)

# summary(g)
