"""
This method process 'adjust_sale_message' type
"""


import utils.common as cfg
import utils.Constants as Constants
import module.Unprocessed_Recorder as unprocess

def process_adjust_sale_message(product_type, msg_dict):
    try:
        operation_type = msg_dict[Constants.adjust_operation_type]
        adjustment_price = msg_dict[Constants.adjustment_price]
        if product_type in cfg.global_sales_dict and Constants.total_product_sales_count in cfg.global_sales_dict.get(
                product_type, {}):
            total_product_sales_count = cfg.global_sales_dict[product_type][Constants.total_product_sales_count]

            # adjusment opeartion is add.
            if operation_type == Constants.add:
                if product_type in cfg.global_sales_dict and Constants.total_sales_price in cfg.global_sales_dict.get(product_type, {}):
                    current_total_sale_price = cfg.global_sales_dict[product_type][Constants.total_sales_price]
                    cfg.global_sales_dict[product_type][Constants.total_sales_price] = current_total_sale_price + (
                    total_product_sales_count * adjustment_price)

                    update_adjustment_report(current_total_sale_price, adjustment_price, total_product_sales_count,
                                             operation_type, product_type)
                else:
                    unprocess.record_unprocessed_message(msg_dict, Constants.error_message3)

            #adjusment opeartion is subtract.
            elif operation_type == Constants.subtract:
                if product_type in cfg.global_sales_dict and Constants.total_sales_price in cfg.global_sales_dict.get(product_type, {}):
                    current_total_sale_price = cfg.global_sales_dict[product_type][Constants.total_sales_price]
                    if current_total_sale_price <  total_product_sales_count * adjustment_price:
                        unprocess.record_unprocessed_message(msg_dict, Constants.error_message7)
                    else:
                        cfg.global_sales_dict[product_type][Constants.total_sales_price] = cfg.global_sales_dict[product_type][
                                                                                      Constants.total_sales_price] - (
                                                                                  total_product_sales_count * adjustment_price)
                        update_adjustment_report(current_total_sale_price, adjustment_price, total_product_sales_count,
                                                 operation_type, product_type)

                else:
                    unprocess.record_unprocessed_message(msg_dict, Constants.error_message3)

            # adjusment opeartion is multiply.
            else:
                if product_type in cfg.global_sales_dict and Constants.total_sales_price in cfg.global_sales_dict.get(product_type, {}):
                    current_total_sale_price = cfg.global_sales_dict[product_type][Constants.total_sales_price]
                    cfg.global_sales_dict[product_type][Constants.total_sales_price] = cfg.global_sales_dict[product_type][
                                                                                  Constants.total_sales_price] * adjustment_price
                    update_adjustment_report(current_total_sale_price, adjustment_price, total_product_sales_count,
                                             operation_type, product_type)
                else:
                    unprocess.record_unprocessed_message(msg_dict, Constants.error_message3)
        else:
            unprocess.record_unprocessed_message(msg_dict, Constants.error_message3)
    except Exception as e:
        print(str(e))
        unprocess.record_unprocessed_message(msg_dict, Constants.error_message8)

    cfg.message_counter += 1


"""
This method create and update adjustment record to be printed out after 50th message
"""
def update_adjustment_report(current_total_sale_price,adjustment_price, total_product_sales_count, adjust_type, product_type):

    try:
        cfg.adjustment_counter += 1
        adjustment_key = Constants.adjustment + str(cfg.adjustment_counter)

        cfg.adjustment_dict[adjustment_key].update({
             Constants.product_type_is:product_type,
             Constants.adjustment_type_is: adjust_type,
             Constants.price_to_be_adjusted:adjustment_price,
             Constants.before_adjustment_total_sale_price_is:  current_total_sale_price,
             Constants.after_adjustment_total_sale_price_is: cfg.global_sales_dict[product_type][
                 Constants.total_sales_price],
             Constants.total_sale_recorded_for_this_product: total_product_sales_count})
    except Exception as e:
        print(Constants.error_message6)
        print(str(e))

