test = "12233443"

charactersPicked = []
tupleResult = []

currentSlot = 0

currentCount = 0

def findCharacters():
    recursiveFinder(currentSlot,[char for char in test])
    Counter([char for char in test],charactersPicked)


def recursiveFinder(slot,arr):
    if((slot == len(arr)) == False):
        if(charactersPicked.count(arr[slot]) == 0):
            charactersPicked.append(arr[slot])
        recursiveFinder(slot+1,arr)

def Counter(arr,CC):
    final =""
    for i in CC:
        fin  = str((i,arr.count(i)))
        final = final + " " + fin

    print(final)


findCharacters()