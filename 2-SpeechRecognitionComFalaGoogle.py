import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/teste.mp3')
    print("Estou aprendendo o que você disse...")
    playsound('audios/teste.mp3')

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #redução de ruído
        microfone.adjust_for_ambient_noise(source)
        
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
        
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase


frase = ouvir_microfone()
cria_audio(frase)