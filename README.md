## Prediction Safe/Unsafe Working Condition

## Repository Outline
1. README.md - About the project
2. notebook.ipynb - Code script for data analysis and modeling
3. notebook_inf.ipynb - Code script for data inference
4. /deployment - Files and script for deployment

## Problem Background
Workplace safety is a critical aspect of industrial and construction environments. Ensuring workers comply with safety protocols, such as wearing helmets, vests, and other protective equipment, helps prevent accidents and injuries. However, manual supervision to monitor safety compliance is time consuming and prone to human error. To address this, computer vision can be utilized to automatically detect whether a workplace condition is safe or unsafe based on image data. By leveraging an Artificial Neural Network (ANN) model, this project aims to classify workplace safety conditions accurately, reducing the risk of oversight in safety operations.

## Project Output
This project aims to perform comprehensive data analysis and develop a model of predictive system for industrial and construction environments. The result is model ANN with certain arcitecture and alo transfer learning method using TensorFlow/Keras with its evaluation. Recall is the key metric because missing unsafe conditions (false negatives) can lead to serious risks like accidents or injuries. The final result of the model is `Accuracy 85%` and `Recall 83%`. Analysis and model is deployed sucessfully.

Inference result:

<img src="deployment/Screenshot%201.png" width="500"/>

<img src="deployment/Screenshot%202.png" width="500"/>

<img src="deployment/Screenshot%203.png" width="500"/>

## Data
The dataset used in this project was sourced from Kaggle.com and focuses on determining whether an image meets the safety requirements based on the presence of essential Personal Protective Equipment (PPE) such as helmets and reflective vests. Dataset has two class for safe and unsafe class. Each class has Train Set: 810 images, Validation Set: 100 images and Test Set: 100 images.

## Method
This project employs Python and its libararies to conduct data analyis and modeling (TensorFlow/Keras). Analysis and model is deployed in huggingface.co as space and can be used to do exploration and prediction of data.

## Stacks
The programming language, tools, and Python libraries utilized in this project, including:
- Pandas – used for data manipulation and analysis.
- Numpy - used for data manipulation and analysis.
- Matplotlib Pyplot – used for data visualization.
- Seaborn - used for data visualization.
- Scikit-Learn - used for model evaluation.
- TensorFlow/Keras - used for modeling.

## Reference
- [Dataset Source](https://www.kaggle.com/datasets/lbquctrung/worksite-safety-monitoring-dataset)
- [Deployment Model](https://huggingface.co/spaces/ilham86/safe-unsafe-condition)
- [Model File](https://drive.google.com/drive/folders/1EsxVkxg_TyWeQIUOKRiqlhEKZeNz8wYu?usp=share_link)
