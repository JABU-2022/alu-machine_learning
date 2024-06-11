#!/usr/bin/env python3

import numpy as np
import tensorflow as tf

class SelfAttention(tf.keras.layers.Layer):
    """Self-attention layer"""

    def __init__(self, units):
        super(SelfAttention, self).__init__()
        """Initialize the layer with the given units"""

        if type(units) is not int:
            raise TypeError("units must be int representing the number of hidden units")
        self.W = tf.keras.layers.Dense(units=units)
        self.U = tf.keras.layers.Dense(units=units)
        self.V = tf.keras.layers.Dense(units=1)

    def call(self, s_prev, hidden_states):
        """
        Compute the context and attention weights
        s_prev - tensor of shape (batch, units) representing the previous decoder hidden state
        hidden_states - tensor of shape (batch, input_seq_len, units) representing the encoder outputs
        returns: context, weights
        """
        W = self.W(tf.expand_dims(s_prev, 1))
        U = self.U(hidden_states)
        V = self.V(tf.nn.tanh(W + U))
        weights = tf.nn.softmax(V, axis=1)
        context = tf.reduce_sum(weights * hidden_states, axis=1)

        return context, weights

# Testing the SelfAttention class
attention = SelfAttention(256)
print(attention.W)
print(attention.U)
print(attention.V)

s_prev = tf.convert_to_tensor(np.random.uniform(size=(32, 256)), preferred_dtype='float32')
hidden_states = tf.convert_to_tensor(np.random.uniform(size=(32, 10, 256)), preferred_dtype='float32')
context, weights = attention(s_prev, hidden_states)
print(context)
print(weights)
