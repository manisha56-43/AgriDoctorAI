import os
import kagglehub

dataset_path = kagglehub.dataset_download("emmarex/plantdisease")
plant_path = os.path.join(dataset_path, "PlantVillage")

print("Checking each item:\n")

for item in os.listdir(plant_path):
    full_path = os.path.join(plant_path, item)

    if os.path.isdir(full_path):
        image_count = len(os.listdir(full_path))
        print(f"{item} --> {image_count} files")