import types

def load_choice(owner_node, data):
    return globals().get(
        data.get('class', 'BaseChoice'),
        BaseChoice
    )(owner_node, data)

class BaseChoice:
    '''
    Basic functionality related to choices presented to the reader.

    Note that this one has sufficient functionality on its own that for
    a simple text game (either pick a choice, or interpreter-based),
    it might not even require subclassing.
    '''
    def __init__(self, owner_node, data=None):
        '''
        Initializes the choice object with the following parameters:

        owner_node: Node object.
                    The story node this choice is attached to.
        data: dictionary (or any dict-like object that supports .get())
              It is expected to contain the following keys:
               - leads_to: name of the story node this choice leads to
              and one of the following:
               - name: if present, this attribute will be used as a label
                       that will be shown. This is useful for pick-a-choice
                       nodes.
               - contains_any: if present, it is expected to be a list of
                               strings. This assumes the parent node has
                               the 'type' input set. Any of the contains_any
                               attributes will be equivalent to the reader
                               having picked this choice.
              
        '''
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