from igraph import Graph


def image_to_graph(img, neighborhood=8):
    if neighborhood == 8:
        return image_to_graph_neighborhood_eight(img)
    elif neighborhood == 4:
        return image_to_graph_neighborhood_four(img)
    else:
        return Graph()


def image_to_graph_neighborhood_four(img):
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

            acc += 1

    g = Graph(vertices)
    g.vs['value'] = vertices_value
    g.es['weight'] = weights
    return g


def image_to_graph_neighborhood_eight(img):
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


def image_to_mst(image):
    g = image_to_graph(image)
    return g.spanning_tree(weights=g.es['weight'], return_tree=True), g
