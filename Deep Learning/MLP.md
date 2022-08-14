---
    title: Multiple Layer Perceptron
    update: 2022-08-14
---



# *MLP (Multiple Layer Perceptron)*
![](images/mlp.png)

*Back Propagation:*

$\delta^L$ =  $\nabla_a C\odot\sigma^{'} (Z^L)$

$\delta^l$ =  $((W^{l+1})^{T}\delta^{l+1})\odot\sigma^{'} (Z^l)$

$\frac{\partial C}{\partial W_{jk}^l}$ = $a_k^{l-1}\delta_j^l$

$\frac{\partial C}{\partial b^l}$ = $\delta_j^l$

![](images/mlp-1.jpg)