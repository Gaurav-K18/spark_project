from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkSQLServer") \
    .master("spark://spark-master:7077") \
    .config(
        "spark.jars",
        "/opt/spark/jars/extra-jar/mssql-jdbc-13.2.1.jre11.jar"
    ) \
    .getOrCreate()



properties = {
    "user": "spark_user",
    "password": "Spark@123",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


df = spark.read.jdbc(
    url="jdbc:sqlserver://host.docker.internal:1435;databaseName=practice;encrypt=false",
    table="dbo.orders",
    properties={
        "user": "spark_user",
        "password": "Spark@123",
        "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    }
)


df.show()
