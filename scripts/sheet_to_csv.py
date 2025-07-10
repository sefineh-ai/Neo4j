import os
import pandas as pd # type: ignore

excel_folder = "data/excel"
csv_folder = "data/csv"
os.makedirs(csv_folder, exist_ok=True)

for excel_file in os.listdir(excel_folder):
    if excel_file.endswith(".xlsx"):
        excel_path = os.path.join(excel_folder, excel_file)
        csv_file = os.path.join(csv_folder, f"{os.path.splitext(excel_file)[0]}.csv")
        df = pd.read_excel(excel_path)
        df.to_csv(csv_file, index=False)
        
        print(f"Excel file '{excel_file}' has been converted to CSV as '{csv_file}'.")
