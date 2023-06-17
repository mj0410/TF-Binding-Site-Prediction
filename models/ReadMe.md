### Neural Network

<img src="./IMAGE/NeuralNetwork.png" width="700"><br/>

- Machine learning algorithm inspired by the neural architecture of the human brain
- Consists of a basic building block called a neuron; neurons take input and produce output using a mathematical function called activation function
- 1 input layer, 1 or more hidden layers, and 1 output layer

### Convolutional Neural Network (CNN)

<img src="./IMAGE/CNN.png" width="700"><br/>

- Multilayered neural network designed to handle data in the form of multiple arrays, for example, sequence data in 1D array and images in 2D arrays 
- The hidden layers consist of convolutional layers, pooling layers, and fully connected layers

    `Convolutional layer` 
    >convolutional filter slides the input and extracts features from the input
    >The size of the filter is defined by the user
    >feature extraction is performed by dot product of filter and input
    
    `Pooling layer`
    >reduces the output size of the convolutional layer
    >integrates the features of small neighborhood extracted by convolutional layer
    >helps to decrease time-complexity
    >identifies more important features

    `Fully connected layer`
    >collects the outputs from previous layers
    >forms the final output
    >starts classification
