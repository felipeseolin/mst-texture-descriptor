from layout import *
from image_to_graph import *
from extract_values import *


def main():
    image = open_image('new.jpg')
    g = image_to_graph(image)
    mst = g.spanning_tree(weights=g.es['weight'], return_tree=True)
    values = extract_values(mst.es['weight'])


def open_image(filename):
    return io.imread(filename, as_gray=True)


if __name__:
    main()
