# to increase the detail, increase the value of ITERATIONS
ITERATIONS = 1000
WIDTH, HEIGHT = 601, 601  

# zoom in and out by changing the DIAMETER
DIAMETER = 1

start = (-.5 - DIAMETER / 2, 0)  
d_over_h = DIAMETER / HEIGHT
d_over_w = DIAMETER / WIDTH

real, imag = start
colors = ("#B000B5", "#111111", "#444444", "#000000")
