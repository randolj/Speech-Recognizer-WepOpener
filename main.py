import speech_recognition as sr
import webbrowser as web

path = "/Users/randoljrecio/Desktop/Google Chrome"
r = sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.2)

    print("What wesbite would you like to visit?")
    audio = r.listen(source)
    print("Reconizing Now")
    try:
        dest = r.recognize_google(audio)
        print("You have said : " + dest)

        web.get("safari").open(dest)
    except Exception as e:
        print("Error " + str(e))
