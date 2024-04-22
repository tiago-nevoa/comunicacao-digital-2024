import cv2
import os


key_generator = __import__('4b').third_exercise

def encrypt_image(image, key):
    return image ^ key

def desencrypt_image(encrypted_image, key):
    return encrypted_image ^ key

def main():

    image_types = ['png', 'jpg', 'jpeg', 'tif']
    directory = "modulo_1/TestFiles/CD/"
    files = os.listdir(directory)
    files = ["modulo_1/TestFiles/CD/barries.jpg"]

    for filename in files:

        file = os.path.join(directory, filename)

        is_image = file[-3:] in image_types

        if not is_image:
            break

        image = cv2.imread(file#, cv2.IMREAD_GRAYSCALE
                           )

        key = key_generator(1)
        encrypted_image = encrypt_image(image, key[0])
        cv2.imwrite('encrypted_image.png', encrypted_image)
        desencrypted_image = desencrypt_image(encrypted_image, key)


    

if __name__ == '__main__':
    main()