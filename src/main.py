from activity_diagram import ActivityDiagram
from decision_node import DecisionStream

import os


if __name__ == "__main__":
    opt = input("Deseja criar um novo Diagrama de Atividades (s/n): ")

    if opt[0].lower() == "s":
        name = input("Nome do Diagrama: ")

        act = ActivityDiagram(name)

        while (1):
            os.system("clear")

            option = int(input(
                "-- Criação do Diagrama de Atividades --\n" +
                "1 - Inserir Elementos\n" +
                "2 - Inserir Transição\n" +
                "3 - Finalizar e Salvar\n" +
                "-> "
            ))

            if option == 1:
                start_node = input("Nome do Nó Inicial: ")
                act.create_initial_node(start_node)

                while (1):
                    os.system("clear")

                    option1 = int(input(
                        "-- Inserir Elemento no Diagrama de Atividades --\n" +
                        "1 - Atividade\n" +
                        "2 - Nó de Decisão\n" +
                        "3 - Nó de Fusão\n" +
                        "4 - Nó Final\n" +
                        "5 - Sair\n" +
                        "-> "
                    ))

                    if option1 == 1:
                        activity_name = input("Nome da Atividade: ")
                        act.elements.create_activity(activity_name)

                        # COMEÇAR AQUI O DIAGRAMA DE SEQUÊNCIA ??

                    elif option1 == 2:
                        streams = int(input("Quantidade de Fluxos: "))
                        act.elements.initiate_decision(streams)

                        for i in range(streams):
                            decision = DecisionStream()

                            while True:
                                os.system("clear")

                                option2 = int(input(
                                    "-- Criação do Fluxo de Decisão " +
                                    "{} --\n".format(i+1) +
                                    "1 - Inserir Atividade\n" +
                                    "2 - Inserir Transição\n" +
                                    "3 - Inserir Nó de Fusão / Sair\n" +
                                    "4 - Inserir Nó Final / Sair\n" +
                                    "-> "
                                ))

                                if option2 == 1:
                                    activity_name = input(
                                        "Nome da Atividade: "
                                    )

                                    decision.create_activity(activity_name)

                                elif option2 == 2:
                                    transition_name = input(
                                        "Nome da Transição: "
                                    )

                                    transition_prob = input(
                                        "Probabilidade da Transição: "
                                    )

                                    decision.create_transitions(
                                        transition_name, transition_prob
                                    )

                                elif option2 == 3:
                                    merge_name = input("Nome do Nó de Fusão: ")
                                    decision.create_merge(merge_name)

                                    break

                                elif option2 == 4:
                                    final_name = input("Nome do Nó Final: ")
                                    decision.create_final(final_name)

                                    break

                            act.elements.create_decision(decision)

                        act.elements.aux_decision()

                        # decision_node = input("Nome do Nó de Decisão: ")
                        # act.elements.create_decision(decision_node)

                    elif option1 == 3:
                        merge = input("Nome do Nó de Fusão: ")
                        act.elements.create_merge(merge)

                    elif option1 == 4:
                        final = input("Nome do Nó Final: ")
                        act.elements.create_final(final)

                    elif option1 == 5:
                        break

                    else:
                        pass

                # TODO: TRATAR SOBRESCRIÇÃO DE ELEMENTOS

            elif option == 2:
                name = input("Nome da Transição: ")
                prob = float(input("Probabilidade da Transição: "))

                act.create_transitions(name, prob)

            else:
                act.create_xml()

                # TODO: TRATAR DIAGRAMA VAZIO

                break

    else:
        print("Saindo...\n")
