import types

def load_choice(owner_node, data):
    return globals().get(
        data.get('class', 'BaseChoice'),
        BaseChoice
    )(owner_node, data)

class BaseChoice:
    def __init__(self, owner_node, data=None):
        self.owner_node = owner_node
        self.name = data.get('name', '???')
        self.leads_to = data.get('leads_to', None)
        self.parser_choices = data.get('contains_any', None)

        if isinstance(self.parser_choices, str):
            self.parser_choices = [
                x.strip() for x in self.parser_choices.split(',')
            ]
        else:
            try:
                self.parser_choices = [x.strip().lower() for x in self.parser_choices]
            except TypeError:
                self.parser_choices = None

    def interpret(self, received):
        if self.parser_choices is None:
            return (False, None)

        result = any(x in received.lower() for x in self.parser_choices)
        return (
            result,
            self.leads_to if result else None,
        )

    def __str__(self):
        return self.name