import os

directory_path = "data/csv_files"
output_file = "ids.txt"

try:
    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.csv'):
                    name = os.path.splitext(file)[0]
                    formatted_name = f"{name}_id"
                    f.write(formatted_name + "\n")
except Exception as e:
    print(f"Failed to write to '{output_file}': {e}")

print(f"IDs saved to '{output_file}'")
