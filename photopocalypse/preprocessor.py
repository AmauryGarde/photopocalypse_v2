import tensorflow as tf

def preprocess_image(contents):
    output_img = tf.image.decode_image(contents)
    hr_image = tf.convert_to_tensor(output_img)
    # If RGBA, remove the alpha channel
    if hr_image.shape[-1] == 4:
        hr_image = hr_image[...,:-1]
    # Ensure image size is a multiple of 4
    hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
    hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
    # Cast to float32
    hr_image = tf.cast(hr_image, tf.float32)
    # Expand dimensions to add batch size
    return tf.expand_dims(hr_image, 0)
