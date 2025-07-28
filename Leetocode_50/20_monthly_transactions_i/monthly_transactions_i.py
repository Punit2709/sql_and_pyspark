## assume we have transaction df

from pyspark.sql.functions import col, sum, count, when, date_format

transaction_grp_df = transaction_df \
    .groupBy(date_format(col('trans_date'), 'yyyy-MM').alias('month')) \
    .agg(
        sum(col('amount')).alias('total_amount'),
        count("*").alias('total_transaction'),
        sum(when(col('status') == 'approved', col('amount')).otherwise(0)).alias('approved_amount'),
        sum(when(col('status') == 'approved', 1).otherwise(0)).alias('approved_transaction')
    )