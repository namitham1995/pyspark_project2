
import matplotlib.pyplot as plt
from pyspark.sql import functions as F
def Analytics5(tablename):
# Aggregate data by 'Country' and calculate the sum of 'Boxes Shipped' and 'Rupees'
    analytics= tablename.groupBy('Country').agg(
        F.sum('Boxes Shipped').alias('Total Boxes Shipped'),
        F.sum('Rupees').alias('Total Revenue')
    )
    return analytics



