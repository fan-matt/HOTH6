import random


class Neuron:

    # Connection to another Neuron. Connections are
    # 1 way- they can only propagate forward
    class Connection:
        # Creates a connection object with a given
        # connecting neuron and connection weight
        # THIS DOES NOT BIND THE CONNECTION TO ANYTHING
        def __init__(self , neuron , weight):
            self.neuron = neuron
            self.weight = weight

        
        # Prints out all the properties of the connection, but
        # not the connected neuron
        def print(self):
            print("-- Connection --")
            print("Weight: " + str(self.weight))
            print()


    # Sets bias and activation to 0
    # No connections, no input
    def __init__(self):
        self.bias = 0
        self.activation = 0
        self.connections = []   
        self.rawInput = 0
    

    # Adds the input to this neuron's raw input
    def addToRawInput(self , input):
        self.rawInput += input


    # Takes raw input and bias and pipes it through a sigmoid
    # and sets the activation to the output of the sigmoid
    #
    # Call this AFTER all necessary propagation is done!
    def activate(self):
        self.activation = self.sigmoid(self.rawInput - self.bias)
        self.rawInput = 0


    # Standard sigmoid function
    def sigmoid(self , input):
        e = 2.71828
        return (1 / (1 + e ** -input))


    # Adds a connection to the neuron
    def addConnection(self , neuron):
        self.connections.append(self.Connection(neuron , random.uniform(-1 , 1)))


    # Sends a value to each connection
    # This value is this activation times the connection weight
    def propagate(self):
        for i in self.connections:
            i.neuron.addToRawInput(self.activation * i.weight)


    # Prints out all the properties of the neuron
    def print(self):
        print("-- Neuron -- ")
        print("Activation: " + str(self.activation))
        print("Bias: " + str(self.bias))
        print("Connections: ")
        for i in self.connections:
            i.print()
        print()