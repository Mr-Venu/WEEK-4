import random
a=input('Enter a sentence: ')
b=list(a[i:i+3] for i in range(0,len(a),3))
d=""
while(b!=[]):
    c=random.choice(b)
    b.remove(c)
    d=d+c
print(d)    
