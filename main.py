from skimage import io
from igraph import *


def main():
    image = open_image('new.jpg')
    g = image_to_graph(image)
    mst = g.spanning_tree(weights=g.es['weight'], return_tree=True)
    show_graph_and_mst(g, mst)


def open_image(filename):
    return io.imread(filename)


def show_image(image):
    io.imshow(image)
    io.show()


def show_graph(graph):
    layout_graph = graph.layout('auto')
    plot(graph, layout=layout_graph, bbox=(300, 300), margin=20)


def show_full_graph(graph):
    graph = graph_layout(graph)
    show_graph(graph)


def graph_layout(graph):
    number_edges_by_node = calc_number_edges_by_node(graph)
    color_dict = {
        1: 'black',
        2: 'gray',
        3: 'blue',
        4: 'green',
        5: 'yellow',
        6: 'orante',
        7: 'pink',
        8: 'red',
    }
    graph.vs['label'] = graph.vs['value']
    graph.vs['color'] = [color_dict[number] for number in number_edges_by_node]
    graph.es['label'] = graph.es['weight']
    return graph


def show_graph_and_mst(graph, mst):
    graph = graph_layout(graph)
    color_dict = dict.fromkeys(mst.get_edgelist(), 'red')
    graph.es['color'] = [color_dict[i] if i in color_dict else 'black' for i in graph.get_edgelist()]
    show_graph(graph)


def show_simple_graph(graph):
    graph.vs['label'] = graph.vs['value']
    graph.es['label'] = graph.es['weight']
    layout2 = graph.layout('auto')
    plot(graph, layout=layout2, bbox=(300, 300), margin=20)


def calc_number_edges_by_node(graph):
    number_edges_by_node = [0] * graph.vcount()
    for (v1, v2) in graph.get_edgelist():
        number_edges_by_node[v1] += 1
        number_edges_by_node[v2] += 1

    return number_edges_by_node


def image_to_graph(img):
    y, x = img.shape
    acc = 0
    vertices = []
    vertices_value = []
    weights = []

    for pos_i, i in enumerate(img):
        for pos_j, j in enumerate(i):
            vertices_value.append(j)
            # horizontal
            if pos_j + 1 != len(i):
                vertices.append((acc, acc + 1))
                weights.append(calc_edge_weight(j, i[pos_j + 1]))
            # vertical
            if pos_i + 1 != y:
                vertices.append((acc, acc + x))
                weights.append(calc_edge_weight(j, img[pos_i + 1][pos_j]))
            # diagonal direita
            if pos_j + 1 != len(i) and pos_i + 1 != y:
                vertices.append((acc, acc + x + 1))
                weights.append(calc_edge_weight(j, img[pos_i + 1][pos_j + 1]))
            # diagonal esquerda
            if pos_j != 0 and pos_i + 1 != y:
                vertices.append((acc, acc + x - 1))
                weights.append(calc_edge_weight(j, img[pos_i + 1][pos_j - 1]))

            acc += 1

    g = Graph(vertices)
    g.vs['value'] = vertices_value
    g.es['weight'] = weights
    return g


def calc_edge_weight(val1, val2):
    return abs(int(val1) - int(val2))


if __name__:
    main()
