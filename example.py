from adventure_weave.loaders import load_data

data = {
    'Start of the adventure': {
        'content': 'You are standing at the brink of a new adventure',
        'choices': [
            {'name': 'Look around', 'leads_to': 'Your Surroundings'},
            {'name': 'Skip to the end', 'leads_to': 'Ending'}
        ]
    },
    'Your Surroundings': {
        'content': "There's a lot of things around you, all of which are very interesting",
        'choices': [
            {'name': 'Yeah just skip to the end', 'leads_to': 'Ending'}
        ]
    },
    'Ending': {
        'content': 'Congratulations, you have completed this indubitably riveting adventure!'
    }
}

def main():
    loaded = load_data(data)
    for item in loaded.values():
        print(item)

if __name__ == '__main__':
    main()