import os
import shutil
import csv

folder_path = os.path.join(os.getcwd(), "dataSet_train")
input_folder_path = os.path.join(folder_path, 'input')
output_folder_path = os.path.join(folder_path, 'output')
training_folder_path = os.path.join(folder_path, 'training')
dataset_csv = os.path.join(folder_path, "data.csv")


def create_folder_if_not_exist(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


create_folder_if_not_exist(folder_path)
create_folder_if_not_exist(input_folder_path)
create_folder_if_not_exist(output_folder_path)
create_folder_if_not_exist(training_folder_path)
rows = []
for root, dirs, files in os.walk("Dataset"):
    path = root.split(os.sep)
    print(root)
    for file in files:
        if file.endswith(".tif"):
            file_path = os.path.join(os.getcwd(), root, file)
            if file.find("_mask") > 0:
                dest = os.path.join(output_folder_path, file)
            else:
                dest = os.path.join(input_folder_path, file)
                rows.append(file)
            shutil.copyfile(file_path, dest)

fields = ["X", "Y"]
print(rows)
with open(dataset_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for file in rows:
        orig = os.path.join(input_folder_path, file)
        masked = os.path.join(output_folder_path,
                              file.replace(".tif", "_mask.tif"))
        csvwriter.writerow([
            orig, masked
        ])
