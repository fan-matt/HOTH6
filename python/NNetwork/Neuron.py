import random


class Neuron:
    # Sets bias and activation to 0
    # No connections
    def __init__(self):
        self.bias = 0
        self.activation = 0
        self.connections = []   
        # No need for connection object
        # Just use them in order, from top to bottom
    

    # Takes raw input and bias and pipes it through a sigmoid
    # Also sets the activation to the output of the sigmoid
    def rawInput(self , input):
        self.activation = self.sigmoid(input - self.bias)


    # Standard sigmoid function
    def sigmoid(self , input):
        e = 2.71828
        return (1 / (1 + e ** -input))


    # Adds a connection to the neuron. A connection is just the value
    # of a bias- the neuron doesn't need to know what comes before
    # or after it
    def addConnection(self):
        self.connections.append(random.uniform(-1 , 1))


    # Prints out all the properties of the neuron
    def print(self):
        print("-- Neuron -- ")
        print("Activation: " + str(self.activation))
        print("Bias: " + str(self.bias))
        print("Connections: ")
        print(self.connections)
        print()