# Modules:
from pygame import mixer

# Load Sounds:
mixer.init()

sounds = {
   'main_menu':  [
      mixer.Sound('Sounds/main_menu_music.mp3'),
      mixer.Sound('Sounds/main_menu_movement.mp3')
                  ]
}

channel1 = mixer.Channel(1)
channel2 = mixer.Channel(2)
channel3 = mixer.Channel(3)
channel4 = mixer.Channel(4)
channel5 = mixer.Channel(5)
