# plant-leaf-classification
In this project, We made a Web Application that allows us to take a plant leaf image and then predict if the leaf/plant is healthy or has diseases like rust, scab and multiple diseases. We used Deep Learning which takes in leaf image and gives the predictions.

## Summary
We made a Web Application that allows us to take a plant leaf image and then predict if the leaf/plant is healthy or has diseases like rust, scab and multiple diseases. We used Deep Learning which takes in leaf image and gives the predictions.

## Background
Having diseases in plants or crops is not good and detecting what kind of disease it is can really help to make right decisions to remove/prevent the disease. And Deep Learning can really helps in detecting all kinds of plant diesease very accuratly and can be runned through webpages or even mobile phones.

## How it is used?
It is really easy to use. Just go to this link: "https://plant-leaf-classification.herokuapp.com/". And upload your plant leaf image. After uploading the image, the process will automatically start where the deep learning model will take the image and after a few seconds later, predictions will be shown.

![Screenshot (11)](https://user-images.githubusercontent.com/54503215/102689553-00d34100-4225-11eb-8f34-31c82bd6fc03.png)

### Libraries used
* Tensorflow 2.0 - Framework for creating & training deep learning models.
* efficientnet - Libraries for training efficient-net model architectures.
* Streamlit - For creating Web Applications using python.
* Wandb - For Recording our Experiments.

### Challenges
The dataset we used only had 4 different classes and was only for apple trees. It would be much better to have more variety in the dataset with many different kinds of leaf images from different kinds of trees.

