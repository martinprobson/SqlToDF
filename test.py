'''
Created on 15 Feb 2017

@author: martinr
'''
from __future__ import print_function
import os
import sys
import glob
import unittest
from multiprocessing import Process

import pandas as pd

from sqltodf import Factory


class TestSqltodf(unittest.TestCase):
    ''' Unit Test - sqltodf '''


    @classmethod
    def setUpClass(cls):
        ''' Setup a table in hive to run our unit test against.
        This has to be run in a separate process to avoid spark context issues
        '''

        def setup():
            ''' table setup '''
            if not os.environ.has_key('SPARK_HOME'):
                raise Exception("Environment variable SPARK_HOME must be set " +
                                "to the root directory of the SPARK installation")
            spark_home_py = os.path.expandvars("$SPARK_HOME/python")
            sys.path.append(spark_home_py)
            file_list = glob.glob(spark_home_py + "/lib/py4j*.zip")
            if file_list is None:
                raise Exception("p4j*.zip not found - this needs to be on the PYTHONPATH")
            sys.path.append(file_list[0])
            try:
                from pyspark import SparkContext, SparkConf
                from pyspark.sql import HiveContext
            except ImportError:
                raise Exception("Required pyspark modules cannot be found")

            # Configure Spark
            conf = SparkConf().setAppName('SQLTODF_UT')
            conf = conf.setMaster('local[*]')
            sparkctx = SparkContext(conf=conf)

            pandasdf = pd.DataFrame({'name': ['Martin', 'Gemma'], 'age': [16, 52]})
            sqlctx = HiveContext(sparkctx)
            sqldf = sqlctx.createDataFrame(pandasdf)
            sqldf.write.format('orc').mode('overwrite').saveAsTable('sqltodf_test')
            sparkctx.stop()

        process = Process(target=setup)
        process.start()
        process.join()


    def test_spark(self):
        ''' Test SqlToPandas with Spark '''
        cls = Factory.get('Spark')
        dataf = cls.SqlToPandas(sql='Select * from sqltodf_test')
        self.assertEqual(len(dataf), 2, 'Invalid dataframe length!')
        self.assertEqual(dataf.loc[0, 'age'], 16, 'Dataframe contents mis-match')

    @classmethod
    def tearDownClass(cls):
        pass
