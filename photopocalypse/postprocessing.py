import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import io

def postprep_sharpening(upscaled_image):
    # output_img = tf.image.decode_image(contents) #! Needs to go inside of api
    # model = hub.load(model) #! Needs to go to API (but outside)
    # image_hr = prediction.preprocess_image(output_img) #! Needs to go to API
    # image_out = prediction.predict_upscaled(image_hr,model) #!Needs to go to API
    upscaled_image_post_processed = tf.cast(upscaled_image, tf.uint8).numpy()
    image_pil = Image.fromarray(upscaled_image_post_processed)
    img_byte_arr = io.BytesIO()
    image_pil.save(img_byte_arr, format='JPEG')  # Use 'PNG' or other format as needed
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr
