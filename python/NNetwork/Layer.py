from Neuron import Neuron


class Layer: 

    # Creates a Layer of Neurons given the number of neurons (size)
    def __init__(self , size):
        self.size = size
        self.neurons = []
    
        for i in range(size):
            self.neurons.append(Neuron())


    # Connects this layer to another layer
    def connect(self , layer):
        for i in self.neurons:
            for j in layer.neurons:
                i.addConnection(j)


    # Propagates this layer to the next
    # For each neuron in this layer, first activate then propagate
    def propagate(self):
        for i in self.neurons:
            i.activate()
            i.propagate()


    # THIS SHOULD ONLY BE USED FOR TESTING AND THE INPUT LAYER
    # Make sure the size of the inputs matches the size of the layer!
    def setInput(self , inputs):
        for i in range(len(inputs)):
            self.neurons[i].addToRawInput(inputs[i])


    def getAllValues(self):
        values = []

        for i in self.neurons:
            values += i.getAllValues()

        return values

    
    def setAllValues(self , values):
        currentArray = values

        for i in range(len(self.neurons)):
            spliceIndex = 1 + len(self.neurons[i].connections)
            self.neurons[i].setAllValues(currentArray[:spliceIndex])
            currentArray = currentArray[spliceIndex:]


    # Prints all properties of this layer and its Neurons
    def print(self):
        print("-- Layer --")
        print("Size: " + str(self.size))
        for i in self.neurons:
            i.print()
        print()