from django.shortcuts import render

# from django.shortcuts import render
# import os
# import pandas as pd
# import random

# # Paths
# image_folder = 'static/images/model_images/train/'
# label_file = os.path.join('static', 'images', 'model_images', 'labels.csv')

# # Load labels
# labels_df = pd.read_csv(label_file)

# # If the csv doesn't include extensions in 'id', create a new column img_file
# if not labels_df['id'].iloc[0].endswith('.jpg'):
#     labels_df['img_file'] = labels_df['id'] + '.jpg'
# else:
#     labels_df['img_file'] = labels_df['id']

# # List image files from folder
# image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

# def home(request):
#     img_file = random.choice(image_files)
#     label_list = labels_df.loc[labels_df['img_file'] == img_file, 'breed'].values
#     # Convert label list to string for template
#     label = label_list[0] if len(label_list) > 0 else ''
#     context = {
#         'random_image': img_file,
#         'random_label': label
#     }
#     return render(request, 'index.html', context)

from django.shortcuts import render
import os
import pandas as pd
import random
from random import sample

image_folder = 'static/images/model_images/train/'
label_file = os.path.join('static', 'images', 'model_images', 'labels.csv')
test_folder = 'static/images/model_images/test/'

labels_df = pd.read_csv(label_file)
if not labels_df['id'].iloc[0].endswith('.jpg'):
    labels_df['img_file'] = labels_df['id'] + '.jpg'
else:
    labels_df['img_file'] = labels_df['id']

image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
test_images = [f for f in os.listdir(test_folder) if f.endswith('.jpg') or f.endswith('.png')]

def home(request):
    img_file = random.choice(image_files)
    label_list = labels_df.loc[labels_df['img_file'] == img_file, 'breed'].values
    label = label_list[0] if len(label_list) > 0 else ''

    # Pick a random sample of 6 test images if more than 6 exist
    test_images_sample = sample(test_images, 6) if len(test_images) > 6 else test_images

    context = {
        'random_image': img_file,
        'random_label': label,
        'test_images': test_images_sample
    }

    return render(request, 'index.html', context)



import os
import random
import pandas as pd
from django.shortcuts import render

image_folder = 'static/images/model_images/train/'
label_file = os.path.join('static', 'images', 'model_images', 'labels.csv')

labels_df = pd.read_csv(label_file)

# Add extension if missing
if not labels_df['id'].iloc[0].endswith('.jpg'):
    labels_df['img_file'] = labels_df['id'] + '.jpg'
else:
    labels_df['img_file'] = labels_df['id']

def gallery(request):
    # Get all image filenames in the folder
    all_images = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    # Number of images to show (e.g., 20)
    num_images = 20
    sampled_images = random.sample(all_images, min(num_images, len(all_images)))
    
    # Filter dataframe for sampled images only
    sampled_df = labels_df[labels_df['img_file'].isin(sampled_images)]

    images_with_labels = []
    for _, row in sampled_df.iterrows():
        label = row['breed']
        # Convert stringified list if necessary
        if isinstance(label, str) and label.startswith('[') and label.endswith(']'):
            import ast
            label = ast.literal_eval(label)
        elif isinstance(label, str):
            label = [label]
        images_with_labels.append((row['img_file'], label))

    context = {
        'images_with_labels': images_with_labels
    }
    return render(request, 'gallery.html', context)



def model_info(request):
    return render(request, 'model_info.html')

def about(request):
    return render(request,'about.html')