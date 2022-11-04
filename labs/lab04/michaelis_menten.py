#!/usr/bin/env python
# coding: utf-8

# In[2]:


from argparse import ArgumentParser
import json


# In[3]:


parser = ArgumentParser()

parser.add_argument('-S', type=float, required=True)
parser.add_argument('-E0', type=float, required=True)
parser.add_argument('-KM', type=float, required=True)
parser.add_argument('-k', type=float, required=True)
parser.add_argument('--savefile')

args = parser.parse_args()
v = args.k * args.E0 * args.S / (args.KM + args.S)
data = {
    "v" : v,
    "S" : args.S,
    "E0" : args.E0,
    "KM": args.KM,
    "k" : args.k
}
if args.savefile is not None:
    with open(args.savefile , 'w') as out:
        json.dump(data, out, indent=4)
print(v)

