import tkmacosx as tkm
from helpers import clean_screen
from json import load, dump
from PIL import ImageTk, Image
from canvas import frame, root


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open('db/products_data.json', 'r') as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)

        frame.create_text(
            x, y,
            text=item_name,
            font=('Courier', 15)
        )

        frame.create_image(x, y + 80, image=item_img)

        if item_info['quantity'] > 0:
            color = 'green'
            text = f'In stock: {item_info["quantity"]}'

            item_button = tkm.Button(
                root,
                text='Buy',
                bg='green',
                fg='white',
                font=('Courier', 15),
                width=50,
                activebackground='#53bda5',
                command=lambda x=item_name, y=info: buy_product(x, y)
            )
            frame.create_window(x, y+ 150, window=item_button)
        else:
            color = 'red'
            text = 'Out of Stock'
        frame.create_text(x, y + 180, text=text, fill=color, font=('Courier', 15))
        x += 200
        if x > 550:
            y += 230
            x = 150


def buy_product(product_name, info):
    info[product_name]['quantity'] -= 1

    with open('db/products_data.json', 'w') as stock:
        dump(info, stock)

    display_products()



images = []
