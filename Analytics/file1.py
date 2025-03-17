from pyspark.sql.functions import regexp_replace, split,bround,col,desc

def Analytics1(tablename):
    df = tablename.withColumn('Rupees', regexp_replace(tablename['Amount'], '[$,]', '').cast('int') * 86.81)
    df = df.withColumn('Rupees', bround(col('Rupees'), 2)).orderBy(desc('Rupees'))
    return df
