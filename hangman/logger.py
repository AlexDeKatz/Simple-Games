import logging

logging.basicConfig(filename='error.log',
                    format=f'%(asctime)s %(levelname)s %(name)s : %(filename)s @ %(lineno)d - %(message)s')

def get_logger():
    return logging.getLogger()

