import random


class Neuron:
    def __init__(self):
        self.bias = 0
        self.activation = 0
        self.connections = []   
        # No need for connection object
        # Just use them in order, from top to bottom
    

    def rawInput(self , input):
        self.activation = self.sigmoid(input - self.bias)


    def sigmoid(self , input):
        e = 2.71828
        return (1 / (1 + e ** -input))


    def addConnection(self):
        self.connections.append(random.uniform(-1 , 1))


    def print(self):
        print("-- Neuron -- ")
        print("Activation: " + str(self.activation))
        print("Bias: " + str(self.bias))
        print("Connections: ")
        print(self.connections)
        print()