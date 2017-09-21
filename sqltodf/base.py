'''
Accept SQL statement and return Panda's dataframe object containing SQL result or
raise SqlToDFExeception on error.
Created on 15 Feb 2017

@author: martinr
'''
import abc

class AbstractSqlToDF(object):
    '''
    Abstract base class for SQL to DF.
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, *args,**kwargs):
        '''
        Constructor
        '''
        pass

    @abc.abstractmethod
    def SqlToPandas(self,sql,*args,**kwargs):
        '''
        SqlToPandas
        '''
        pass


    