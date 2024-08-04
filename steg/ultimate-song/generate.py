import wave
import numpy as np
import subprocess

# Configuration variables
download_link = "https://archive.org/details/rick-roll"
input_video = 'input.mp4'
output_video = 'awesome-song.mp4'
output_audio = 'awesome-song.mp3'
# flag = 'SOS'
# flag = 'pecan{thi5_15_r1ck_r0lling_fun}'
flag = 'pecan(thi5-15-r1ck-fun)'
hidden_message = f"{flag}	{flag}	{flag}	  SOS SOS SOS SOS SOS SOS SOS SOS SOS"
# hidden_message = f"{flag}"


# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/', '	': '	'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        if char == '	': 
            morse_code += char
    return morse_code

def morse_to_audio(morse_code, filename, dot_length=0.1, freq=550, sample_rate=44100):
    print(morse_code)
    audio = np.array([])
    for symbol in morse_code:
        dot = np.sin(2 * np.pi * np.arange(sample_rate * dot_length) * freq / sample_rate)
        dash = np.sin(2 * np.pi * np.arange(sample_rate * dot_length * 3) * freq / sample_rate)
        silence_dot = np.zeros(int(sample_rate * dot_length * 2))
        silence_dash = np.zeros(int(sample_rate * dot_length * 2))
        silence_between = np.zeros(int(sample_rate * dot_length * 7))
        silence_gap = np.zeros(int(sample_rate * dot_length * 14))

        if symbol == '.':
            audio = np.concatenate((audio, dot, silence_dot))
        elif symbol == '-':
            audio = np.concatenate((audio, dash, silence_dash))
        elif symbol == ' ':
            audio = np.concatenate((audio, silence_between))
        elif symbol == '	':
            audio = np.concatenate((audio, silence_gap))
            freq += 250
        # elif symbol == '/':
        #     freq += 100

    audio = np.int16(audio / np.max(np.abs(audio)) * 32767)

    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, sample_rate, len(audio), 'NONE', 'not compressed'))
        wav_file.writeframes(audio.tobytes())

# Generate Morse Code Audio
morse_code = text_to_morse(hidden_message)
morse_audio_file = 'morse_code.wav'
morse_to_audio(morse_code, morse_audio_file)

# Paths to input and output files
original_audio_file = 'original_audio.wav'
mixed_audio_file = 'mixed_audio.wav'

# Extract Original Audio from Video
subprocess.run(['ffmpeg', '-y', '-i', input_video, '-q:a', '0', '-map', 'a', original_audio_file])

# Mix Original Audio with Morse Code Audio
subprocess.run(['ffmpeg', '-y', '-i', original_audio_file, '-i', morse_audio_file, '-filter_complex', '[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=2', mixed_audio_file])

# Replace the Audio Track in the Video
subprocess.run(['ffmpeg', '-y', '-i', input_video, '-i', mixed_audio_file, '-c:v', 'copy', '-map', '0:v:0', '-map', '1:a:0', output_video])

# Convert Mixed Audio to MP3
subprocess.run(['ffmpeg', '-y', '-i', mixed_audio_file, output_audio])

# Convert Mixed Audio to MP3 with *fake* Metadata
audio_metadata = {
    'title': 'The Duck Song',
    'artist': 'Bryant Oden + forrestfire101',
    'album': 'Youtube Animations',
    'album_artist': 'Various Artists',
    'track': '1',
    'year': '2009',
    'date': '2009',
    'comment': 'Enjoy this track!',
    'subtitle': 'Mp3 version of YouTube so I can listen!',
    'synopsis': 'Mp3 version of YouTube so I can listen!',
    'rating': '5',
    'copyright': 'https://www.youtube.com/watch?v=MtN1YnoL46Q'
}
metadata_args = []
for key, value in audio_metadata.items():
    metadata_args.extend(['-metadata', f'{key}={value}'])

subprocess.run(['ffmpeg', '-y', '-i', mixed_audio_file, *metadata_args, output_audio])