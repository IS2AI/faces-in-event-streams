# Faces in Event Streams (FES): An Annotated Face Dataset for Event Cameras

![Faces in Event Streams](https://user-images.githubusercontent.com/5821328/212868401-00f986d8-6bcf-44be-9d76-5bac4b6f21d7.png)



Our dataset contains 689 minutes of recorded event streams, and 1.6 million annotated faces with bounding box and five point facial landmarks.

To access the dataset and pre-trained models from our servers directly, please follow the [link]( https://forms.gle/R7WHmVueCoyvYvrY9) and provide your informaton.

After filling out the form, you will receive credentials and instructions on how to connect to our server where dataset is located.

Alternatively, you can get the pre-trained models and dataset from [google drive link](https://drive.google.com/drive/folders/1btC_bkWV0RpU1JJKBUehH4_NaGG1SMov?usp=share_link).



# Documentation

Further, this repo contains pre-processing scripts and instructions for inference and model training for face and facial landmark detection from events streams. 

# Environment Installation & Set up
To be able to launch training or inference, first of all it is required to install Metavision SDK environment.

If you use Linux, please proceed with the following instructions:
https://docs.prophesee.ai/stable/installation/linux.html

If you use Windows, please proceed with the following instructions:
https://docs.prophesee.ai/stable/installation/windows.html

# Downloading the repository

```
$ git clone https://github.com/IS2AI/faces-in-event-streams
```

# Inference
To be able to run face bounding box or bounding box + facial landmarks detection models, please proceed with the following instructions:
https://docs.prophesee.ai/stable/metavision_sdk/modules/ml/samples/detection_and_tracking_inference.html#chapter-sdk-ml-detection-and-tracking-inference
# Training
1. To be able to train the model to detect face bounding box in event streams, follow these instructions:
https://docs.prophesee.ai/stable/metavision_sdk/modules/ml/quick_start/index.html#training

2.To be able to select the feature extractor, you need to define in the option using:
python3 train_detection.py <path to output directory> <path to dataset> --feature_extractor <select feature extractor: Vanilla, ResNet_18, ResNet_34, ResNet_50>
