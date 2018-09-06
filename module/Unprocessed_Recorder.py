"""
This method print unprocessed message report after 50th message
"""

import utils.common as cfg
import utils.Constants as Constants

def record_unprocessed_message(msg_dict,unprocess_reason):

    try:
        cfg.unprocessesd_message_counter += 1
        unprocessesd_key = Constants.unprocessed + str(cfg.unprocessesd_message_counter)
        msg_dict.update({
            "reason_for_unprocess":unprocess_reason
        })
        cfg.unprocessesd_message_dict[unprocessesd_key] = msg_dict
    except Exception as e:
        print(Constants.error_message6)
        print(str(e))
