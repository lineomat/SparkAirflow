import org.apache.spark.sql.SparkSession

object WordCount {
	def main(args: Array[String]) {
		val spark = SparkSession.builder.appName("Word Count").master("spark://spark-master:7077").getOrCreate()
		val sc = spark.sparkContext

		val words  = sc.parallelize(List("apple", "banana", "orange", "kiwi", "strawberry"))

		val shortWords = words.collect {
              case word if word.length < 5 => word
        }
        println(shortWords)

		spark.stop()
	}
}