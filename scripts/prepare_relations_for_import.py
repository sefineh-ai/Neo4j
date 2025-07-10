import os
import pandas as pd # type: ignore
import numpy as np # type: ignore

directory_path = "data/relations"
for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_name = os.path.join(root, file)
        df = pd.read_csv(file_name, on_bad_lines='skip')
        df = df.rename(columns={df.columns[0]:"start_id", df.columns[1]:"end_id"})
        df['type'] = "ASSOCIATED_WITH"
        df.to_csv(file_name, index=False)
        
        