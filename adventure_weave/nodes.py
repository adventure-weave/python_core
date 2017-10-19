#!/usr/bin/env python

# from adventure_weave.loaders import load_choice
from adventure_weave.choices import load_choice

def load_node(title, data):
    return globals().get(
        data.get('class', 'BaseNode'),
        BaseNode
    )(title, data)

class BaseNode:
    '''Base functionality all nodes inherit'''
    def __init__(self, title, data=None):
        data = data or {}

        self.title = title
        self.content = data.get('content', '')
        self.choices = [
            load_choice(self, choice) for choice in (data.get('choices') or [])
        ]

    def __str__(self):
        '''Returns markdown representation of itself'''
        return '\n\n'.join([
            '# ' + self.title,
            self.content,
            '\n'.join(
                '**%s.** %s' % (x+1, choice) for (x, choice) in enumerate(self.choices)
            )
        ])