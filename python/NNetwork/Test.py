from NNetwork import NNetwork

myNetwork = NNetwork([2 , 2])

myNetwork.setInput([5 , 2])
myNetwork.propagate()
myNetwork.print()
print(myNetwork.getOutput())