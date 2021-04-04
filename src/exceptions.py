class ActivityDiagramRuleException(Exception):
    def __init__(self, msg='Necessario a criacao de um no inicial e um no final, nada mais e nada menos', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

