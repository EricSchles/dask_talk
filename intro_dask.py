#Documentation: http://dask.pydata.org/en/latest/
#Installation: pip install dask
#Where to find data: https://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public

import time
import pandas as pd
import dask.dataframe as dd

start = time.time()
df = pd.read_csv("data/accident.csv")
result = df.groupby(df.CITY).mean()
import code
code.interact(local=locals())
print("Average number of accidents:",result," per city")
print("took",time.time() - start,"seconds")

start = time.time()
df = dd.read_csv("data/accident.csv")
result = df.groupby(df.CITY).mean().compute()
print("Average number of accidents:",result," per city")
print("took",time.time() - start,"seconds")



