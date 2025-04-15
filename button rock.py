from ursina import *
from pydub import AudioSegment
from pydub.playback import play
import threading

drag = AudioSegment.from_wav("")
smash = AudioSegment.from_wav("")
app = Ursina()


first = True
particles = []

def spawn_particle(pos):
    vel = Vec3(
        random.uniform(-1, 1),
        random.uniform(1, 3),
        random.uniform(-1, 1)
    )
    lifespan = 10
    age = 0
    e = Entity(
        model='cube',
        color=color.gray,
        scale=0.3,
        position=pos
    )
    particles.append({'entity': e, 'vel': vel, 'lifespan': lifespan, 'age': age})

def burst_particles(pos):
    for _ in range(50):
        spawn_particle(pos)

def update():
    for p in particles[:]:
        p['entity'].position += p['vel'] * time.dt
        p['vel'].y -= 9 * time.dt  # gravity
        p['age'] += time.dt

        if p['age'] > p['lifespan']:
            destroy(p['entity'])
            particles.remove(p)

def on_click():
    global first
    if first:
        first = False
    else:
        pos = draggable_button.world_position  # Closest to internal drag tracking
        threading.Thread(target=play_sound_thread, daemon=True).start()
        burst_particles(pos)  # Spawn particles at correct 3D center
        destroy(draggable_button)


draggable_button = Draggable(
    text = "Button",
    model='quad',
    scale=(0.3, 0.3),
    color=color.gray,
    texture='white_cube',
    origin=(0,0),
    on_click=on_click
)

# Function to play sound in a thread
def play_sound_thread():
    global first
    if first == False:
        play(smash)
    else:    
        play(drag)

# on_drag with threading
def on_drag():
    threading.Thread(target=play_sound_thread, daemon=True).start()



draggable_button.drag = on_drag

app.run()

#slider = Slider(0, 20, default=10, height=Text.size*3,x=-0.09, y=-0.09, step=1, vertical=True)

#thin_slider = ThinSlider(text='height', dynamic=True,x=0.1)

#thin_slider.label.origin = (0,0)
#thin_slider.label.position = (1, 1)


