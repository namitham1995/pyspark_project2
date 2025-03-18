import matplotlib.pyplot as plt
from pyspark.sql.functions import count
def Analytics3(tablename):
    analytics2 = tablename.groupBy('Country').agg(count('Product').alias('No_of_Products'))
    result = analytics2.collect()
    countries = [row['Country'] for row in result]
    product_counts = [row['No_of_Products'] for row in result]
    plt.figure(figsize=(6, 6))
    plt.bar(countries, product_counts, color='blue')
    plt.xlabel('Country')
    plt.ylabel('No of Products')
    plt.title('Number of Products per Count')
    plt.xticks(rotation=90)
    return plt


