import argparse
import json
import yaml
import sys

from adventure_weave.loaders import load_data

def main():
    argparser = argparse.ArgumentParser(description="Simple commandline player for Adventure Weave games")
    argparser.add_argument('path', help='Path to the game file')
    args = argparser.parse_args()

    print(args.path)
    language = [yaml, json][args.path.endswith('json')]
    with open(args.path) as datafile:
        data = language.load(datafile)
        start_id, loaded = load_data(data)
    
    node = loaded[start_id]
    while node.choices:
        print(chr(27) + "[2J")
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