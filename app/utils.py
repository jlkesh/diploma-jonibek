from uuid import uuid4
from time import time_ns
import pathlib

def unique_code():
    return f'{time_ns()}{uuid4()}'

