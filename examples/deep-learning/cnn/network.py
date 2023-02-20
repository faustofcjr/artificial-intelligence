"""
network1.py

That script is based on http://neuralnetworksanddeeplearning.com/ book, with the author's permission

This class implements a neural network with learning based on the Stochastic Gradient Descent algorithm for a feedforward neural network.
Gradients are calculated using backpropagation.

Note that this is simple, easily readable and easily modifiable code. It is not optimized and omits many desirable features.
"""

import random
import numpy as np


class Network(object):

    def __init__(self, sizes):
        """
        The `sizes` list contains the number of neurons in the respective layers of the network.
        For example, if the list is [2, 3, 1] then it will be a three-layer network, with the first
        layer containing 2 neurons, the second layer 3 neurons, and the third layer 1 neuron. 
        
        The biases and weights for the network are initialized randomly, using a Gaussian distribution
        with mean 0 and variance 1.
        
        Note that the first layer is assumed to be an input layer, and by convention we did not
        define any bias for these neurons, as biases are used computing the outputs of the later layers.
        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        

    def feedforward(self, a):
        """
        Returns the network output if `a` is input.
        """
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
            
        return a
    

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        """
        Train the neural network using stochastic mini-batch gradient descent. 
        
        The `training_data` is a list of tuples `(x, y)` representing the training inputs and the 
        outputs. The other non-optional parameters are self-explanatory. 
        
        If `test_data` is given, then the network will be evaluated against the test data after each epoch
        and partial progress printed. This is useful for track progress, but slows things down substantially.
         """

        training_data = list(training_data)
        n = len(training_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k : k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            
            if test_data:
                print("Epoch {} : {} / {}".format(j,self.evaluate(test_data),n_test));
            else:
                print("Epoch {} finalizada".format(j))

                
    def update_mini_batch(self, mini_batch, eta):
        """
        Updates the weights and bias of the network by applying gradient descent using backpropagation
        for a single mini-batch.
        
        The `mini_batch` is a list of `(x, y)` tuples, and `eta` is the learning rate.
         """

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        
        self.weights = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)]

        
    def backprop(self, x, y):
        """
        Returns a `(nabla_b, nabla_w)` tuple representing the gradient for the C_x cost function. 
        `nabla_b` and `nabla_w` are layer lists of numpy arrays, similar to `self.biases` and `self.weights`.
        """

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        
        # Feedforward
        activation = x

        # Lista para armazenar todas as ativações, camada por camada
        activations = [x] 

        # Lista para armazenar todos os vetores z, camada por camada
        zs = [] 

        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        
        # Backward pass
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        
        # Aqui, l = 1 significa a última camada de neurônios, l = 2 é a
        # segunda e assim por diante. 
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    
    def evaluate(self, test_data):
        """Retorna o número de entradas de teste para as quais a rede neural 
         produz o resultado correto. Note que a saída da rede neural
         é considerada o índice de qualquer que seja
         neurônio na camada final que tenha a maior ativação."""

        test_results = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """Retorna o vetor das derivadas parciais."""
        return (output_activations-y)


def sigmoid(z):
    """
    Sigmoid activation function.
    """
    return 1.0/(1.0+np.exp(-z))


def sigmoid_prime(z):
    """
    Return the derivatives of the Sigmoid function
    """
    return sigmoid(z)*(1-sigmoid(z))