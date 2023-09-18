from elevenlabs.api import User
from elevenlabs import set_api_key, generate
import os

# ---------------------------- CONFIGURACIÓN ---------------------------
xi_api_key = "YOUR-ELEVENLABS-API-KEY-HERE"
character_limit = 5000 # 2500 for free acounts, 5000 for paid accounts
# ---------------------------- CONFIGURACIÓN ---------------------------


def generar_audio(texto, api):
    set_api_key(api)
    print("Generating audio...")
    audio = generate(
        text=texto,
        voice="Bella",
        model="eleven_multilingual_v1"
    )
    print("Audio generated. ")
    return audio


def split_text_into_segments(text, max_segment_length):
    words = text.split()  # Divides text in words
    segments = []
    current_segment = []

    for word in words:
        if sum(len(w) for w in current_segment) + len(current_segment) + len(word) <= max_segment_length:
            current_segment.append(word)
        else:
            segments.append(" ".join(current_segment))
            current_segment = [word]

    if current_segment:
        segments.append(" ".join(current_segment))

    return segments


list_texts = os.listdir("texts")
list_path_texts = list(map(lambda file: "texts/" + file, list_texts))
print(str(len(list_texts)) + " text files detected")
set_api_key(xi_api_key)
user = User.from_api()

for i in range(len(list_path_texts)):
    text_complete = open(list_path_texts[i]).read()
    print("Generating audio for text #" + str(i))
    if len(text_complete) > user.subscription.character_limit - user.subscription.character_count:
        print("There aren't enough characters left in the ElevenLabs API key. You may have to extend your subscription tier or wait for the character refill. ")
        input()
        exit(0)
    segmentos = split_text_into_segments(text_complete, character_limit)
    audiodef = bytes()
    for seg in segmentos:
        audiodef += generar_audio(seg, xi_api_key)
    if not os.path.exists("audios"):
        print("'audios' folder doesn't exist, it will be created now. ")
        os.mkdir("audios")
    with open("audios/tts-" + str(i) + ".mp3", "wb") as f:
        f.write(audiodef)

print("Program has ended. ")
input()
exit()


