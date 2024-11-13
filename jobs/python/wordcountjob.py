from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
sc = spark.sparkContext

textData = sc.parallelize(["Yamaha is known for its agility", "Ducati excels in raw power", "Both brands have their unique strengths"])

counts = textData.flatMap(lambda line: line.split(" ")) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b)
#df = counts.toDF()
#df.printSchema()
#Show the DataFrame
#df.show()
print(counts.values())

sc.stop()