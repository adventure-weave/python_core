from adventure_weave.choices import load_choice
from adventure_weave.nodes import load_node
from logging import getLogger

logger = getLogger()

def load_data(data):
    try:
        data.keys()
        data.values()
    except AttributeError:
        raise ValueError('Can only load objects that have key-value pairs')

    loaded_nodes = {}
    for node_title in data:
        if node_title in loaded_nodes:
            logger.warn('%s appears more than once, and has been overwritten. Make sure your titles are unique!', node_title)
        node = load_node(node_title, data[node_title])
        # TODO: keep track of choices' lead_tos
        loaded_nodes[node_title] = node
    
    return loaded_nodes

