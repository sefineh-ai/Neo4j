# import os 
# import numpy as np # type: ignore
# import pandas as pd  # type: ignore

# directory_path = "data/nodes"
# all_files = []
# file_names = []
# for root, dirs, files in os.walk(directory_path):
#     for file in files:
#         all_files.append(os.path.join(root, file))
#         file_names.append(file)

# with open('ids.txt', "r") as ids_file:
#     ids = ids_file.readlines()
#     ids = set([id.replace("\n", "") for id in ids])

# for csv_file_name, file_name in zip(all_files, file_names):
#     try:
#         df = pd.read_csv(
#         csv_file_name,
#         encoding='utf-8',
#         on_bad_lines="skip", 
#         delimiter=",",       
#         na_values=['', ' '], 
#         keep_default_na=True,
#         skipinitialspace=True)
#         columns = df.columns.tolist()
#         cols_to_exclude = ([column for column in columns if column in ids])
#         cols_to_exclude.append("id")
#         df_new = df.drop(columns = cols_to_exclude)
        
#     except:
#         continue
