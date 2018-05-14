'''
Config file for SqlToDF
Created on 15 Feb 2017

@author: martinr
'''

#
# Spark parameters
#
SPARK = {
        'spark.executor.memory': '3g',
        'spark.driver.maxResultSize' : 2048,
        'spark.driver.memory' : '10g',
        'spark.ui.port' : 9095,
        }

#
# Spark application name
#
APP_NAME = 'SqlToPandas'
#
# Spark execution mode
#
#SPARK_MODE = 'local[10]'
#SPARK_MODE = 'yarn'
SPARK_MODE = 'local[*]'
