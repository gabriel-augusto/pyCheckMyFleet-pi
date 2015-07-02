__author__ = 'gabriel'

import socket

REMOTE_SERVER = "www.google.com"


def is_float(value):
    try:
        value = float(value)
        return True
    except:
        return False


def has_internet_connection():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        socket.create_connection((host, 80), 2)
    except:
        return False
    return True
