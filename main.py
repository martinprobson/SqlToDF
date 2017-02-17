'''
Created on 15 Feb 2017

@author: martinr
'''
from sqltodf import Factory
#import pandas as pd
def test():
    cls = Factory.get('Spark')
    df = cls.SqlToPandas(sql='Select * from martin_test')
    print df.info(memory_usage='deep')
    print df.head()
    
def test2():
    cls = Factory.get('Spark')
    cls.dumpConfig()

if __name__ == '__main__':
    test()
