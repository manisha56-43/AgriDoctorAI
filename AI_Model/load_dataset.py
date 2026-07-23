import os
import kagglehub
import tensorflow as tf

# Download (uses cached copy if already downloaded)
dataset_path = kagglehub.dataset_download("emmarex/plantdisease")

# Path to the PlantVillage folder
plant_path = os.path.join(dataset_path, "PlantVillage", "PlantVillage")
# Load dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    plant_path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(224, 224),
    batch_size=32
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    plant_path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(224, 224),
    batch_size=32
)

print("\n✅ Dataset Loaded Successfully!")

print("\nClasses:")
print(train_dataset.class_names)

print("\nNumber of Classes:", len(train_dataset.class_names))
