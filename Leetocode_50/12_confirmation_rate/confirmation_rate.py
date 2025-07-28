## suppose we are having signup_df and confirmations_df

# Solution 1
from pyspark.sql.functions import col, when, sum, count, round

# Alias DataFrames
signup_df = signup_df.alias('s')
confirmations_df = confirmations_df.alias('c')

# Join DataFrames
joined_df = signup_df.join(confirmations_df, col('s.user_id') == col('c.user_id'), 'left') \
                        .groupBy(col('s.user_id').alias('user_id')) \
                        .agg(
                            sum(when(col('c.action') == 'confirmed', 1).otherwise(0)).alias('cnf_cnt'),
                            count("*").alias('total_cnt'))

# Calculate confirmation rate
result_df = joined_df \
    .withColumn('confirmation_rate', round(col('cnf_cnt') / col('total_cnt'), 2)) \
    .select('user_id', 'confirmation_rate')
