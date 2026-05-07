# def fence(func):
#     def wrapper():
#         print("%"*10)
#         func()
#         print("-" * 10)
#     return wrapper

# @fence
# def log():
#     print("decorator!")
    
# another_funtion=fence(log)
# another_funtion()

# log()

from typing import Callable,Any
def decorator(func:Callable[[int,int],Any]):
    pass