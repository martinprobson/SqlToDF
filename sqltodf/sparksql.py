'''
Accept SQL statement and return Panda's dataframe object containing SQL result or 
raise SqlToDFExeception on error.
Created on 15 Feb 2017

@author: martinr
'''
from __future__ import print_function

import os
import sys
import glob
import pandas as pd
from exceptions import SqlToDFException
from base import AbstractSqlToDF
import config as cfg

class SparkSqlToDF(AbstractSqlToDF):
    def __init__(self, *args,**kwargs):
        '''
        Constructor
        Check for the existence of SPARK_HOME in the environment - this is required for the Spark libraries.
        Add the required SPARK libraries to the system path.
        Configure and start up a Spark and Hive context
        '''
        if not os.environ.has_key('SPARK_HOME'):
            raise SqlToDFException("Environment variable SPARK_HOME must be set to the root directory of the SPARK installation")
        spark_home_py = os.path.expandvars("$SPARK_HOME/python")
        sys.path.append(spark_home_py)
        file_list = glob.glob(spark_home_py + "/lib/py4j*.zip")
        if file_list is None:
            raise SqlToDFException("p4j*.zip not found - this needs to be on the PYTHONPATH")
        sys.path.append(file_list[0])

        try:
            from pyspark import SparkContext, SparkConf
            from pyspark.sql import HiveContext
        except ImportError:
            raise SqlToDFException("Required pyspark modules cannot be found")
        try:
            import pandas as pd
        except ImportError:
            raise SqlToDFException("Required pandas library cannot be found")

        # Hack to force spark.driver.memory to get set.
        if cfg.spark.has_key('spark.driver.memory'):
            memory = cfg.spark['spark.driver.memory']
        else:
            memory = '1g'
        pyspark_submit_args = ' --driver-memory ' + memory + ' pyspark-shell'
        os.environ["PYSPARK_SUBMIT_ARGS"] = pyspark_submit_args

        self.sc = SparkContext(conf = self._sparkConfig(SparkConf()))
        self.sc.setLogLevel('WARN')
        self.hc = HiveContext(self.sc)

    def _sparkConfig(self,sparkc):
        '''
        Build SparkConf object
        '''
        sparkc.setMaster(cfg.spark_mode).setAppName(cfg.app_name)
        for k in cfg.spark.keys():
            sparkc.set(k,cfg.spark[k])
        self.conf = sparkc
        return self.conf


    def dumpConfig(self):
        for itm in self.conf.getAll():
            print(itm)

    def SqlToPandas(self,sql,*args,**kwargs):
        '''
        SqlToPandas
        Create a Spark SQL dataframe from the query results.
        Convert the Saprk dataframe to Pandas dataframe and return.
        Note a valid kerberos ticket is assumed.
        :param sql: the sql statement to run.
        '''
        spark_df = self.hc.sql(sql)
        pandas_df = spark_df.toPandas()
        spark_df.unpersist()
        return pandas_df
