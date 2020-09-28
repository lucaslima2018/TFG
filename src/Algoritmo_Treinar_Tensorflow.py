import numpy as np
import tensorflow as tf
from tensorflow.python.keras.layers import Input, Dense


entradas = tf.constant([0.72, 0.82, 0.92])
pesos = tf.constant([0.3, 0.8, 0.5])

tf.keras.metrics.Recall(
    thresholds=1, top_k=None, class_id=None, name=entradas, dtype=float
)

tf.keras.metrics.Recall(
    thresholds=1, top_k=None, class_id=None, name=pesos, dtype=float
)

for i in range(0,3):
    somatorio = somatorio + (entradas * pesos)


for i in range(0,10):
    treinar = tf.nn.sigmoid(somatorio)




with tf.Session() as sess:
    retorno1 = sess.run(entradas)
    print(retorno1)
    retorno2 = sess.run(pesos)
    print(retorno2)




