from Climate2 import *
import random
import numpy as np


def Ph_of_soil():
    return random.choice(np.arange(4.5, 8.5, 0.007)) 

def main(lat, lang):
    temperature, precipitation = collect_weather(lat, lang)
    Ph =  Ph_of_soil()
    return temperature, Ph, precipitation


if __name__ == '__main__':
    print(main(40.427887497399716, -80.00927739563862))