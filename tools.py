from cryptography.fernet import Fernet

def encrypt(file_path, key):

    with open(file_path,"rb") as f:
        image = f.read()

    # key = Fernet.generate_key()

    # with open("key.key",mode='wb') as f:
    #     f.write(key)

    f = Fernet(key)
    encrypted_image = f.encrypt(image)

    with open("image.jpg",mode='wb') as f:
        f.write(encrypted_image)

def decrypt(file_path, key):
# key = b'0'

# with open("key.key", mode="rb") as f:
#     key = f.read()

# img_encrypted = b'0'

    with open(file_path,mode="rb") as f:
        encrypted_img = f.read()

    f = Fernet(key)
    decrypted_img = f.decrypt(encrypted_img)

    with open("image.jpg","wb") as f:
        f.write(decrypted_img)

def generate_key():
    key = Fernet.generate_key()
    print(key)
    with open("key.key",mode='wb') as f:
        f.write(key)

