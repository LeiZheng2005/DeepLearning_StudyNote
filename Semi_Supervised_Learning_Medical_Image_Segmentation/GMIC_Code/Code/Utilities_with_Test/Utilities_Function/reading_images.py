import numpy as np
import imageio
import h5py

# 两个读取图像的函数，第一个用于读取png格式的图片
def read_image_png(file_name):
    image=np.array(imageio.imread(file_name))
    return image

def read_image_mat(file_name):
    data=h5py.File(file_name,'r')
    image=np.array(data['image']).T
    data.close()
    return image