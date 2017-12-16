from graph import Graph


def main():
    """with open('graph.py') as srcfile:
        for line in srcfile:
            if line.strip():
                print(line)
"""
    # d = Debug()
    # print(repr(d))

    g = Graph()
    g.create_matrix(2, 4)

    print(repr(g))

    quit()


if __name__ == "__main__":
    main()
