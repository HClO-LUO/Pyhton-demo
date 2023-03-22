import imageio
import glob
import numpy
import matplotlib.pyplot

our_own_dataset = []

for image_file_name in glob.glob('5.png'):
    print("加载文件：", image_file_name)
    # 使用文件名设置正确的标签
    label = int(image_file_name[-5:-4])
    # 将png文件图像转为数组
    img_array = imageio.imread(image_file_name, as_gray=True)
    # 每张图片都由一个28 ×28 的矩阵表示，每张图片都由一个784 维的向量表示（28*28=784）
    # 将数组的值减去了255.0。常规而言，0指的是黑色，255指的是白色，但是，MNIST数据集使用相反的方式表示，因此将值逆转过来以匹配MNIST数据
    # 从28x28重塑到包含784个值的列表，反转值
    img_data = 255.0 - img_array.reshape(784)
    # 然后将数据缩放到范围从0.01到1.0
    img_data = (img_data / 255.0 * 0.99) + 0.01
    print(numpy.min(img_data))
    print(numpy.max(img_data))
    # 附加标签和图像数据来测试数据集
    record = numpy.append(label, img_data)
    print(record)
    our_own_dataset.append(record)
    pass

matplotlib.pyplot.imshow(our_own_dataset[0][1:].reshape(28, 28), cmap='Greys', interpolation='None')

print(our_own_dataset[0])
print("识别结果为：", record[0])
print(record[0])