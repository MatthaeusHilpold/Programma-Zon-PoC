import laspy
import tifffile

"""
    Reads an image in tiff format
    Args:
        source: a string containing the source path of the image
    Return:
        tiffimage: an image in tiff format
    """
def readtiff(source: str):
    try:
        tiffimage = tifffile.imread(source)
        print('succesfully read: ' + source)
        return tiffimage
    except:
        print('error while reading: ' + source)



if __name__ == "__main__":
    testtif = readtiff('../data/test.tif')
    print(testtif.shape)
    tifffile.imshow(testtif)
