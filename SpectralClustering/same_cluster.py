def same_cluster(a,b, graph, attr, label):
    query_1 = "MATCH (a:" + str(label) + " {name: '" + str(a) + "'})"
    query_2 = "RETURN a." + str(attr)
    query = query_1 + query_2
    clusta = graph.run(query).to_data_frame().values[0][0]

    query_3 = "MATCH (b:" + str(label) + " {name: '" + str(b) + "'})"
    query_4 = "RETURN b." + str(attr)
    query = query_3 + query_4
    clustb = graph.run(query).to_data_frame().values[0][0]

    if clusta == clustb:
        diffclust = 0
    else:
        diffclust = 1

    return diffclust
