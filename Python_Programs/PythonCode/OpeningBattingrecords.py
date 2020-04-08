import pandas as pd
import numpy as np

data = pd.read_html("https://stats.espncricinfo.com/ci/content/records/283512.html")
print(data.head())
