from pyspark.sql import HiveContext
from pyspark.sql.types import *
from pyspark.sql import Row
csv_data = sc.textFile("file:///home/maria_dev/go_track_trackspoints.csv")
print("Split")
csv_data  = csv_data.map(lambda p: p.split(","))
header = csv_data.first()
csv_data = csv_data.filter(lambda p:p != header)
df_csv = csv_data.map(lambda p: Row(id = int(p[0]), latitude = p[1], longitude=p[2], track_id =int(p[3]), time =p[4])).toDF()
from pyspark.sql import HiveContext
hc = HiveContext(sc)
df_csv.write.format("orc").saveAsTable("pool.carss")

print("Successful")