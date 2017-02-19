'''
Created on 15 Feb 2017

@author: martinr
'''
from .sparksql import SparkSqlToDF

class Factory(object):
    '''
    Factory class to create sqltodf instances.
    '''
    __factory_classes = {
        "spark": SparkSqlToDF
        }

    @staticmethod
    def get(name,*args,**kwargs):
        '''
        Factory method for SqlToDF.
        '''
        factory_class = Factory.__factory_classes.get(name.lower(),None)
        if factory_class:
            return factory_class(*args,**kwargs)
        raise NotImplementedError("The requested SqlToDF class has not been implemented")
