
# --- Modeli dahil etme --- #

from keras.models import load_model

model = load_model("asd.h5")
print(model.summary())

# --- Test resmi normalize işlemi --- #

img_path = "dog.jpg"

# resmi 4B tensör olarak işleme
from keras.preprocessing import image
import numpy as np

img = image.load_img(img_path, target_size=(150, 150))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis=0)
img_tensor /= 255.

# tensör şekli (1, 150, 150, 3)
print(img_tensor.shape)

import matplotlib.pyplot as plt

plt.imshow(img_tensor[0])
plt.title("Test resmi")
plt.show()

# --- Girdi ve çıktı tensörü listesinden model oluşturmak --- #

from keras import models

layer_outputs = [layer.output for layer in model.layers[:8]] # ilk sekiz katman çıktısı

activation_model = models.Model(inputs=model.input, outputs=layer_outputs) # verilen model bilgisine göre çıktı dödürür

# --- Modeli tahmin modunda çalıltırma --- #

activations = activation_model.predict(img_tensor) # her katman aktivasyonu için numpy dizisi döndürür.

first_layer_activation = activations[0]
print("Test resmine ilk evrişimli katmanın aktivasyonları : ",first_layer_activation.shape)

# --- kanaları görselleştirme --- #

import matplotlib.pyplot as plt

plt.matshow(first_layer_activation[0, :, :, 5], cmap="viridis")
plt.title("ilk katmanın besinci kanalı")
plt.show()

plt.matshow(first_layer_activation[0, :, :, 26], cmap="viridis")
plt.title("ilk katmanın yirmialtıncı kanalı")
plt.show()

# --- Tüm kanalların tüm aktivasyonlarını görselleştirme --- #

import keras

# These are the names of the layers, so can have them as part of our plot
layer_names = []
for layer in model.layers[:8]:
    layer_names.append(layer.name)

images_per_row = 16

# nitelik haritaları
for layer_name, layer_activation in zip(layer_names, activations):

    n_features = layer_activation.shape[-1]


    size = layer_activation.shape[1]

    # aktivasyon katmanlarını bu matris üzerine döşer
    n_cols = n_features // images_per_row
    display_grid = np.zeros((size * n_cols, images_per_row * size))

    # tüm flitreleri yatayda döşer
    for col in range(n_cols):
       
        for row in range(images_per_row):
            
            channel_image = layer_activation[0,
                                             :, :,
                                             col * images_per_row + row]
            # niteliklerin görsel olarak daha iyi görünmesi
            channel_image -= channel_image.mean()
            channel_image /= channel_image.std()
            channel_image *= 64
            channel_image += 128
            channel_image = np.clip(channel_image, 0, 255).astype("uint8")
            display_grid[col * size : (col + 1) * size,
                         row * size : (row + 1) * size] = channel_image


    scale = 1. / size
    plt.figure(figsize=(scale * display_grid.shape[1],
                        scale * display_grid.shape[0]))
    plt.title(layer_name)
    plt.grid(False)
    plt.imshow(display_grid, aspect='auto', cmap="viridis")
    
plt.show()

# --- Filitre görselleştirme oluşturmak için --- #

from keras.applications import VGG16
from keras import backend as K

model = VGG16(weights='imagenet',
              include_top=False)

layer_name = 'block3_conv1'
filter_index = 0

layer_output = model.get_layer(layer_name).output
loss = K.mean(layer_output[:, :, :, filter_index])

# girdi için kaybın gradyanını almak
grads = K.gradients(loss, model.input)[0]

# sıfıra bölme hatası almamak için
grads /= (K.sqrt(K.mean(K.square(grads))) + 1e-5)

iterate = K.function([model.input], [loss, grads])

import numpy as np
loss_value, grads_value = iterate([np.zeros((1, 150, 150, 3))])


# resme bir miktar gürültü ekleme
input_img_data = np.random.random((1, 150, 150, 3)) * 20 + 128.

# gradyan 40 defa çalışır
step = 1.  # gradyan güncelleme şiddeti

for i in range(40):

    loss_value, grads_value = iterate([input_img_data])

    input_img_data += grads_value * step


def deprocess_image(x):
    # tensörü normalize etme
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1


    x += 0.5
    x = np.clip(x, 0, 1)

    # RGB
    x *= 255
    x = np.clip(x, 0, 255).astype('uint8')
    return x

def generate_pattern(layer_name, filter_index, size=150):

    # katmanın n. filitresininaktivasyonunu en büyülten kayıp fonk. oluşturur.

    layer_output = model.get_layer(layer_name).output
    loss = K.mean(layer_output[:, :, :, filter_index])

    # girdinin bu kayba göre gradyanı
    grads = K.gradients(loss, model.input)[0]

    # normalizasyon hilesi
    grads /= (K.sqrt(K.mean(K.square(grads))) + 1e-5)

    # This function returns the loss and grads given the input picture
    iterate = K.function([model.input], [loss, grads])
    
   
    input_img_data = np.random.random((1, size, size, 3)) * 20 + 128.

    # 40 gradyan inişi
    step = 1.
    for i in range(40):
        loss_value, grads_value = iterate([input_img_data])
        input_img_data += grads_value * step
        
    img = input_img_data[0]
    return deprocess_image(img)


plt.imshow(generate_pattern('block4_conv1', 0))
plt.title("block4_conv1 filitresi görselleştirme")
plt.show()

# --- Bir katmandaki tüm filitre çıktılarını oluşturma --- #
"""
for i in ['block1_conv1', 'block2_conv1', 'block3_conv1','block4_conv1']:

	for c in range(0,16):

		plt.imshow(generate_pattern(i, c))
		plt.show()


"""
# -------------      Sınıf aktivasyon ısı haritası görselleştirme     ------------- #

from keras.applications.vgg16 import VGG16

K.clear_session()


model = VGG16(weights='imagenet') # eğitilmiş model

# --- Resme ön işlem yapmak --- #

from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np


img_path = 'dog.jpg'


img = image.load_img(img_path, target_size=(224, 224))


x = image.img_to_array(img)


x = np.expand_dims(x, axis=0)

x = preprocess_input(x)


preds = model.predict(x) # model resimdeki köpeğin türünü Labrador_retriever olarak buldu
print('Predicted:', decode_predictions(preds, top=3)[0])

# --- Grad-CAM algoritması --- #

dog_output = model.output[:, 386]


# katman çıktı nitelik haritası
last_conv_layer = model.get_layer('block5_conv3')

# çıktıya göre gradyan
grads = K.gradients(dog_output, last_conv_layer.output)[0]


pooled_grads = K.mean(grads, axis=(0, 1, 2))

iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])

pooled_grads_value, conv_layer_output_value = iterate([x])

for i in range(512):
    conv_layer_output_value[:, :, i] *= pooled_grads_value[i]


heatmap = np.mean(conv_layer_output_value, axis=-1)


# --- Isı haritası --- #

heatmap = np.maximum(heatmap, 0)
heatmap /= np.max(heatmap)
plt.matshow(heatmap)
plt.show()

# --- Resme ısı haritasını ekleme --- #

import cv2


img = cv2.imread(img_path)


heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))


heatmap = np.uint8(255 * heatmap)

heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)


superimposed_img = heatmap * 0.4 + img

# Save the image to disk

cv2.imwrite("ga/asd.jpg", superimposed_img)

