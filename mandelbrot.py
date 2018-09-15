from tkinter import *
import CONFIG

def mandelbrot(c):
    z = 0
    for i in range(CONFIG.ITERATIONS):
        z = z*z + c
        if abs(z) > 2:
            return i     
    return CONFIG.ITERATIONS

def magic():
    root = Tk()
    canvas = Canvas(root, width=CONFIG.WIDTH,height=CONFIG.HEIGHT)
    root.title("mandelbrot")
    canvas.pack()
    img = PhotoImage(width=CONFIG.WIDTH, height=CONFIG.HEIGHT)
    canvas.create_image(((CONFIG.WIDTH+1)//2, (CONFIG.HEIGHT+1)//2), image=img, state="normal")

    for x in range(CONFIG.WIDTH):
        for y in range(CONFIG.HEIGHT//2, -1, -1):
            i = mandelbrot(complex(CONFIG.real, CONFIG.imag))
            color = CONFIG.colors[i//2 % (len(CONFIG.colors))]
            img.put(color, (x, y))
            img.put(color, (x, (CONFIG.HEIGHT - 1) - y)) 
            CONFIG.imag += CONFIG.d_over_h
        CONFIG.imag = CONFIG.start[1]
        CONFIG.real += CONFIG.d_over_w

    mainloop()

if __name__ == '__main__':
    magic()
