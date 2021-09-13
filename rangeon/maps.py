"""Code to generate 2D random maps"""

import math

import numpy
import plotly.graph_objects as go
import perlin_noise

COLOR_SCALE = [
    [0, 'rgb(0,0,100)'],
    [0.3, 'rgb(50, 50, 200)'],
    [0.31, 'rgb(189,183,107)'],
    [0.4, 'rgb(80,20,20)'],
    [0.55, 'rgb(0,130,30)'],
    [0.75, 'rgb(0,60,0)'],
    [0.9, 'rgb(0,50,0)'],
    [0.95, 'rgb(100, 100, 100)'],
    [1, 'rgb(255, 255, 255)']
]

def generate(seed: int = 1):
    n1div = 30 # landmass distribution
    n2div = 4 # boulder distribution
    n3div = 1 # rock distribution

    n1scale = 20 # landmass height
    n2scale = 2 # boulder scale
    n3scale = 1 # rock scale

    size = 200

    zroot = 5
    zpower = 2.5

    noise = perlin_noise.PerlinNoise(octaves=1, seed=seed)
    map_x = range(-int(size/2), int(size/2))
    map_y = map_x
    map_z = []

    for x in map_x:
        for y in map_y:
            x1 = x + size/2
            y1 = y + size/2
            z = noise([x1 / n1div, y1 / n1div]) * n1scale # add landmass
            z += noise([x1 / n2div, y1 / n2div]) * n2scale # add boulders
            z += noise([x1 / n3div, y1 / n3div]) * n3scale # add rocks
            if z >= 0:
                z = -math.sqrt(z)
            else:
                z = ((-z) ** (1 / zroot)) ** zpower
            map_z.append(z)

    fig = go.Figure(data=go.Heatmap(
        z = numpy.array(map_z).reshape((len(map_x), len(map_x))),
        type = 'heatmap', colorscale = COLOR_SCALE))

    fig.show()
