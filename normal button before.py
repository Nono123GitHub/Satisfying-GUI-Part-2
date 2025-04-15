from ursina import *
from pydub import AudioSegment
from pydub.playback import play
import threading

app = Ursina()

button = Button(
    text='Button',
    scale=(0.2, 0.1),
    x=0,
    y=-0,

)

app.run()