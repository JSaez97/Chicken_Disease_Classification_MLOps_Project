import os
import shutil
import pandas as pd
from pathlib import Path
from cnnClassifier.entity.config_entity import DataSortingConfig

class DataSorting:
    def sort_images(self, config: DataSortingConfig):
        # Leer el archivo CSV que contiene los nombres de las imágenes y las etiquetas
        df = pd.read_csv(config.source_csv)

        # Crear carpetas para cada clase en el directorio de salida
        classes = ['Salmonella', 'Coccidiosis', 'New_Castle_Disease', 'Healthy']
        for cls in classes:
            class_dir = os.path.join(config.output_dir, cls)
            os.makedirs(class_dir, exist_ok=True)

        # Copiar las imágenes en las carpetas correspondientes según las etiquetas
        for index, row in df.iterrows():
            img_filename = row['images']
            label = row['label']

            if "salmo" in img_filename or "pcrsalmo" in img_filename:
                dest_folder = "Salmonella"
            elif "cocci" in img_filename or "pcrcocci" in img_filename:
                dest_folder = "Coccidiosis"
            elif "ncd" in img_filename or "pcrncd" in img_filename:
                dest_folder = "New_Castle_Disease"
            elif "healthy" in img_filename or "pcrhealthy" in img_filename:
                dest_folder = "Healthy"
            else:
                print(f"Unrecognized image prefix in: {img_filename}")
                continue

            # Ajustar la ruta de la imagen de origen a la ubicación correcta
            src_path = os.path.join(config.artifacts_root, "data_ingestion", "chicken-fecal-images", img_filename)

            # Asegurarse de que la ruta de origen sea correcta
            if not os.path.exists(src_path):
                print(f"Source image not found: {src_path}")
                continue

            # Ruta de destino de la imagen
            dest_path = os.path.join(config.output_dir, dest_folder, img_filename)

            # Copiar la imagen al directorio de destino
            shutil.copy(src_path, dest_path)
            print(f"Copied {img_filename} to {dest_folder}")
        
    def transfer_and_clean_folders(self, data_sorting_config: DataSortingConfig):
        # Rutas
        source_root = data_sorting_config.output_dir  # Ruta de salida de data sorting
        target_root = Path('artifacts/data_ingestion/chicken-fecal-images')  # Ruta de destino

        # Nombres de las carpetas que queremos conservar
        target_folders = ["Coccidiosis", "Healthy", "New_Castle_Disease", "Salmonella"]

        # Transferir las carpetas
        for folder in target_folders:
            src_folder = os.path.join(source_root, folder)
            dest_folder = os.path.join(target_root, folder)

            # Verificar si la carpeta fuente existe antes de copiar
            if os.path.exists(src_folder):
                shutil.copytree(src_folder, dest_folder, dirs_exist_ok=True)
                print(f"Transferred {src_folder} to {dest_folder}")

        # Limpiar archivos que no están en las carpetas especificadas
        for item in os.listdir(target_root):
            if item not in target_folders:
                item_path = os.path.join(target_root, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)  # Eliminar directorios
                    print(f"Deleted directory: {item_path}")
                else:
                    os.remove(item_path)  # Eliminar archivos
                    print(f"Deleted file: {item_path}")
