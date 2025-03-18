from pyspark.sql.functions import count
def Analytics2(tablename):
    analytics2 = tablename.groupBy('Country').agg(count('Product').alias('No_of_Products'))

    # Select and show the result
    analytics2=analytics2.select('Country', 'No_of_Products')
    return analytics2