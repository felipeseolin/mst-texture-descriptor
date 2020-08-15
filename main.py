from layout import *
from image_to_graph import *


def main():
    image = open_image('new.jpg')
    g = image_to_graph(image)
    mst = g.spanning_tree(weights=g.es['weight'], return_tree=True)
    show_graph_and_mst(g, mst)


def open_image(filename):
    return io.imread(filename)


if __name__:
    main()
