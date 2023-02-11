from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('roa-music-daybreak.mp3')
play(sound)
