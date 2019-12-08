'''program which generates howmany=10 passwords for howmany=10 persons'''

import pandas as pd
import string
import random


def passgen():
    #generating passwords of the length of 16 made of digits and uppercase, lowercase letters
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16)) 

howmany = 10
#generating lists of persons and passwords for them
persons = ['Person'+str(i+1) for i in range(howmany)]
passwords = [passgen() for i in range(howmany)]

#creating a dict, then creating a df out of this dict
p = {'Person':persons, 'Password': passwords}
df = pd.DataFrame(p)

print(df)

