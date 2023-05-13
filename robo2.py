import gtts
import playsound
text = input("enter the text :")
sound = gtts.gTTS(text, lang='hi')
sound.save('1.mp3')
playsound.playsound('1.mp3')
