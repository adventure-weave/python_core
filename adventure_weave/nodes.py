#!/usr/bin/env python

# from adventure_weave.loaders import load_choice
from adventure_weave.choices import load_choice

def load_node(id, data):
    return globals().get(
        data.get('class', 'BaseNode'),
        BaseNode
    )(id, data)

class BaseNode:
    '''Base functionality all nodes inherit'''
    def __init__(self, id, data=None):
        data = data or {}

        self.id = id
        self.title = data.get('title', id)
        self.content = data.get('content', '')
        self.choices = [
            load_choice(self, choice) for choice in (data.get('choices') or [])
        ]

    def __str__(self):
        '''Returns markdown representation of itself'''
        paragraphs = ['# ' + self.title] if self.title else []
        paragraphs += [
            self.content,
            '\n'.join(
                '**%s.** %s' % (x+1, choice) for (x, choice) in enumerate(self.choices)
            )
        ]
        return '\n\n'.join(paragraphs)