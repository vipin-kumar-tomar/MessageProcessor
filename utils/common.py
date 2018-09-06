"""
This module keep the golbal dictionaries and counters
"""

import collections
from collections import defaultdict

"""
Dictionary for recording and accumulating all sales to print after every 10th message
"""
global_sales_dict = defaultdict(dict)

"""
keep a message counter
"""
message_counter = 0

"""
Dictionary for recording adjustments and print after 50th message
"""
adjustment_dict = defaultdict(dict)

"""
keep a counter for adjustments
"""
adjustment_counter = 0

"""
Dictionary for recording unprocessed messages
"""
unprocessesd_message_dict = defaultdict(dict)

"""
Dictionary for recording individual message sales.
"""
individual_message_dict = defaultdict(dict)

"""
keep a counter for individual messages
"""
individual_message_counter = 0


"""
keep a counter for unprocessed messages
"""
unprocessesd_message_counter = 0