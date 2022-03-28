from uuid import uuid4
from time import time_ns
from os.path import join as join_path
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent

UPLOADS_DIR = join_path(BASE_DIR, 'uploads')

def unique_code():
    return f'{time_ns()}{uuid4()}'


def get_extension(filename: str):
    return filename.split(".")[-1]


def generate_new_name(filename: str):
    return f'{unique_code()}.{get_extension(filename)}'
    return filename.split(".")[-1]