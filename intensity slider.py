from ursina import *
from pydub import AudioSegment
from pydub.playback import play
import threading
import time

# Load audio files
high = AudioSegment.from_wav("C:\\Users\\nshei\\Desktop\\youtube code\\satisfying pt 2\\intensity\\high.wav")
mid = AudioSegment.from_wav("C:\\Users\\nshei\\Desktop\\youtube code\\satisfying pt 2\\intensity\\mid.wav")
low = AudioSegment.from_wav("C:\\Users\\nshei\\Desktop\\youtube code\\satisfying pt 2\\intensity\\low.wav")

# Initialize app and slider
app = Ursina()
slider = Slider(0, 30, default=10, height=Text.size*3, x=-0.09, y=-0.09, step=10,dynamic=True, vertical=True)

slider_label = Text(text=f'Intensity: {slider.value}', position=(0.1, 0.1), origin=(0, 0), scale=1.2)
slider_label.color = color.lime

def tone():
    val = slider.value
    slider_label.text = f'Intensity: {val}'

    # Set color based on value
    if val <= 10:
        slider.knob.color = color.lime
        slider_label.color = color.lime
    elif val <= 20:
        slider.knob.color = color.yellow
        slider_label.color = color.yellow
    else:
        slider.knob.color = color.red
        slider_label.color = color.red

    # Play the tone in a separate thread
    def play_tone():
        if val <= 10:
            play(low)
        elif val <= 20:
            play(mid)
        else:
            play(high)
        time.sleep(1)

    threading.Thread(target=play_tone).start()

# Bind the value change to the tone function
slider.on_value_changed = lambda: tone()

app.run()
