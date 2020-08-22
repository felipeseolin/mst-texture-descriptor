from glob import glob
from image_to_graph import image_to_mst
from open_image import open_image
from extract_values import extract_values
from csv import DictWriter


def image_to_csv(dir='/mnt/5022A63622A620C8/TCC/tests/datasets/KylbergTextureDataset/*.png'):
    images = glob(dir)
    dic = []
    print(f"Iniciando extração de {len(images)} imagens...")
    for i, image in enumerate(images):
        print(f"- Imagem {i + 1}")
        image = open_image(image)
        mst, g = image_to_mst(image)
        dic.append(extract_values(mst.es['weight']))
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


if __name__:
    image_to_csv()
