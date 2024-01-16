"""
Message Encryption means keeping the message secret. In simple words, Message Encryption means putting the message in a secret box that only the receiver can open. If you want to learn how to encrypt messages using Python, this article is for you. In this article, I will take you through the task of message encryption using Python.

Message Encryption
Before implementing Message Encryption using Python, let’s look at the process of Message Encryption. Here’s the complete process of Message Encryption that messaging apps follow:

First, choose a secret key that to encrypt the message. This key is a password only the person supposed to read the message knows.
Then take the message and scramble it using the key. It means turning the message into a secret code like a jumble of letters or numbers.
Once the message is scrambled, it is delivered to the person who is supposed to read it. But if anyone else tries to read it, they’ll see a jumble of letters or numbers that don’t make sense.
So, Message Encryption is like having a secret code that only the person who is supposed to read the message can understand
    """

message_data = {
    "Aman": [
        {"message": "Hey Divyansha, how's it going?", "time": "2023-03-21 10:30:00"},
        {"message": "Not too bad, just working on some coding projects. Did you hear about the new encryption algorithm?", "time": "2023-03-21 10:35:00"},
        {"message": "It's called AES256 and it's supposed to be really secure. Want to give it a try with our messages?", "time": "2023-03-21 10:40:00"},
    ],
    "Divyansha": [
        {"message": "Good, thanks! How about you?", "time": "2023-03-21 10:32:00"},
        {"message": "No, what's that?", "time": "2023-03-21 10:37:00"},
        {"message": "Sure, let's do it!", "time": "2023-03-21 10:42:00"},
    ]
}

import os 
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend
shared_secret_key = os.urandom(32)

def encrypt_message(message,key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key),modes.CBC(iv),backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message + (16-len(message)%16) * chr(16-len(message)%16)
    ciphertext = encryptor.update(padded_message.encode()) + encryptor.finalize()
    return iv + ciphertext