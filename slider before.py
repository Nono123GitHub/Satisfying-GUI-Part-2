from ursina import *

app = Ursina()
slider = Slider(0, 30, default=10, height=Text.size*3, x=-0.09, y=-0.09, step=1,dynamic=True, vertical=True)


app.run()