from item import *
from receipts import *

receipt = Receipt()

receipt.find_splitters()
receipt.set_shared_costs()

print(receipt)

# Add in way mode selection (csv)

# example:
"""
shank,pratix,heli

alc,3.50
something,1231.32

23.30,15.32
"""
