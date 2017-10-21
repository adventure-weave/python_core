from adventure_weave.loaders import load_data

data = {
    'start': {
        'title': 'Start of the adventure',
        'content': 'You are standing at the brink of a new adventure',
        'choices': [
            {'name': 'Look around', 'leads_to': 'scene1'},
            {'name': 'Skip to the end', 'leads_to': 'ending'}
        ]
    },
    'scene1': {
        'title': 'Your Surroundings',
        'content': "There's a lot of things around you, all of which are very interesting",
        'choices': [
            {'name': 'Yeah just skip to the end', 'leads_to': 'ending'}
        ]
    },
    'ending': {
        'title': 'The End', 
        'content': 'Congratulations, you have completed this indubitably riveting adventure!'
    }
}

def main():
    start_id, loaded = load_data(data)
    
    node = loaded[start_id]
    while node.choices:
        print(node)
        choice = None
        while choice is None:
            try:
                choice = node.choices[int(input('> ')) - 1]
            except:
                print("Input not recognized, try again")
        node = loaded[choice.leads_to]
    
    print(node)

if __name__ == '__main__':
    main()