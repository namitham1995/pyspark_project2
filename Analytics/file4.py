
from pyspark.sql.functions import desc


def Analytics4(tablename):
    # Filter rows where 'Country' is 'India' and order by 'Date' descending
    out = tablename.filter(tablename['Country'] == 'India').orderBy(desc('Date'))

    # Select the relevant columns
    out2 = out.select('Sales Person', 'Product', 'Date', 'Boxes Shipped', 'Rupees')

    return out2

