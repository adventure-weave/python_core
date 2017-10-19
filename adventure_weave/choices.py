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

    def __str__(self):
        return self.name