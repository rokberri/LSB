from PIL import Image, ImageFilter
import numpy as np

def max_absolute_deviation(origin, new_img):
    array1 = np.array(origin)
    array2 = np.array(new_img)

    absolute_diff = np.abs(array1 - array2)

    max_deviation = np.max(absolute_diff)

    return max_deviation

def root_mean_square_deviation(origin, new_img):
    array1 = np.array(origin)
    array2 = np.array(new_img)

    square_diff = (array1 - array2) ** 2

    mean_square_diff = np.mean(square_diff)

    rmsd = np.sqrt(mean_square_diff)

    return rmsd

def normalized_root_mean_square_deviation(origin, new_img):

    array1 = np.array(origin)
    array2 = np.array(new_img)

    rmsd = np.sqrt(np.mean((array1 - array2) ** 2))

    nrmse = rmsd / (np.max(array1) - np.min(array1))

    return nrmse

def snr(origin, new_img):
    array1 = np.array(origin)
    array2 = np.array(new_img)

    diff = array1 - array2

    signal_power = np.mean(array1) ** 2

    noise_power = np.mean(diff ** 2)

    snr = 10 * np.log10(signal_power / noise_power)

    return snr

def minkowski_distance(origin, new_img, p=2):
    array1 = np.array(origin)
    array2 = np.array(new_img)

    diff = np.abs(array1 - array2)

    distance = np.sum(diff ** p) ** (1/p)

    return distance

def laplacian_rmse(origin, new_img):
    array1 = np.array(origin)
    array2 = np.array(new_img)

    laplacian1 = Image.fromarray(array1).filter(ImageFilter.LAPLACIAN)
    laplacian2 = Image.fromarray(array2).filter(ImageFilter.LAPLACIAN)

    square_diff = np.square(np.array(laplacian1) - np.array(laplacian2))

    rmse = np.sqrt(np.mean(square_diff))

    return rmse

def psnr(origin, new_img):
    array1 = np.array(origin, dtype=np.float32)
    array2 = np.array(new_img, dtype=np.float32)

    diff = array1 - array2
    mse = np.mean(diff ** 2)

    max_intensity = 255

    if mse == 0:
        return float('inf')
    psnr_value = 20 * np.log10(max_intensity / np.sqrt(mse))

    return psnr_value