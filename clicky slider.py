from ursina import *
from pydub import AudioSegment
from pydub.playback import play
import threading
import time

click = AudioSegment.from_wav("C:\\Users\\nshei\\Desktop\\youtube code\\satisfying pt 2\\click.wav")

app = Ursina()
slider = Slider(0, 30, default=10, height=Text.size*3,x=-0.09, y=-0.09, step=5,dynamic=True, vertical=True)
slider.knob.color = color.lime.tint(-0.2)

def tone():
    val = slider.value
    def play_tone():
        play(click+10)
    threading.Thread(target=play_tone).start()

slider.on_value_changed = lambda: tone()

app.run()