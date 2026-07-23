import kagglehub

# Download the PlantVillage dataset
path = kagglehub.dataset_download("emmarex/plantdisease")

print("Dataset downloaded successfully!")
print("Dataset location:", path)