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

-- map ---

data = [
    (1, {"i1": "phone", "i2": "charger"}),
    (2, {"i1": "pepsi"})
]

df = spark.createDataFrame(
    data,
    ["id", "items"]
)


df.show(10,False)
df.show(10,False)

+---+----------------------------+
|id |items                       |
+---+----------------------------+
|1  |{i1 -> phone, i2 -> charger}|
|2  |{i1 -> pepsi}               |
+---+----------------------------+


df.select(
    "id",
    col("items")["i1"].alias("item"),
).show(10,False)

+---+-----+
|id |item |
+---+-----+
|1  |phone|
|2  |pepsi|
+---+-----+

But if the keys are dynamic, you don't know whether the key is i1, i2, etc.

Then explode() is very useful.


df2 = df.select(
    "id",
    explode("items").alias("item_key", "item_value")
)

df2.show(10,False)

+---+--------+----------+
|id |item_key|item_value|
+---+--------+----------+
|1  |i1      |phone     |
|1  |i2      |charger   |
|2  |i1      |pepsi     |
+---+--------+----------+

important:

explode will works if its Array or MapType type it wont work on struct types

-- refer example on array_zip --
df4 = df3.select(
    "id",
    create_map(
        col("nm_score.nm"),
        col("nm_score.score")
    ).alias("name_salary")
)



-- map ---


-- arrays_zip() --


id | names                    | salaries
1  | [John, Alice, Bob]       | [100, 200, 300]

John  → 100
Alice → 200
Bob   → 300


from pyspark.sql.functions import arrays_zip

df2 = df.withColumn(
    "combined",
    arrays_zip("names", "salaries")
)


data1 =["John", "Alice", "Bob"]   

data2 =[100, 200, 300]


df=spark.createDataFrame([(1,data1,data2),(2,data1,data2),(3,data1,data2)],["id","nm","score"])

df=spark.createDataFrame([(1,data1,data2),(2,data1,data2),(3,data1,data2)],["id","nm","score"])
>>> df.show(10,False)
+---+------------------+---------------+
|id |nm                |score          |
+---+------------------+---------------+
|1  |[John, Alice, Bob]|[100, 200, 300]|
|2  |[John, Alice, Bob]|[100, 200, 300]|
|3  |[John, Alice, Bob]|[100, 200, 300]|
+---+------------------+---------------+


df1=df.select("id",arrays_zip("nm","score").alias("nm_score"))

df2= df1.select("id",explode("nm_score"))


df1.show(10,False)

+---+---------------------------------------+
|id |nm_score                               |
+---+---------------------------------------+
|1  |[{John, 100}, {Alice, 200}, {Bob, 300}]|
|2  |[{John, 100}, {Alice, 200}, {Bob, 300}]|
|3  |[{John, 100}, {Alice, 200}, {Bob, 300}]|
+---+---------------------------------------+

>>> df2= df1.select("id",explode("nm_score").alias("nm_score"))
>>> df2.show(10,False)
+---+------------+
|id |nm_score         |
+---+------------+
|1  |{John, 100} |
|1  |{Alice, 200}|
|1  |{Bob, 300}  |
|2  |{John, 100} |
|2  |{Alice, 200}|
|2  |{Bob, 300}  |
|3  |{John, 100} |
|3  |{Alice, 200}|
|3  |{Bob, 300}  |
+---+------------+


df3= df2.select("id",explode("nm_score").alias("nm","sal"))
df3.show(10,False)


important:

explode will works if its Array or MapType type it wont work on struct types


df2.select("id",col("nm_score")["nm"]).show(10,False)


df3= df2.select("id",explode("nm_score").alias("nm","sal"))

-- use the create_map


df4 = df2.select(
    "id",
    create_map(
        col("nm_score.nm"),
        col("nm_score.score")
    ).alias("name_salary")
)

df4.show(10,False)
df5= df4.select("id",explode("name_salary").alias("nm","sal"))
df5.show(10,False)


---- arrays_zip() --



