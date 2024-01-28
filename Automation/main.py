import os
import pandas as pd

path = "FilePath"
files = os.listdir(path)
print(files)

consolidated_table = pd.DataFrame()

for file_name in files:
  sales_table = pd.read_csv()
  print(file_name)
 