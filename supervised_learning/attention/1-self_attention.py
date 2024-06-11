#!/usr/bin/env python3

"""
This module contains a class SelfAttention for implementing
a self-attention mechanism in a neural network.
"""

import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    """Class SelfAttention implementing self-attention mechanism."""

    def __init__(self, units):
        """
        Initialize the layer.

        Args:
        units (int): Number of hidden units in the alignment model.
        """
        super(SelfAttention, self).__init__()

        if not isinstance(units, int):
            raise TypeError("units must be an int representing the number of hidden units")
        
        self.W = tf.keras.layers.Dense(units=units)
        self.U = tf.keras.layers.Dense(units=units)
        self.V = tf.keras.layers.Dense(units=1)

    def call(self, s_prev, hidden_states):
        """
        Compute the context vector and attention weights.

        Args:
        s_prev (tf.Tensor): Tensor of shape (batch, units) representing the previous decoder hidden state.
        hidden_states (tf.Tensor): Tensor of shape (batch, input_seq_len, units) representing the encoder outputs.

        Returns:
        context (tf.Tensor): Tensor of shape (batch, units) representing the context vector.
        weights (tf.Tensor): Tensor of shape (batch, input_seq_len, 1) representing the attention weights.
        """
        s_prev_expanded = tf.expand_dims(s_prev, 1)
        W_s_prev = self.W(s_prev_expanded)
        U_hidden_states = self.U(hidden_states)
        V_tanh = tf.nn.tanh(W_s_prev + U_hidden_states)
        weights = tf.nn.softmax(self.V(V_tanh), axis=1)
        context = tf.reduce_sum(weights * hidden_states, axis=1)

        return context, weights


# Testing the SelfAttention class
if __name__ == "__main__":
    attention = SelfAttention(256)
    print("W:", attention.W)
    print("U:", attention.U)
    print("V:", attention.V)

    s_prev = tf.random.uniform((32, 256), dtype=tf.float32)
    hidden_states = tf.random.uniform((32, 10, 256), dtype=tf.float32)
    context, weights = attention(s_prev, hidden_states)
    print("Context:", context)
    print("Weights:", weights)
