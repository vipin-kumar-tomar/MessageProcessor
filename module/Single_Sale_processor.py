"""
This method process 'single_sale_message' type
"""

import utils.Constants as Constants
import utils.common as cfg
import json

def process_single_sale_message(product_type, msg_dict):
    try:
        product_price = msg_dict[Constants.product_price]

        #to check if some messages are already processed and recorded for this product type. Get the accumulated sales price.
        if product_type in cfg.global_sales_dict and Constants.total_sales_price in cfg.global_sales_dict.get(product_type, {}):
            cfg.global_sales_dict[product_type][Constants.total_sales_price] = cfg.global_sales_dict[product_type][
                                                                          Constants.total_sales_price] + product_price
        else:
            # first messaged for this product type
            cfg.global_sales_dict[product_type][Constants.total_sales_price] = product_price

        # to check if some messages are already processed and recorded for this product type. Get the accumulated sales count.
        if product_type in cfg.global_sales_dict and Constants.total_product_sales_count in cfg.global_sales_dict.get(product_type,
                                                                                                                      {}):
            cfg.global_sales_dict[product_type][Constants.total_product_sales_count] = cfg.global_sales_dict[product_type][
                                                                                   Constants.total_product_sales_count] + 1
        else:
            # first messaged for this product type
            cfg.global_sales_dict[product_type][Constants.total_product_sales_count] = 1
    except Exception as e:
        print(Constants.error_message4)
        print(str(e))
        print(json.dumps(msg_dict, indent=2))

    cfg.message_counter += 1