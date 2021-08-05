import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logging.info('Hello From Step1')

    logging.info('event: ')
    logging.info(json.dumps(event))

    logging.info('context: ')
    print(context)

    logging.info('End From Step1')

    return {
        'event': json.dumps(event)
    }
