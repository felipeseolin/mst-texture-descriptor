from skimage import io


def open_image(filename):
    return io.imread(filename, as_gray=True)
