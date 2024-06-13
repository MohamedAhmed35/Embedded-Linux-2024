import os
from pprint import pprint

# Access all environment variables
pprint(dict(os.environ), width = 1,)

# Access a particular enivronment variable
print('\n', os.environ['HOME'], '\n')

pprint(os.environ['PATH'])


