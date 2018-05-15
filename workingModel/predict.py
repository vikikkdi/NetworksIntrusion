#!/usr/bin/env python

# dataset: http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

import sys
import os

os.environ['SPARK_HOME']="/opt/spark"

sys.path.append("/opt/spark/python")

try:
    from pyspark import SparkContext, SparkConf
    from pyspark.mllib.clustering import KMeans, KMeansModel 
    from pyspark.mllib.feature import StandardScaler
    from pyspark.mllib.linalg import Vectors
    print ("Successfully imported Spark Modules")
except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)

from collections import OrderedDict
from numpy import array
from math import sqrt

if __name__ == "__main__":
    if (len(sys.argv) != 2):
		print "Usage: /path/to/spark/bin/spark-submit --driver-memory 2g " + \
		  "predict.py kddcup.data.file"
        	sys.exit(1)

    data_file = sys.argv[1]
    conf = SparkConf().setAppName("KDDCup99") \
      #.set("spark.executor.memory", "2g")
    sc = SparkContext(conf=conf)

    model=KMeansModel.load(sc,"best_model")

    clusters=model.clusterCenters
    
    with open(data_file) as file:
        for line in file:
            line_split = line.split(",")
            clean_line_split = [line_split[0]]+line_split[4:]
            clusterIndex=model.predict(array([float(x) for x in clean_line_split]))
            print clusterIndex
    print

print "DONE!"
