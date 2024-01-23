from tkinter import Button, Entry, Label
from canvas import root, frame
import tkmacosx as tkm
from helpers import clean_screen, get_password_hash
from PIL import ImageTk, Image
from json import dump, loads
from buying_page import display_products

login_screen = None


def render_entry():
    store_image = ImageTk.PhotoImage(Image.open('db/images/pngwing.com-4.png'))
    frame.create_image(350, 250, image=store_image)
    images.append(store_image)
    register_button = tkm.Button(
        root,
        text='Register',
        bg='#00CDAC',
        fg='white',
        borderwidth=0,
        width=200,
        height=30,
        font='Courier',
        activebackground='#8DD7BF',
        command=register
    )

    login_button = tkm.Button(
        root,
        text='Login',
        bg='#00b0ba',
        fg='white',
        borderwidth=0,
        width=200,
        height=30,
        font='Courier',
        activebackground='#8DD7BF',
        command=login
    )

    frame.create_window(350, 520, window=register_button)
    frame.create_window(350, 560, window=login_button)


def login():
    global login_screen
    login_screen = True
    clean_screen()

    frame.create_text(100, 50, text='Username:', font='Courier')
    frame.create_text(100, 100, text='Password:', font='Courier')

    frame.create_window(230, 50, window=username_box)
    frame.create_window(230, 100, window=password_box)

    register_button = tkm.Button(
        root,
        text='Register',
        bg='#00CDAC',
        fg='white',
        borderwidth=0,
        width=150,
        height=30,
        font='Courier',
        activebackground='#8DD7BF',
        command=register
    )

    frame.create_window(250, 150, window=login_button)
    frame.create_window(400, 150, window=register_button)
    frame.create_window(350, 100, window=show_button)


def register():
    global login_screen
    login_screen = False
    clean_screen()

    frame.create_text(100, 50, text='First name:', font='Courier')
    frame.create_text(100, 100, text='Last name:', font='Courier')
    frame.create_text(100, 150, text=' Username:', font='Courier')
    frame.create_text(100, 200, text='Password:', font='Courier')

    frame.create_window(240, 50, window=first_name_box)
    frame.create_window(240, 100, window=last_name_box)
    frame.create_window(240, 150, window=username_box)
    frame.create_window(240, 200, window=password_box)
    frame.create_window(350, 200, window=show_button)

    register_button = tkm.Button(
        root,
        text='Register',
        bg='#00CDAC',
        fg='white',
        borderwidth=0,
        width=200,
        height=25,
        font='Courier',
        activebackground='#8DD7BF',
        command=registration
    )
    frame.create_window(300, 250, window=register_button)


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(250, 180, text='Invalid username or password!', fill='red')


def check_logging():
    info_data = get_users_data()

    current_user_username = username_box.get()
    current_user_password = get_password_hash(password_box.get())

    for record in info_data:
        record_username = record['Username']
        record_password = record['Password']

        if current_user_username == record_username and current_user_password == record_password:
            return True

    return False


def get_users_data():
    info_data = []

    with open('db/users_information.txt', 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def registration():
    info_dict = {
        'First name': first_name_box.get(),
        'Last name': last_name_box.get(),
        'Username': username_box.get(),
        'Password': password_box.get(),
    }

    if check_registration(info_dict):
        with open('db/users_information.txt', 'a') as users_file:
            info_dict['Password'] = get_password_hash(info_dict['Password'])
            dump(info_dict, users_file)
            users_file.write('\n')
            display_products()


def check_registration(info):
    frame.delete('error')

    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                300,
                330,
                text=f'{key} cannot be empty!',
                fill='red',
                tags='error'
            )
            return False

    info_data = get_users_data()

    for record in info_data:
        if record['Username'] == info['Username']:
            frame.create_text(
                300,
                330,
                text='Username is already taken!',
                fill='red',
                tags='error'
            )
            return False

    return True


# password show button
def show():
    hide_button = tkm.Button(
        root,
        image=hide_image,
        command=hide,
        bd=0,
        bg='white',
        activebackground='white'
    )
    if not login_screen:
        frame.create_window(350, 200, window=hide_button)
    else:
        frame.create_window(350, 100, window=hide_button)
    password_box.config(show='')


# password hide button
def hide():
    show_button = tkm.Button(
        root,
        image=show_image,
        command=show,
        activebackground='white',
        bd=0
    )
    if not login_screen:
        frame.create_window(350, 200, window=show_button)
    else:
        frame.create_window(350, 100, window=show_button)
    password_box.config(show='*')


show_image = ImageTk.PhotoImage(file='db/images/show-2.png')
hide_image = ImageTk.PhotoImage(file='db/images/hide-2.png')

show_button = tkm.Button(root, image=show_image, command=show, bd=0)

first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, highlightthickness=2.4, show='*')

login_button = tkm.Button(
    root,
    text='Login',
    bg='#00b0ba',
    fg='white',
    borderwidth=0,
    width=150,
    height=30,
    font='Courier',
    activebackground='#8DD7BF',
    command=logging
)

login_button['state'] = 'disabled'


# disable / # enable login button
def print_event(event):
    info = [
        username_box.get(),
        password_box.get()
    ]
    for el in info:
        if not el.strip():
            login_button['state'] = 'disabled'
            break
    else:
        login_button['state'] = 'normal'


root.bind('<KeyRelease>', print_event)

images = []
