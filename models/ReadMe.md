### Neural Network
<br/>
<img src="https://github.com/mj0410/TFBS-Prediction/blob/main/IMAGE/NeuralNetwork.png" width="400"><br/>

- Machine learning algorithm inspired by the neural architecture of the human brain
- Consists of a basic building block called a neuron; neurons take input and produce output using a mathematical function called activation function
- 1 input layer, 1 or more hidden layers, and 1 output layer

<br/>

### Convolutional Neural Network (CNN)
<br/>
<img src="https://github.com/mj0410/TFBS-Prediction/blob/main/IMAGE/CNN.png" width="400"><br/>

- Multilayered neural network designed to handle data in the form of multiple arrays, for example, sequence data in 1D array and images in 2D arrays
- zero padding : pad 0 to provide information where are the edges -> done before enter to the convolutional layer
- The hidden layers consist of convolutional layers, pooling layers, and fully connected layers

    `Convolutional layer` 
    > Convolutional filter slides the input and extracts features from the input <br/>
    > The size of the filter is defined by the user <br/>
    > Filter detects whether the image has interested features or not <br/>
    > Stride : how many pixels filter will move at once <br/>
    > Feature extraction is performed by dot product of filter weight and input <br/>
    > e.g) 32x32 input image, 6 5x5 filters -> 6 28x28 feature maps <br/>
    > Depth : number of filter <br/>
    > filter -> feature map -> activation function -> activation map (output)
    
    `Pooling layer`
    > Reduces the output size of the convolutional layer <br/>
    > Integrates the features of small neighborhood extracted by convolutional layer <br/>
    > Helps to decrease time-complexity <br/>
    > Identifies more important features

    `Fully connected layer`
    > Collects the outputs from previous layers <br/>
    > Forms the final output <br/>
    > Starts classification

<br/>

### Recurrent Neural Network (RNN)

<br/>

<img src="https://github.com/mj0410/TFBS-Prediction/blob/main/IMAGE/RNN.png" align="left" width="120">

<br/>

&nbsp;&nbsp; - The main neural network model for tasks such as natural language processing and time-series analysis <br/>
&nbsp;&nbsp; - Processes one input element at a time, for example, a word in a sentence or a nucleotide in a DNA sequence <br/>
&nbsp;&nbsp; - Takes the output of the previous step as an input, therefore it is able to have a memory

<br clear="left"/>
<br/>

#### Long Short-Term Memory (LSTM)

<br/>

[<img src="https://github.com/mj0410/TFBS-Prediction/blob/main/IMAGE/LSTM.png" width="400">](https://www.semanticscholar.org/paper/Accident-Scenario-Generation-with-Recurrent-Neural-Jenkins-Gee/4bb261e727835aca4ac4b61a6147ab5d84aab709)

<br/>

- Developed to deal with gradient vanishing problem using a memory cell and gates

    `Gradient vanishing problem`
    > The effect of the information received earlier can gradually decrease and disappear as learning progresses

    `Memory cell`
    > Long-term state : memory of important information accumulated at every stage <br/>
    > Short-term state : the output of the previous step 
    
    `Gate : forget, input, and output`
    > Forget gate can control what needs to be forgotten from the long-term state <br/>
    > Input gate provides the information of what needs to be stored to long-term state from short-term state <br/>
    > Output gate reads both states and decides what needs to be moved to the next step

<br/>

#### Bidirectional Long Short-Term Memory

<br/>

<img src="https://github.com/mj0410/TFBS-Prediction/blob/main/IMAGE/Bi-LSTM.png" width="400">

<br/>

- Constructed by applying LSTM twice 
- The inputs are fed into the forward LSTM layer as it is, and reversed version of the inputs are fed into the backward LSTM layer
- This structure makes it easy to capture the impact of input information from the past and the future on the current state
