## ATTACK VECTORS PAGE ##

import tkinter as tk  # python 3
# import tkFont as tkfont  # python 2

from tkinter import font as tkfont, ttk
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg
from nav_bar import *
from vector_descriptions import *


class VectorsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # displays navbar at top of app screen
        display_nav_bar(self, controller)
        # sets font for frame
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        # sets font for buttons
        btnfont = tkfont.Font(family='Calibri', size=13)

        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#232536', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="Attack Vectors List", bg='#4D6C84', fg='white', anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)

        # extra frame for spacing, pushes all subsquent content below nav bar and title label using the pady field
        frameextra = tk.Label(self, bg='#4D6C84')
        frameextra.pack(pady=120)

        # new frame for tools list
        container = Frame(self)
        container.pack(fill='both', expand=True)
        # create a canvas on the new frame
        canvas = Canvas(container)

        # create scrollbar on new frame
        # scrollbar y
        scrollbar_y = Scrollbar(container,
                                orient=VERTICAL,
                                command=canvas.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_y.config(command=canvas.yview)
        # create scrollbar x
        scrollbar_x = Scrollbar(container,
                                orient=HORIZONTAL,
                                command=canvas.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_x.config(command=canvas.xview)
        # create new canvas that will be scrolled
        scrollable_frame = Frame(canvas)
        # binds scroll canvas to execute function that gets scrollable region of canvas on event e
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("alsl")))

        # creates new window using scrollable frame as a base
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # sets scrollcommand to the existing scrollbar, linking the widgets
        canvas.config(
            xscrollcommand=scrollbar_x.set,
            yscrollcommand=scrollbar_y.set
        )
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        # creates new image variable from start_button.png, used for launch button on vector entry
        global button_image
        button_image = tk.PhotoImage(file='resources/start_button.png')
        global info_image
        info_image = tk.PhotoImage(file='resources/Info_button.png')

        # packs passed widget to the left of screen, used for creating a vector entry
        def pack_widget_left(button):
            button.pack(fill='x', padx=80, pady=(5, 5), side=LEFT)

        # same as above but to right of screen
        def pack_widget_right(button):
            button.pack(fill='x', padx=120, pady=(5, 5), side=RIGHT)

        # creates a vector entry using passed strings and command function
        def create_attack_vector(name, author, onclick_pagenav, desc):
            # creates new canvas to hold vector information/execute widgets
            vector_canvas = tk.Canvas(scrollable_frame, height=10, bg="#E3E4E5")

            vectorname_label = tk.Label(vector_canvas, text=name, height=2, font='controller.btn_font2 20 bold',
                                        bg="#E3E4E5")
            pack_widget_left(vectorname_label)

            nav_button = tk.Button(vector_canvas, bg="#4D6C84", compound=LEFT, text="LAUNCH", fg="white",
                                   font="controller.btn_font2 12 bold",
                                   command=lambda: controller.show_frame(onclick_pagenav))
            pack_widget_right(nav_button)
            info_button = tk.Button(vector_canvas, image=info_image, compound=LEFT,
                                    command=lambda: self.show_hint(desc), relief=FLAT, bg="#E3E4E5", borderwidth=0)
            pack_widget_right(info_button)

            author_label = tk.Label(vector_canvas, text=author, font="controller.btn_font2 12", height=2, bg="#E3E4E5")
            pack_widget_right(author_label)

            vector_canvas.pack(expand=TRUE, fill='x', padx=190, pady=20)

        # creates vector entries
        # if you want to add a new vector entry,
        # 1. invoke create_attack_vector
        # 2. enter the name, author, version and pageName you want to navigate to on button click
        # 3. make sure you enter the name of the page defined in main.py at line 35
        # 4. You're done, run the app and see your new vector
        create_attack_vector("Reverse TCP Shell", "Daniel Sacchetta", "AttackVectorOne",
                             REVERSE_TCP_DESC)
        create_attack_vector("Directory Triversal & IDOR", "Ryan Harris", "AttackVectorTwo",
                             DIR_TRAV_IDOR_DESC)
        create_attack_vector("Unpatched Vulnerabilities and Exploits", "Adrian Nadalin",
                             "AttackVectorThree", UNPATCH_VULN_EXP_DESC)
        create_attack_vector("Web Application Attacks: Automated XSS and SQLiInjection attack",
                             "Nancy Patel", "AttackVectorFour", WEB_APP_XSS_SQLI_DESC)
        create_attack_vector("NFS Privilege Escalation", "Mohammed Alassiri", "AttackVectorSeven",
                             NFS_PRIV_ESC_DESC)
        create_attack_vector("apache Webserver Exploit", "Taylor Smith", "AttackVectorEight", APACHE_DESC)
        create_attack_vector("Authentication Bypass Attack", "Thanh Bao Chau Le", "AttackVectorNine",
                             AUTH_BYPASS_DESC)

        # used for spacing purposes, extends width of vector listing to look nicer
        space = tk.Label(scrollable_frame,
                         text="                                                                                                                                                                                                                                                         ",
                         height=0).pack(fill=BOTH, expand=True)

    def show_hint(self, desc):
        desc_label = tk.Label(self, text=desc + "\n\n\n\nClick to dismiss", bg='#6f8396', fg='white', borderwidth=8,
                              relief=RAISED,
                              font=("Calibri", 15))
        desc_label.place(rely=0.125, relx=0.25, relheight=0.75, relwidth=0.5)
        desc_label.bind("<Button-1>", lambda x: desc_label.place_forget())

        # binds the labels configure action to execute the set_label_wrap function
        # This will run when the screen is resized
        desc_label.bind("<Configure>", self.set_label_wrap)

    # dynamically updates the wraplength of the labels so that the text fits to the width properly
    def set_label_wrap(self, event):
        wraplength = event.width - 100  # the 8 is for padding (makes it look nicer)
        event.widget.configure(wraplength=wraplength)
