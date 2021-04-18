import pandas as pd
import sys
import os

path_without_extention = os.path.splitext(sys.argv[1])[0]

data = pd.read_json(sys.argv[1], lines=True)
data.to_csv(path_without_extention + ".csv",index=False)