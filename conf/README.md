# Remote Spark Jobs on YARN

This directory contains the Hadoop/yarn configuration files from the vagrant Hadoop box
[vagrant-hadoop-hive-spark](https://github.com/martinprobson/vagrant-hadoop-hive-spark "Github repo")

They allow remote spark jobs/shells to be launched on the yarn cluster, using `--master yarn` option on `pyspark` and `spark-shell`.

All that is required on the client machine is a copy of the spark code. A good description of how this works is [here](http://theckang.com/2015/remote-spark-jobs-on-yarn/)

## Environment Variables

In order to be able to connect to remote cluster, Spark needs to be able to find the configuration files, so `HADOOP_CONF_DIR` is set in the conda virtual environment via the file `/home/martinr/miniconda2/envs/SqlToDF/etc/conda/activate.d/set_env.sh`:-

```
#!/bin/sh
export OLD_PATH=${PATH}
alias projdir="cd ~/Documents/projects/python/git_projects/SqlToDF"
MYDIR=${HOME}/Documents/projects/python/git_projects/SqlToDF
export HADOOP_CONF_DIR=${MYDIR}/conf
export SPARK_HOME=${MYDIR}/spark
export PATH=${PATH}:$SPARK_HOME/bin:$SPARK_HOME/sbin
```

