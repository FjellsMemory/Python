from sys import argv

# multistring = argv

# def multivar(*args):
    

def save_ranking(first, second, third=None, fourth=None):
    rank = {}
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print(rank)
    print(rank.keys())
    print(rank.values())
    keylist = list(rank.keys())
    valuelist = list(rank.values())
    print(keylist, valuelist, "i'm da valuelist you tryna pop from")
    valuelist.pop(2)
    valuelist.insert(2, "broham")
    print("you ought to see brandi replaced with broham")
    zipdict = zip(keylist, valuelist)
    print(dict(zipdict))

def addlikeboss(**kwargs):
    return kwargs

def mydictfunc(**kwargs):
    print(kwargs)

def args_n_kwargs(*args, **kwargs):
    print(args)     
    print(kwargs)
# args_n_kwargs('ming', 'alice', 'tom', fourth='wilson', fifth='roy')
# ('ming', 'alice', 'tom')
# {'fourth': 'wilson', 'fifth': 'roy'}

# primes = [2, 3, 5, 7, 11, 13]
# args_n_kwargs(*primes)

# mydictfunc(a=1, b=2, c=3)
var = addlikeboss(a=1, b=2, c=3)
print(type(var))
print(*var)
mydict = {1: 4, 2: 5, 3: 6}
print(*mydict.values())
