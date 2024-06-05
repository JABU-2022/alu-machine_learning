#!/usr/bin/env python3

import tensorflow as tf

class RNNEncoder(tf.keras.layers.Layer):
    def __init__(self, vocab, embedding, units, batch):
        super(RNNEncoder, self).__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(vocab, embedding)
        self.gru = tf.keras.layers.GRU(units,
                                       return_sequences=True,
                                       return_state=True,
                                       recurrent_initializer='glorot_uniform')

    def initialize_hidden_state(self):
        return tf.zeros((self.batch, self.units))

    def call(self, x, initial):
        x = self.embedding(x)
        outputs, hidden = self.gru(x, initial_state=initial)
        return outputs, hidden

if __name__ == "__main__":
    import numpy as np

    encoder = RNNEncoder(1024, 128, 256, 32)
    print(encoder.batch)
    print(encoder.units)
    print(type(encoder.embedding))
    print(type(encoder.gru))

    initial = encoder.initialize_hidden_state()
    print(initial)
    x = tf.convert_to_tensor(np.random.choice(1024, 320).reshape((32, 10)))
    outputs, hidden = encoder(x, initial)
    print(outputs)
    print(hidden)
