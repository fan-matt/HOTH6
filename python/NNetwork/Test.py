from Layer import Layer

inputLayer = Layer(1)

hidden = Layer(1)

inputLayer.setInput([2])
inputLayer.connect(hidden)
inputLayer.propagate()
hidden.propagate()

inputLayer.print()
hidden.print()