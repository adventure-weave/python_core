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

    input_types = {'pick', 'type'}

    def __init__(self, id, data=None):
        data = data or {}

        self.id = id
        self.title = data.get('title', id)
        self.content = data.get('content', '')
        self.input = data.get('input', 'pick')

        if self.input not in self.input_types:
            self.input = 'pick'

        self.choices = [
            load_choice(self, choice) for choice in (data.get('choices') or [])
        ]
        self.is_start = data.get('is_start', False)

    def interpret(self, received):
        if self.input == 'pick':
            try:
                return self.choices[int(received) - 1].leads_to
            except:
                return None
        elif self.input == 'type':
            result = max(x.interpret(received) for x in self.choices)

            if result[0] is None:
                return None
            return result[1]

    def __str__(self):
        '''Returns markdown representation of itself'''
        paragraphs = ['# ' + self.title] if self.title else []
        paragraphs.append(self.content)

        if self.input == 'pick':
            paragraphs.append(
                '\n'.join(
                    '**%s.** %s' % (x+1, choice) for (x, choice) in enumerate(self.choices)
                )
            )
        return '\n\n'.join(paragraphs)