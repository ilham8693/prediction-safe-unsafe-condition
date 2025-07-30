import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import os

def run():
    # Title
    st.title('Safe and Unsafe Working Condition')

    # Sub Header
    st.subheader('Exploratory Data Analysis (EDA) of dataset')

    # Image
    image = Image.open('./src/image11.jpg')
    st.image(image)

    # Data
    st.write('##### Dataset Overview')

    main_path = './src/Worksite-Safety-Monitoring-Dataset/'
    train_path = os.path.join(main_path, 'train')
    val_path = os.path.join(main_path, 'valid')
    test_path = os.path.join(main_path, 'test')

    def plot_images(path):
        labels = sorted(os.listdir(path))
        figures = []
        for label in labels:
            folder_path = os.path.join(path, label)
            images = os.listdir(folder_path)
            images = images[:5]
            fig, axes = plt.subplots(1, len(images), figsize=(50, 50))
            if len(images) == 1:
                axes = [axes]
            for idx, img_file in enumerate(images):
                img = plt.imread(os.path.join(folder_path, img_file))
                axes[idx].imshow(img)
                axes[idx].axis("off")
                axes[idx].set_title(label, fontsize=50, fontweight='bold')
            plt.tight_layout()
            figures.append(fig)
        return figures
    
    # Train
    st.write('##### Train')
    figs_train = plot_images(train_path)
    for fig in figs_train:
        st.pyplot(fig)

    # Validation
    st.write('##### Validation')
    figs_val = plot_images(val_path)
    for fig in figs_val:
        st.pyplot(fig)

    # Test
    st.write('##### Test')
    figs_test = plot_images(test_path)
    for fig in figs_test:
        st.pyplot(fig)

    st.markdown("""
                ##### Exploration:

                - From the visualization results, it can be seen that the images mostly depict people performing tasks in industrial environments across various sectors such as manufacturing, construction, and others. What stands out in the images are the safety helmets and vests, which have much brighter colors compared to other objects. Notably, in the unsafe class, there are also images of people wearing safety helmets but not wearing safety vests, this is good for model learning as it prevents bias, such as assuming that wearing a helmet only implies safety. There are also some images that do not show full of people but only body parts or PPE only.
                - From the dataset, it's apparent that the image sizes are consistent, and all images have the same pixel dimensions, allowing the model to properly see each one. The image sizes will also be resized uniformly during model preprocessing.
                - These images are of people in work environments. The color channels are kept in RGB format because PPE (Personal Protective Equipment) typically comes in bright, vivid colors.
                - The images are mostly landscape or portrait photos of people working in various workplace settings, taken from different angles and distances (both close-up and wide shots). This variation may help the model learn more comprehensively, but the challenge is whether the dataset is large and varied enough for effective learning.
                - Another challenge is that the images involve different activities, locations, and body positions, with individuals wearing various types of PPE. Therefore, evaluating model performance carefully is crucial to ensure prediction accuracy.
                """)

if __name__ == '__main__':
    run()