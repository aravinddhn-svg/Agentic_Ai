--- important pyspark functions --

--- ARRAY  and explode,posexplode--

data = [
    (1, ["phone", "charger"]),
    (2, ["pepsi", "coke"])
]

df = spark.createDataFrame(
    data,
    ["id", "items"]
)

df.show(10,False)

>>> df1.show(10,False)
+---+-------+
|id |item   |
+---+-------+
|1  |phone  |
|1  |charger|
|2  |pepsi  |
|2  |coke   |
+---+-------+

>>> df1=df.select("id",explode("items").alias("item"))

>>> df1.show(10,False)
+---+-------+
|id |item   |
+---+-------+
|1  |phone  |
|1  |charger|
|2  |pepsi  |
|2  |coke   |
+---+-------+

df.show(10,False)
>>> df.show(10,False)
+---+----------------+
|id |items           |
+---+----------------+
|1  |[phone, charger]|
|2  |[pepsi, coke]   |
+---+----------------+


df2= df.select("id",posexplode("items").alias("itm_pos","itm_val"))

df2.show(10,False)

--- ARRAY , explode, posexplode --

--- concat_ws

>>> df2.show(10,False)
+---+-------+-------+
|id |itm_pos|itm_val|
+---+-------+-------+
|1  |0      |phone  |
|1  |1      |charger|
|2  |0      |pepsi  |
|2  |1      |coke   |
+---+-------+-------+


>>> 
>>> df3 = df2.withColumn(
...     "record_id",
...     concat_ws("_", "itm_pos", "itm_val")
... )
>>> 
>>> df3.show(10,False)
+---+-------+-------+---------+
|id |itm_pos|itm_val|record_id|
+---+-------+-------+---------+
|1  |0      |phone  |0_phone  |
|1  |1      |charger|1_charger|
|2  |0      |pepsi  |0_pepsi  |
|2  |1      |coke   |1_coke   |
+---+-------+-------+---------+


-- concat_ws --

  
