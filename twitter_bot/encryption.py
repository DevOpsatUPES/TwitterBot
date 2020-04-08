import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import json

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

random_generator = Random.new().read
KEY = RSA.generate(1024, random_generator)
with open ("private.pem", "w") as prv_file:
    prv_file.write(str(KEY.exportKey(format='PEM')))

def loadKeys():
    global CONSUMER_KEY
    global CONSUMER_SECRET
    global ACCESS_KEY
    global ACCESS_SECRET
    try:
        with open('token.access', mode='r') as f:
            keys = f.read().splitlines()
            CONSUMER_KEY = keys[0]
            CONSUMER_SECRET = keys[1]
            ACCESS_KEY = keys[2]
            ACCESS_SECRET = keys[3]
            print("Loading keys succesful")
    except:
        print("Loading keys failed")

def strToBinary(str):
    return (" ".join(f"{ord(i):b}" for i in str))

def convertToBinary():
    global CONSUMER_KEY
    global CONSUMER_SECRET
    global ACCESS_KEY
    global ACCESS_SECRET
    CONSUMER_KEY = strToBinary(CONSUMER_KEY)
    CONSUMER_SECRET = strToBinary(CONSUMER_SECRET)
    ACCESS_KEY = strToBinary(ACCESS_KEY)
    ACCESS_SECRET = strToBinary(ACCESS_SECRET)

def encrypt(message):
    global KEY
    publickey = KEY.publickey()
    encrypted = publickey.encrypt(message, 32)
    return encrypted[0]

def encryptKeys():
    global CONSUMER_KEY
    global CONSUMER_SECRET
    global ACCESS_KEY
    global ACCESS_SECRET
    CONSUMER_KEY_splitted = CONSUMER_KEY.split()
    CONSUMER_KEY = ""
    CONSUMER_SECRET_splitted = CONSUMER_SECRET.split()
    CONSUMER_SECRET = ""
    ACCESS_KEY_splitted = ACCESS_KEY.split()
    ACCESS_KEY = ""
    ACCESS_SECRET_splitted = ACCESS_SECRET.split()
    ACCESS_SECRET = ""
    with open('consumer.key', mode='w') as f1:
        for i in CONSUMER_KEY_splitted:
            f1.write(str(encrypt(int(i))))
            f1.write("\n")
    with open('consumer.secret', mode='w') as f2:
        for i in CONSUMER_SECRET_splitted:
            f2.write(str(encrypt(int(i))))
            f2.write("\n")
    with open('access.key', mode='w') as f3:
        for i in ACCESS_KEY_splitted:
            f3.write(str(encrypt(int(i))))
            f3.write("\n")
    with open('access.secret', mode='w') as f4:
        for i in ACCESS_SECRET_splitted:
            f4.write(str(encrypt(int(i))))
            f4.write("\n")


loadKeys()
convertToBinary()
encryptKeys()
