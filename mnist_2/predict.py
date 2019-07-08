# coding: utf-8
import sys, os, io
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.layers import *
from deep_convnet import DeepConvNet
import random
from PIL import Image
import cv2


net = DeepConvNet()
net.load_params("deep_convnet_params.pkl")
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# img = cv2.imread("tmp.jpg")
# img = cv2.resize(img, (28,28))
# img = img.astype(np.float)
# img /= 255
# img = np.array(img).reshape(1,1,28,28)

print(random.choice(t_test))
img = random.choice(x_test)
img = np.reshape(img,(1,1,28,28))
# img = np.array(img)
# cv2.imshow('image', img)
plt.imshow(img)
num = net.predict(img)
print(np.argmax(num.data))
cv2.waitKey(0)
cv2.destroyAllWindows()