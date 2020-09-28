import numpy as np
import tensorflow as tf

'''Problema XOR'''
'''
   A  B   A XOR B
   0  0      0
   0  1      1
   1  0      1
   1  1      0
              '''

'''tabela contendo os valores de entrada e saída.'''
binary_i = np.array([[0,0], [0,1], [1,0], [1,1]])
binary_o = np.array([[0], [1], [1], [0]])

'''criar dois tensores, que serão alimentados durante o treino com os valores de entrada e saída.'''
X = tf.placeholder(tf.float32, shape=(None, 2), name="X")
y = tf.placeholder(tf.float32, shape=(None, 1), name="y")

'''definir a estrutura da rede neural.'''
n_inputs = 2 #CAMADAS DE ENTRADA
n_hidden1 = 3 #CAMADAS OCULTAS
n_outputs = 1 #CAMADAS DE SAÍDA

hidden1 = tf.layers.dense(X, n_hidden1, name="hidden1-new",
                          activation=tf.nn.sigmoid)
logits = tf.layers.dense(hidden1, n_outputs, name="outputs-new")

'''definir qual algoritmo de treinamento que será usado.'''
eta = 0.1 # APRENDIZAGEM (0.1 = 10%)
n_epochs = 500 # QUANTIDADE DE REPETIÇÕES DE TREINO (GERAÇÕES)

cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y))
#train = tf.train.AdamOptimizer(eta).minimize(cost)
optimizer = tf.train.AdamOptimizer(eta)
training_op = optimizer.minimize(cost)

'''função de custo: MSE(Mean Square Error(Erro Quadrático Médio) e para treinamento: Algoritmo Adam Optimization
(Método Adam de Descida do Gradiente Estocástico).'''

'''Fase de Treinamento:'''
pred = tf.nn.sigmoid(logits)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(n_epochs):
        sess.run(training_op, feed_dict={X: binary_i, y: binary_o})
    print("Treino completo!")

    prediction = sess.run(pred, feed_dict={X: binary_i})
    print("Porcentagem: ")
    print(prediction)
    print("Arredondando")
    print(np.round(prediction))