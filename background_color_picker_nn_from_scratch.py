def avg_neuron(data1, data2, data3):
    tot = data1+data2+data3
    avg = tot/3
    return avg
def output_neuron(data1):
    output_01 = data1/255
    if output_01 < 0.5:
        return "white"
    else:
        return "black"


def model(color1, color2, color3):
    average = avg_neuron(color1, color2, color3)
    return output_neuron(average)
def fit(color1, color2, color3):
    return model(color1, color2, color3)
    
fit()

"""
this is a bit of a dumb project, I just wanted to do this for fun.
it is called nn but there is no real learning :)
*I made this when I was learning dl just to try to understand what a nn is
"""
