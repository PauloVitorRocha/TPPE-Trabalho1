from activity_diagram import ActivityDiagram


if __name__ == "__main__":
    opt = input("Deseja criar um novo Diagrama de Atividades (s/n): ")

    if opt[0].lower() == "s":
        name = input("Nome do Diagrama: ")
        act = ActivityDiagram(name)
