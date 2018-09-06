"""
This module process the messages
"""

import json
import sys
import utils.common as cfg
import utils.Constants as Constants
import module.Single_Sale_processor as single
import module.Multiple_Sale_Processor as multiple
import module.Adjustment_Processor as adjust
import module.Unprocessed_Recorder as unprocess

"""
entry point method to handle process requests and invoke corresponding process method.
"""
def process(msg_dict):
    try:
        record_all_messages(msg_dict)
        product_type = msg_dict[Constants.product_type]
        message_type = msg_dict[Constants.message_type]
        if message_type == Constants.single_sale_record:
            single.process_single_sale_message(product_type, msg_dict)
        if message_type == Constants.multiple_sales_record:
            multiple.process_multiple_sale_message(product_type, msg_dict)
        if message_type == Constants.adjustment_record:
            adjust.process_adjust_sale_message(product_type, msg_dict)

    except KeyError as e:
        print(str(e))
        unprocess.record_unprocessed_message(msg_dict, Constants.error_message1)

    if cfg.message_counter in [10, 20, 30, 40, 50]:
        after_tenth_message()

    if cfg.message_counter == 50:
        print(Constants.error_message2)
        after_fiftieth_message()
        clean()
        sys.exit(0)




"""
This method print a sales report after every 10th message
"""
def after_tenth_message():
    print('After ' + str(cfg.message_counter) + 'message')
    print(json.dumps(cfg.global_sales_dict, indent=2))

"""
This method print a adjustment report after 50th message
"""
def after_fiftieth_message():
    #print(json.dumps(cfg.individual_message_dict, indent=2))
    print(json.dumps(cfg.adjustment_dict, indent=2))
    print("printing unprocessed message")
    print(json.dumps(cfg.unprocessesd_message_dict, indent=2))


"""
This method reset the dictionaries and counters before completion
"""
def clean():
    cfg.adjustment_dict = {}
    cfg.global_sales_dict = {}
    cfg.message_counter = 0
    cfg.adjustment_dict = {}
    cfg.adjustment_counter = 0
    cfg.unprocessesd_message_dict = {}
    cfg.unprocessesd_message_counter = 0

"""
This method records all sales
"""
def record_all_messages(msg_dict):
    try:
        cfg.individual_message_counter += 1
        individual_key = Constants.individual + str(cfg.individual_message_counter)
        cfg.individual_message_dict[individual_key] = msg_dict
    except Exception as e:
        print(str(e))

