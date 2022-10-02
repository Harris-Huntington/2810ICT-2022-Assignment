import pandas as pd
import re

stats = pd.read_csv('C:/Users/ericm/Documents/SoftwareTech/AssignmentPartB/data/Crash Statistics Victoria.csv', index_col=0)
code = stats['DCA_CODE'].unique()


print(code, sep="\n", end="\n")