from skimage import data, io, filters
from skimage.color import rgb2gray
from igraph import *


def main():
    image = data.astronaut()
    img_gray = rgb2gray(image)
    g = image_to_graph(img_gray)

    # io.imshow(img_gray)
    # io.show()


def image_to_graph(img):
    y, x = img.shape
    acc = 0
    vertices = []
    weights = []

    for pos_i, i in enumerate(img):
        for pos_j, j in enumerate(i):
            # horizontal
            if pos_j + 1 != len(i):
                vertices.append((acc, acc + 1))
                weights.append(calc_edge_weight(j, i[pos_j + 1]))
            #vertical
            if pos_i + 1 != y:
                vertices.append((acc, acc + x))
                weights.append(calc_edge_weight(j, img[pos_i + 1][pos_j]))
            # diagonal direita
            if pos_j + 1 != len(i) and pos_i + 1 != y:
                vertices.append((acc, acc + x + 1))
                weights.append(calc_edge_weight(j, img[pos_i + 1][pos_j + 1]))
            #diagonal esquerda
            if pos_j != 0 and pos_i + 1 != y:
                vertices.append((acc, acc + x - 1))
                weights.append(calc_edge_weight(j, img[pos_i + 1][pos_j - 1]))

            acc += 1

    g = Graph(vertices)
    g.es['weight'] = weights
    summary(g)
    path = g.get_all_shortest_paths(0)
    return g


def calc_edge_weight(val1, val2):
    return val1 - val2


if __name__:
    main()
