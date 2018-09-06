"""
This module is for preparing controlled test data and test the system for test data.
"""

import json

import utils.common as cfg

import module.Message_Processor
import utils.Constants as Constants

msg_dict1 = {
    Constants.message_type: Constants.single_sale_record,
    Constants.product_type : Constants.keyboard,
    Constants.product_price :10

}

msg_dict2 = {
    Constants.message_type: Constants.multiple_sales_record,
    Constants.product_type: Constants.keyboard,
    Constants.product_quantity: 5,
    Constants.product_price:10

}

msg_dict3 = {
    Constants.message_type: Constants.adjustment_record,
    Constants.product_type: Constants.keyboard,
    Constants.adjust_operation_type: Constants.multiply,
    Constants.adjustment_price: 2

}

msg_dict4 = {
    Constants.message_type : Constants.single_sale_record,
    Constants.product_type : Constants.mouse,
    Constants.product_price :9

}
msg_dict5 = {
    Constants.message_type: Constants.multiple_sales_record,
    Constants.product_type: Constants.mouse,
    Constants.product_quantity: 11,
    Constants.product_price:20

}

msg_dict6 = {
    Constants.message_type: Constants.adjustment_record,
    Constants.product_type: Constants.mouse,
    Constants.adjust_operation_type: Constants.add,
    Constants.adjustment_price: 5

}

message_list = [msg_dict1,msg_dict2,msg_dict3,msg_dict4,msg_dict5,msg_dict6]
for m in message_list:
    module.Message_Processor.process(m)
    print(json.dumps(cfg.global_sales_dict, indent=2))