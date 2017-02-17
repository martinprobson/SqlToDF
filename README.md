# Python utils for Spark

This repo contains Python utility code for Spark 

## Module  **sqltodf**
Run a simple HQL statement in Hive SparkSQL and return resultset as a Pandas dataframe.

### Notes
 - Spark module imports (pyspark/pyspark sql) are not required as the module handles this.
 - Code currently runs in Spark 'local' mode so complex SQL (any type of join for example) is not supported.
 - Resulting Pandas dataframe will be in memory, so table much be small enough to allow this.
 - Driver memory is currently configured at 10Gb.

### Usage
Module is installed in `doxjs04://data/group/techrevass/sw/share/python/lib` so this needs to be included in your PYTHONPATH, like:-
```bash
    export PYTHONPATH=$PYTHONPATH:/data/group/techrevass/sw/share/python/lib
```

### Example
```python
    import pandas as pd
    import numpy as np
    from sqltodf import Factory
    cls = Factory.get('Spark')
    df = cls.SqlToPandas(sql='Select * from techrevass.robsom12_df_customers_non_ji')
    print df.info(memory_usage='deep')
    print df.head()
    # do stuff with df.....
```
outputs: -
```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2677302 entries, 0 to 2677301
    Data columns (total 26 columns):
    gpart           object
    e_vkont         object
    g_vkont         object
    e_fdgrp         object
    g_fdgrp         object
    e_ezawe         object
    g_ezawe         object
    e_sparte        object
    g_sparte        object
    e_vertrag       object
    g_vertrag       object
    e_einzdat       object
    g_einzdat       object
    e_auszdat       object
    g_auszdat       object
    e_anlage        object
    g_anlage        object
    e_vstelle       object
    g_vstelle       object
    e_opbel         object
    g_opbel         object
    e_begperiode    object
    g_begperiode    object
    e_endperiode    object
    g_endperiode    object
    measure_date    object
    dtypes: object(26)
    memory usage: 5.6 GB
    None
            gpart       e_vkont       g_vkont     e_fdgrp     g_fdgrp e_ezawe  \
    0  1000209698  850000215888  850001003100  0000000002  0000000002       D
    1  1000769984  850000776174  850001019675  0000000005  0000000005
    2  1000738107  850000744297  850001082402  0000000005  0000000005
    3  1000398775  850000404965  850001110251  0000000002  0000000002       D
    4  1000374034  850000380224  850001140176  0000000002  0000000002       D
    
      g_ezawe e_sparte g_sparte   e_vertrag     ...         g_anlage   e_vstelle  \
    0       D       02       01  0490017225     ...       3490020824  2490011225
    1               02       01  0405021106     ...       3585024894  2405017106
    2               02       01  0375026243     ...       3550024890  2375012243
    3       D       02       01  0200018509     ...       3200024043  2200016509
    4       D       02       01  0300014241     ...       3300026903  2300009241
    
        g_vstelle       e_opbel       g_opbel e_begperiode g_begperiode  \
    0  2490011225  100013143000  100014601439     20070905     20080111
    1  2405017106  100044430486  100044430487     20160513     20160513
    2  2375012243  100013034434  100013500451     20070825     20071005
    3  2200016509  100012842060  100012842073     20070810     20070812
    4  2300009241  100021075111  100021075113     20090623     20090623
    
      e_endperiode g_endperiode measure_date
    0     99991231     99991231   2017-01-31
    1     99991231     99991231   2017-01-31
    2     99991231     99991231   2017-01-31
    3     99991231     99991231   2017-01-31
    4     99991231     99991231   2017-01-31
    
    [5 rows x 26 columns]
```


