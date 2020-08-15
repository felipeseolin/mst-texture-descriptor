from skimage import io
from igraph import plot


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
