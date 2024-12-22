import os
import requests
import random

IMAGE_SOURCE_URL = "https://picsum.photos/200/300"

BASE_DIR = "random_images"

os.makedirs(BASE_DIR, exist_ok=True)

for i in range(1, 11):
    folder_name = os.path.join(BASE_DIR, f"folder_{i}")
    os.makedirs(folder_name, exist_ok=True)

    response = requests.get(IMAGE_SOURCE_URL)
    if response.status_code == 200:
        image_path = os.path.join(folder_name, f"image_{i}.jpg")
        with open(image_path, "wb") as image_file:
            image_file.write(response.content)
        print(f"Изображение сохранено: {image_path}")
    else:
        print(f"Не удалось загрузить изображение {i}, код ошибки: {response.status_code}")

print("Загрузка завершена.")
