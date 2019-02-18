from Layer import Layer

class NNetwork:

    # Creates a neural network given a list of layer sizes
    def __init__(self , layerSizes):
        self.numLayers = len(layerSizes)
        self.layers = []

        for i in layerSizes:
            self.layers.append(Layer(i))
        
        for i in range(self.numLayers - 1):
            self.layers[i].connect(self.layers[i + 1])
    

    # Sets inputs to the input layer
    # This assumes that your network has at least 1 layer
    def setInput(self , inputs):
        self.layers[0].setInput(inputs)

    
    # Propagates through the graph
    def propagate(self):
        for i in self.layers:
            i.propagate()   # Yes, all of them!

    
    # Returns the output of the NN, or the greatest value of the output layer
    # THIS IS THE INDEX OF THE NEURON NOT ITS VALUE
    def getOutput(self):
        maxIndex = 0
        maxValue = -2
        index = 0

        for i in self.layers[self.numLayers - 1].neurons:   # Last layer
            if i.activation > maxValue:
                maxValue = i.activation
                maxIndex = index 

            index += 1

        return maxIndex


    def getAllValues(self):
        values = []

        for i in self.layers:
            values += i.getAllValues()

        return values


    def setAllValues(self , values):
        currentArray = values

        for i in range(len(self.layers) - 1):
            spliceIndex = self.layers[i].size + self.layers[i].size * self.layers[i + 1].size
            self.layers[i].setAllValues(currentArray[:spliceIndex])
            currentArray = currentArray[spliceIndex:]

    
    # Prints out the NN and all its properties and layers
    def print(self):
        print("-- NNetwork --")
        print("Num Layers: " + str(self.numLayers))
        for i in self.layers:
            i.print()

        print()