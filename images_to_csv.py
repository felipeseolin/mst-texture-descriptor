from glob import glob
from image_to_graph import image_to_mst
from open_image import open_image
from extract_values import extract_values
from csv import DictWriter


def image_to_csv(dir='/mnt/5022A63622A620C8/TCC/tests/datasets/kylberg-texture-dataset/images/*.png'):
    images = glob(dir)
    dic = []
    print(f"Iniciando extração de {len(images)} imagens...")
    for i, image in enumerate(images):
        print(f"- Imagem {i + 1}")

        file_name = get_file_name(image)
        image_class = get_image_class(file_name)

        image = open_image(image)
        mst, g = image_to_mst(image)

        values = extract_values(mst.es['weight'])
        values['class'] = image_class

        dic.append(values)

    print('Salvando arquivo CSV...')
    save_csv(dic)
    print('Finalizado: arquivo salvo em: /mnt/5022A63622A620C8/TCC/tests/mst.csv')


def save_csv(dic, csv_file='/mnt/5022A63622A620C8/TCC/tests/mst.csv'):
    cols = ['averate', 'standard_deviation', 'skew', 'kurtosis', 'entropy']
    try:
        with open(csv_file, 'w') as csvfile:
            writer = DictWriter(csvfile, fieldnames=cols)
            writer.writeheader()
            for row in dic:
                writer.writerow(row)
    except IOError:
        print("I/O error")


def get_file_name(path):
    return path.split('/')[-1]


def get_image_class(image_file_name):
    return image_file_name.split('_')[0]


if __name__:
    image_to_csv()
