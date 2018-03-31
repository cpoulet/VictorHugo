#!/usr/bin/env python3

import json
import random
import argparse

UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SIZE = {'S':[0, 30],
        'M':[30, 45],
        'L':[45, 150]}

class Poem:
    def __init__(self, size):
        self.size = size
        with open('data/strophes.json', 'r') as fp:
            self.strophes = json.load(fp)
        self.D = {}
        for c in UP:
            self.D[c] = []
        for s in self.strophes:
            if s[0] in UP:
                self.D[s[0]].append(s)
            elif s[0] is 'À':
                self.D['A'].append(s)
            elif s[0] is 'É':
                self.D['E'].append(s)
            elif s[0] is 'Ô':
                self.D['O'].append(s)
        for c in UP:
            random.shuffle(self.D[c])

    def randStrophe(self, char):
        return self.D[char.upper()].pop()

    def sizedStrophe(self, char, size='S'):
        for i,x in enumerate(self.D[char.upper()]):
            if SIZE[size][0] <= len(x) and len(x) < SIZE[size][1]:
                return self.D[char.upper()].pop(i)

    def create(self, sentence="amour"):
        poem = ''
        for c in sentence.upper():
            if c in UP:
                if not self.size:
                    poem += self.randStrophe(c)
                else:
                    poem += self.sizedStrophe(c, self.size)
                poem += '\n'
        return poem[:-1]

def main():
    parser = argparse.ArgumentParser(description='Cadavre Exquis avec des strophes de Victor Hugo')
    parser.add_argument('acro', nargs='?', default='amour', help='Acrostiche')
    parser.add_argument('-s', '--size', action='store', choices=['S', 'M', 'L'], help='Coherence de taille')
    args = parser.parse_args()
    P = Poem(args.size)
    print(P.create(args.acro))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        if str(e):
            print('Error : ' + str(e))
