## assume we have employee df

# solution 1
from pyspark.sql.functions import col, count

# Alias the employee_df for self-join
e1 = employee_df.alias("e1")
e2 = employee_df.alias("e2")

# Join employees with their managers
joined_df = e1.join(e2, col("e1.managerId") == col("e2.id"))

result_df = (
    joined_df
    .groupBy("e2.id", "e2.name")
    .agg(count("*").alias("report_count"))
    .filter(col("report_count") >= 5)
    .select("e2.name")
)

## solution 2
from pyspark.sql.window import Window
from pyspark.sql.functions import col, count

# Step 1: Define window partitioned by managerId
window_spec = Window.partitionBy("managerId")

# Step 2: Add a column 'cnt' with count of reports per manager
window_df = (
    employee_df
    .withColumn("cnt", count("*").over(window_spec))
    .filter(col("cnt") >= 5)
    .select("managerId")
    .distinct()
)

# Step 3: Join back with employee_df to get names
result_df = (
    employee_df
    .join(window_df, employee_df["id"] == window_df["managerId"])
    .select("name", "id")
    .distinct()
)