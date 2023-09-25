# Long-Form-TTS-ElevenLabs
This simple project aims to make easier long form TTS synthesis, using ElevenLabs API.
# Downloading
To get this project in your computer, download the code from Code > Download ZIP.
Or type this command:
```bash
git clone https://github.com/javi22020/Long-Form-TTS-ElevenLabs.git
```
# How to use
To use this script, you'll need an Internet connection and a (preferably) paid ElevenLabs account.
1. Get your API key from https://elevenlabs.io/
2. Edit the 'main.py' file and replace YOUR-ELEVENLABS-API-KEY-HERE (line 6) with the API key you just copied.
3. Double click on 'Install requirements.bat'. This will automatically install all libraries the script needs.
4. Inside the 'texts' folder, edit or create as many .txt files as you want. Each text file will create an audio file as output.
5. Now run 'main.py'. You can do this by double-clicking on 'RunTTS.bat' or by opening a terminal in the main folder and typing 'python main.py'.
6. The script will generate the audio using your ElevenLabs API.
# Some notes
- Check the text files in the 'texts' folder every time you run the program, to avoid generating the same audio twice or unnecesary audio.
- If the number of characters in the ElevenLabs account isn't enough to generate audio for the text, a warning will be shown.
- It's highly recommended to use a paid account, as the free tier only offers up to 10,000 characters.
# Disclaimer
- Don't use or modify this program to bypass ElevenLabs Terms of Service.
