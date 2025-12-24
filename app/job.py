from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("SparkSQLServer") \
    .master("spark://spark-master:7077") \
    .config(
        "spark.jars",
        "/opt/spark/jars/mssql-jdbc-13.2.1.jre11.jar"
    ) \
    .config(
        "spark.driver.extraClassPath",
        "/opt/spark/jars/mssql-jdbc-13.2.1.jre11.jar"
    ) \
    .config(
        "spark.executor.extraClassPath",
        "/opt/spark/jars/mssql-jdbc-13.2.1.jre11.jar"
    ) \
    .getOrCreate()

jdbc_url = (
    "jdbc:sqlserver://sqlserver:1433;"
    "databaseName=practice;"
    "encrypt=false;"
    "trustServerCertificate=true"
)

properties = {
    "user": "sa",
    "password": "Gaurav@1804",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

df = spark.read.jdbc(
    url=jdbc_url,
    table="orders",
    properties=properties
)

df.show(5)
