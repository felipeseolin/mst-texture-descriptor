import os

location = '/Users/seolin/Downloads/USPtex/images'
images = sorted(os.listdir(location))
last_class_name = ""
counter = 1

print(f'Começando a renomear {len(images)} imagens...')
for acc, image in enumerate(images):
    if os.path.isdir(image):
        continue

    image_name = image.split('_')[0].replace('c', '')
    if image_name.startswith("c0"):
        image_name = image_name.replace('0', '', 1)

    class_name = image_name.zfill(3)

    if last_class_name != class_name and acc != 0:
        counter = 1

    new_name = f"{class_name}_{str(counter).zfill(6)}.png"
    print(image + ' -> ' + new_name)

    os.rename(f"{location}/{image}", f"{location}/{new_name}")

    counter += 1
    last_class_name = class_name

print("Finalizou!!")
