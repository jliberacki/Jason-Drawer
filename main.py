import sys
import argparse
from os import path
import json
from drawer import draw

def main():
    if len(sys.argv) < 2: raise Exception("Please provide json file")
    argparser = argparse.ArgumentParser(description='Parse and draw from json')
    argparser.add_argument('input', help='path to json')
    argparser.add_argument('-o', '--output', help='Optional png file to save image')
    args = argparser.parse_args()
    
    # print(args.input)
    # print(args.output)

    if not path.isfile(args.input): raise Exception("Input file does not exist")

    with open(args.input) as input_file:
        data = json.load(input_file)

    Figures = data["Figures"]
    Screen = data["Screen"]
    Palette = data["Palette"]

    draw(Figures,Screen,Palette,args.output)

if __name__ == "__main__":  
    main()
