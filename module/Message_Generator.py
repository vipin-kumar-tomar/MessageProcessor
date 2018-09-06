"""
This module is generate messages using random data from a data set.
This will generate messages to fulfill and test all the requirements of the system.
"""

import random
from random import randint

import utils.common as cfg

import module.Message_Processor
import utils.Constants as Constants
import utils.config_reader

#product type data set
product_type = [Constants.keyboard, Constants.mouse, Constants.speaker, Constants.monitor, Constants.hdd, Constants.ram, Constants.motherboard, Constants.graphic_card, Constants.cpu, Constants.power_supply]
#message types as per requirement
message_types = [Constants.single_sale_record, Constants.multiple_sales_record, Constants.adjustment_record]
#operation types as per requirement
operation_type = [Constants.add, Constants.multiply, Constants.subtract]

generate_range = utils.config_reader.read_json_data_file("message","range")
for i in range(0,51):
    msg_dict={}

    saleBeforeAdjustCount = utils.config_reader.read_json_data_file("message","saleBeforeAdjustCount")
    product_price_start = utils.config_reader.read_json_data_file("product","priceRangeStart")
    product_price_end = utils.config_reader.read_json_data_file("product", "priceRangeEnd")
    quanity_range_start = utils.config_reader.read_json_data_file("product", "quanityRangeStart")
    quanity_range_end = utils.config_reader.read_json_data_file("product", "quanityRangeEnd")
    adjustment_price_start = utils.config_reader.read_json_data_file("product", "adjustmentPriceStart")
    adjustment_price_end = utils.config_reader.read_json_data_file("product", "adjustmentPriceEnd")

    message_type = random.choice(message_types)

    # to control the data set so that adjustment sales messages are created after few sales
    while cfg.message_counter < saleBeforeAdjustCount and message_type == Constants.adjustment_record:
        message_type = random.choice(message_types)

    if message_type == Constants.single_sale_record:
        msg_dict = {
            Constants.message_type: Constants.single_sale_record,
            Constants.product_type:random.choice(product_type),
            Constants.product_price:randint(product_price_start, product_price_end)

        }
    elif message_type == Constants.multiple_sales_record:
        msg_dict = {
            Constants.message_type: Constants.multiple_sales_record,
            Constants.product_type:random.choice(product_type),
            Constants.product_quantity: randint(quanity_range_start, quanity_range_end),
            Constants.product_price:randint(product_price_start, product_price_end)

        }
    elif message_type == Constants.adjustment_record:
        msg_dict = {
            Constants.message_type: Constants.adjustment_record,
            Constants.product_type: random.choice(product_type),
            Constants.adjust_operation_type: random.choice(operation_type),
            Constants.adjustment_price: randint(adjustment_price_start, adjustment_price_end)

        }
    # Invoke message processor
    module.Message_Processor.process(msg_dict)



