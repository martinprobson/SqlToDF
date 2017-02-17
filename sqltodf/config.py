'''
Config file for SqlToDF
Created on 15 Feb 2017

@author: martinr
'''

#
# Spark parameters
#
spark = {
        'spark.executor.memory': '3g',
        'spark.driver.maxResultSize' : 2048,
        'spark.driver.memory' : '10g',
        'spark.ui.port' : 9095,
        }

#
# Spark application name
#
app_name = 'SqlToPandas'
#
# Spark execution mode
#
spark_mode = 'local[10]'
