from item import *
from receipts import *

receipt = Receipt()

receipt.find_splitters()
receipt.set_shared_costs()

print(receipt)

# Add in way mode selection (csv)
"""
comma separated list of names
item,cost
...
item,cost

tax,tip
"""
