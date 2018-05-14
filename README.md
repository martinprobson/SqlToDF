# Python utils for Spark

This repo contains Python utility code for Spark 

## Module  **sqltodf**
Run a simple HQL statement in Hive SparkSQL and return resultset as a Pandas dataframe.

### Notes
 - Spark module imports (pyspark/pyspark sql) are not required as the module handles this.
 - Code currently runs in Spark 'local' mode so complex SQL (any type of join for example) is not supported.
 - Resulting Pandas dataframe will be in memory, so table must be small enough to allow this.
 - Driver memory is currently configured at 10Gb.

### Usage
Invlude this module somewhere on your PYTHONPATH.
```bash
    export PYTHONPATH=$PYTHONPATH:<path to>/sqltodf
```

### Example
```python
    import pandas as pd
    import numpy as np
    from sqltodf import Factory
    cls = Factory.get('Spark')
    df = cls.SqlToPandas(sql='Select * from testtable')
    print df.info(memory_usage='deep')
    print df.head()
    # do stuff with df.....
```
outputs: -
```
    <class 'pandas.core.frame.DataFrame'>
```


