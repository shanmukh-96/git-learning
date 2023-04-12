from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("movie tickets").getOrCreate()


# df = spark.table("default.movie_tickets")

df = spark.read.format("csv").option("header","true").option("inferSchema","true").option("sep",",").load("/FileStore/tables/movie_tickets-2.csv")

df.show()
# df.createOrReplaceTempView("temp_movie_tickets_1")

# windowSpec  = Window.partitionBy(substring("seat_number",1,1)).orderBy("seat_number")

df2 = df.withColumn("s1", lead("occupancy",1).over(Window.partitionBy(substring("seat_number",1,1)).orderBy(substring("seat_number",2,-1)))).withColumn("s2", lead("occupancy",2).over(Window.partitionBy(substring("seat_number",1,1)).orderBy(substring("seat_number",2,-1)))).withColumn("s3", lead("occupancy",3).over(Window.partitionBy(substring("seat_number",1,1)).orderBy(substring("seat_number",2,-1)))).withColumn("occupation_sum", expr("occupancy+s1+s2+s3")).withColumn("last_seat", lead("seat_number",3).over(Window.partitionBy(substring("seat_number",1,1)).orderBy(substring("seat_number",2,-1)))).select("seat_number","last_seat").where(col("occupation_sum")==4)

# lead("seat_number",3).over(Window.partitionBy(substring("seat_number",1,1)).orderBy(substring("seat_number",2,-1)))


df2.show()