---
    title: Deep Learning
    date: 2022-07-15
---


# *MLP (Multiple Layer Perceptron)*
![](images/mlp.png)

*Back Propagation:*

$\delta^L$ =  $\nabla_a C\odot\sigma^{'} (Z^L)$

$\delta^l$ =  $((W^{l+1})^{T}\delta^{l+1})\odot\sigma^{'} (Z^l)$

$\frac{\partial C}{\partial W_{jk}^l}$ = $a_k^{l-1}\delta_j^l$

$\frac{\partial C}{\partial b^l}$ = $\delta_j^l$

![](images/mlp-1.jpg)

# *RNN (Recurrent Neural Network)*
![](images/rnn.png)
![](images/rnn-1.jpg)

# *LSTM (Long Short-Term Memory)*
*Back Propagation Through Time*
![](images/lstm.jpg)

# *GRU (Gate Recurrent Unit)*
![](images/gru.png)
*Back Propagation Through Time*
![](images/gru-1.jpg)

