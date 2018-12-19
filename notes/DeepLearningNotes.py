"""
    Deep Learning Neurel Nets

    1. Each node has an activation function in charge of shaping the data
        a. Linear
        b. Logistic (sigmoid)
        c. Hyperbolic tangent 
        d. ReLU
    2. Network Complexity
        a. Wide Network
        b. Deep Network
        c. Sparse Network
    3. Types of Networks
        a. Convulutional Neural Network (CNN)
            1) Convolution
                - each neuron in the convulution layer is responsible for a small section of neurons in the preceding layer
                - filters: moves across the image and performaning a mathematical operation on a small section of the image
            2) Pooling
                - Downsampling layers
            3) Image -> Convolution Layer -> Pooling Layer -> Convolution -> Pooling -> Hidden Classification Layer -> Hidden Classification Layer -> Prediction
            4) Uses
                - Image classification
                - Image recognition
                - Image processing
                - Image segmentation
                - Video analysis
                - language processing
        b. Recurrent Neural Network (RNN)
            1)can feed data back to itself, doesn't just have to go forward
            2) Gated RNN - Update | Rest
            3) Long Short-Term Memory - Input | Output | Forget
            4) Uses
                - Natural language procesing
                - Speech recognition
                - Language translation
                - Conversation modeling
                - Image captioning
                - Visual Q & A
        c. Generative Adversarial Network (GAN)
            1) Consists to two differnt neural networks
                - Generator network
                - Discriminator network
                - G Produces ==> Data <== D Detects
            2) Uses
                - Image generation
                - Image enhancement
                - Text generation
                - Speech synthesis
                - Drug discovery
        d. Deep Reinforcement Learning
            1) Uses
                - Games
                - Vehicles
                - Robotics
                - Management
                - Finance

"""