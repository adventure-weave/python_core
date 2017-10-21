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
    start_node = None
    node_connections = set()
    for node_id in data:
        if node_id in loaded_nodes:
            logger.warn('%s appears more than once, and has been overwritten. Make sure your IDs are unique!', node_id)

        node = load_node(node_id, data[node_id])
        if node.is_start:
            if start_node:
                raise ValueError('Multiple starting points found, at the very least: %s and %s' % (start_node, node.id))
            start_node = node.id
        loaded_nodes[node_id] = node
        [node_connections.add(x.leads_to) for x in node.choices]
    
    if not start_node:
        possible_starts = set(loaded_nodes.keys()) - node_connections
        if len(possible_starts) != 1:
            raise ValueError('Cannot determine the start of adventure. Possible options are: ' + ', '.join(
                repr(x) for x in possible_starts
            ))
        start_node = possible_starts.pop()

    return start_node, loaded_nodes

