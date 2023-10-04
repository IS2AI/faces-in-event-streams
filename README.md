# Faces in Event Streams (FES): An Annotated Face Dataset for Event Cameras

![Faces in Event Streams](https://user-images.githubusercontent.com/5821328/212868401-00f986d8-6bcf-44be-9d76-5bac4b6f21d7.png)

<p align="center"> Figure 1: Faces and facial landmarks detected using the model produced by the given project.</p>



<p align="center"> Our dataset contains 689 minutes of recorded event streams, and 1.6 million annotated faces with bounding box and five point facial landmarks. </p>

## Access
- To access the dataset and pre-trained models, please follow the [link]( https://forms.gle/R7WHmVueCoyvYvrY9) and provide your informaton.
 After filling out the form, you will receive credentials and instructions on how to access the server.

- Pre-trained models come together with the dataset, alternatively pre-trained models are available on [this google drive link](https://drive.google.com/drive/folders/1I2l-_-RmRLAaS6DF9OfCfq9-VmvrgETQ?usp=share_link).

## Dataset description
![dataset2](https://github.com/IS2AI/faces-in-event-streams/assets/102503259/b33a16cf-d5d3-4658-bfa9-3f1028cbc79e)
<p align="center">  Figure 2: File structure of the FES dataset, with green representing an event stream and blue representing annotations: a) The preprocessed data are divided into three folders, with each folder containing only bounding box annotations,both bounding box and facial landmark annotations, and event streams in the h5 format. The raw dataset contains lab and wild folders with raw videos and annotations. b) Each controlled experiment (Lab) file has an individual subject ID and an experiment ID. Each file in the uncontrolled (Wild) dataset contains a scene ID that provides information about the location of a recording and the number (ID) of an experiment.</p>

The final dataset contains both the originally collected raw files and the preprocessed data. The raw files contain video in the “raw” format that can be rendered, and annotations in the “xml” format. Meanwhile, the converted files contain a dataset ready for machine learning training in the “npy” format, annotations for bounding box and facial landmarks, and “h5” files representing the Python binary format to work with the event stream data as an array.

The integration of event streams with annotated labels was based on the time dimension. Since events were recorded at microsecond precision, the timeline of the labels was also converted to microseconds, although it originally had millisecond precision and was derived based on a frame number and frame rate of 30 Hz.



## Documentation

<p align="center"> Further, this repo contains pre-processing scripts and instructions for inference and model training for face and facial landmark detection from events streams. </p>

### Environment Installation & Set up
To launch training or inference, first of all it is required to install Metavision SDK environment.

- If you use Linux OS, install Metavision SDK environment from this [link](https://docs.prophesee.ai/stable/installation/linux.html).

- If you use Windows OS, install Metavision SDK environment from this [link](https://docs.prophesee.ai/stable/installation/windows.html).


### Downloading the repository

```
$ git clone https://github.com/IS2AI/faces-in-event-streams
```

### Face detection
 - #### Inference
To run inference for face bounding box model, use the following command:
```
python3 detection_and_tracking_pipeline.py --object_detector_dir /path/to/model --record_file <RAW file to process> --display
```
alternatively you can proceed with instructions from [this](https://docs.prophesee.ai/stable/samples/modules/ml/detection_and_tracking_inference_py.html#chapter-samples-ml-detection-and-tracking-inference-python) link.

- #### Training
Before launching training, please place label_map_dictionary.json, which comes as part of this repo, in the same folder where your train/val/test folders are located.
1. To train the model to detect face bounding box in event streams, run:

```
cd <path to train_detection.py>
python3 train_detection.py <path to output directory> <path to dataset>
```

alternatively, you can follow instructions from [here](https://docs.prophesee.ai/stable/samples/modules/ml/train_detection.html#chapter-samples-ml-train-detection).

2. To select the feature extractor, you need to define --feature_extractor option using:
```
python3 train_detection.py <path to output directory> <path to dataset> --feature_extractor <select feature extractor: Vanilla, ResNet_18, ResNet_34, ResNet_50>
```

### Facial landmark detection
To train or detect five point facial landmark detection, the change to the following files should be done:
- box_processing.py
- display_frame.py

Changes which need to be done can be found in our repo in files:
- box_processing_difference.py
- display_frame_difference.py

Further, train and inference instructions are the same as for face detection part, declared above.

Since 
- feature_extractors.py
- box_processing.py
- display_frame.py

are files which originally comes as part of Metavision SDK which comes under Prophesee Metavision Licensing, we will share only changes that has to be done on the installed Metavision SDK package (once you install Metavision SDK, you will have direct access to the original files).

### If you use the dataset/source code/pre-trained models in your research, please cite our work:
@article{Bissarinova2023,<br /> 
author = "Ulzhan Bissarinova and Tomiris Rakhimzhanova and Daulet Kenzhebalin and Huseyin Atakan Varol",<br /> 
title = "{Faces in Event Streams (FES): An Annotated Face Dataset for Event Cameras}",<br /> 
year = "2023",<br /> 
month = "5",<br /> 
url = "https://www.techrxiv.org/articles/preprint/Faces_in_Event_Streams_FES_An_Annotated_Face_Dataset_for_Event_Cameras/22826654",<br /> 
doi = "10.36227/techrxiv.22826654.v1"<br /> 
}




