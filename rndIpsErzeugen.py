import random 

def rndIP():
    min = 0
    max = 255
    seperator = '.'
    return str(str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max)))+seperator+str(int(random.uniform(min,max))))


while True:
    print (rndIP())

