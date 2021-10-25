import random
import qrcode
from khayyam import JalaliDatetime
import telebot
from gtts import gTTS
import pysynth_b

mybot = telebot.TeleBot("2040244984:AAHV8aDeygsxxHmuFSu3ZfN4tf_3aDaIglg",parse_mode="None")

@mybot.message_handler(commands=['start'])
def send_welcome(message: str):
    user_first_name = str(message.chat.first_name)
    mybot.reply_to(message, 'Hi ' + user_first_name + ' welcome to my bot ^^')

@mybot.message_handler(commands=['game'])
def gamei(message):
  mybot.reply_to(message, "Guess the number from(0 to 500): ")
  mybot.register_next_step_handler(message, guessnumber)
  global pc_num
  pc_num=random.randint(0,500)
  print(pc_num)

def guessnumber(message):
    
  user_number = int(message.text)

  if pc_num==user_number:
    mybot.reply_to(message,"hooray you win")
        
  elif user_number>pc_num:
    mybot.reply_to(message,"it's lower")
    mybot.register_next_step_handler(message, guessnumber)
    
  elif user_number<pc_num:
    mybot.reply_to(message,"it's upper")
    mybot.register_next_step_handler(message, guessnumber)

@mybot.message_handler(commands=['age'])
def age_func(message):
  mybot.send_message(message.chat.id, 'Enter your birthdate here:\n\n e.g. 1380/1/21')
  mybot.register_next_step_handler(message, age_)
def age_(message):
  message_text = message.text
  userBirth = message_text.split('/')
  if len(userBirth[0])==4:
    difference = JalaliDatetime.now() - JalaliDatetime(userBirth[0], userBirth[1], userBirth[2])
    mybot.send_message(message.chat.id, 'You are '+ str(difference.days//365)+' year old')
  else:
    mybot.reply_to(message, 'You enter a wrong date type')

@mybot.message_handler(commands=['voice'])
def text_to_voice(message):
  mybot.reply_to(message, "Enter a text we convert it to voice")
  mybot.register_next_step_handler(message, texttospeech)
def texttospeech(message):
  message_text = message.text
  language = 'en'
  myobj = gTTS(text = message_text, lang = language, slow = False)
  myobj.save("voice.mp3")
  audio = open("voice.mp3", "rb")
  mybot.send_audio(message.chat.id, audio)
# دستور جدید
@mybot.message_handler(commands=['music'])
def note_to_music(message):
  mybot.reply_to(message, "Enter the note in form : ('note' , duration ),('note' , duration)... we will convert it to a music")
  mybot.register_next_step_handler(message, notetomusic)

def notetomusic(message):
  try:
    message_text = eval(message.text)
    pysynth_b.make_wav(message_text, fn = "test.wav")
    audio = open("test.wav", "rb")
    mybot.send_audio(message.chat.id, audio)
  except:
    mybot.reply_to(message, "Please enter your notes base on a form above ^^")

@mybot.message_handler(commands=['max'])
def max_num(message):
  global list 
  list = []
  mybot.reply_to(message, "Enter the numbers:\n e.g: 1,5,2")
  mybot.register_next_step_handler(message,calmax)
def calmax(message):
  message_text = message.text
  numbers = message_text.split(',')
  for num in numbers:
    list.append(int(num))
  maxnum = max(list)
  mybot.reply_to(message, f'The largest number in your list is {maxnum}')

@mybot.message_handler(commands=['argmax'])
def argmax_num(message):
  global list 
  list = []
  mybot.reply_to(message, "Enter the numbers:\n e.g: 1,5,2")
  mybot.register_next_step_handler(message,argmax)
def argmax(message):
  message_text = message.text
  numbers = message_text.split(',')
  for num in numbers:
    list.append(int(num))
  maxnum = max(list)
  max_index = list.index(maxnum)
  mybot.reply_to(message, f'The index of largest number in your list is {max_index}')

@mybot.message_handler(commands=['qrcode'])
def creat_qrcode(message):
  mybot.reply_to(message, "Enter a text you want to creat a QR Code from:")
  mybot.register_next_step_handler(message,myqrcode)
def myqrcode(message):
  message_text = message.text
  img = qrcode.make(message_text)
  img.save('qrcode.png')
  photo = open('qrcode.png', 'rb')
  mybot.send_photo(message.chat.id, photo)

@mybot.message_handler(commands=['help'])
def help_(message):
  mybot.reply_to(message, "\n/game  بازی حدس عدد \n/age  تبدیل تاریخ تولد به سن\n/voice  تبدیل متن به صدا \n/make music  تبدیل نت به موسیقی \n/max  نمایش بزرگترین عدد  \n/argmax  نمایش شماره اندیس عدد بزرگتر  \n/qrcode   QR Code ساخت   ")

@mybot.message_handler(func=lambda message:True)
def anysentences(message):
  mybot.reply_to(message,"Use commands")

mybot.polling()
