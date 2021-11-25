import os

location = '/Users/seolin/Downloads/DatasetImages/Train'
target_location = '/Users/seolin/Downloads/DatasetImages/TrainConverted'
image_folders = sorted(os.listdir(location))

print(f'Começando a renomear {len(image_folders)}....')
for folder in image_folders:
    if os.path.isfile(folder) or folder == '.DS_Store' or folder.startswith('.'):
        continue

    print(f'Renomeando pasta "{folder}"...')
    class_name = folder[:3].upper()
    image_folder_location = f'{location}/{folder}'
    images = sorted(os.listdir(image_folder_location))

    acc = 0
    for image in images:
        if os.path.isdir(image) or image == '.DS_Store' or image.startswith('.'):
            continue

        new_name = f"{class_name}_{str(acc + 1).zfill(6)}.png"
        print(image + ' -> ' + new_name)

        os.rename(f"{image_folder_location}/{image}", f"{target_location}/{new_name}")

        acc += 1

    print(f'Pasta "{folder}" renomeada!\n')

print("Finalizou!!")

