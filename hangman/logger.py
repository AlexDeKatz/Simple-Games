import logging

logging.basicConfig(filename='application.log',
                    format=f'%(asctime)s %(levelname)s %(name)s : %(filename)s @ %(lineno)d - %(message)s')

def get_logger():
    global_logger = logging.getLogger()
    global_logger.setLevel(logging.DEBUG)
    return global_logger

