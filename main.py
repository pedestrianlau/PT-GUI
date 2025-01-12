import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from AboutPage import AboutPage
from VectorsPage import VectorsPage
from ToolsPage import ToolsPage
from ReferencesPage import ReferencesPage
from ATTACKVECTOR.attackvector1 import AttackVectorOne
from ATTACKVECTOR.attackvector3 import AttackVectorThree
from ATTACKVECTOR.attackvector2 import AttackVectorTwo
from StartPage import StartPage
from ReconnaissanceTools.PortScanner import PortScan
from EnumerationTools.TestSniffer import TestSniff
from EnumerationTools.MacChanger import MacChange
from Tools.Notepad import *
from ReconnaissanceTools.BannerGrabbing import BannerGrab
from Payload.MsfvenomPayloadGenerator import MsfPayloadGen
from ExecutionTools.MsfconsoleListener import MsfListener
from ExecutionTools.Spoof import MimtDnsSpoof
from ExecutionTools.FTPBruteForce import FTPBruteForce
from Fuzzers.DirectoryTraversalFuzzer import DTFuzz
from EnumerationTools.ImageMetaDataExtractor import IMDExtractor
from ATTACKVECTOR.attackvector7 import AttackVectorSeven
from ATTACKVECTOR.attackvector8 import AttackVectorEight
from ATTACKVECTOR.attackvector9 import AttackVectorNine
from InitialAccessTools.sshbrute import SshBrute
from EnumerationTools.hash_analyzer import HashAn
from InitialAccessTools.PasswordHashCracker import PHCracker
from InitialAccessTools.ZipBruteForce import ZipBF
from ExecutionTools.ICMPPingFlooder import ICMP
from EnumerationTools.HTTPheaders import HTTPheaders
from WalkthroughsPage import WalkthroughClass
from ATTACKVECTOR.attackvector4 import AttackVectorFour


# from WordlistGen_final import WordlistGen

class GUIApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # sets fonts (I dont think it sets them globally)
        self.title_font = tkfont.Font(family='Calibri', size=18, weight="bold")
        self.btn_font = tkfont.Font(family='Calibri', size=18)
        self.btn_font2 = tkfont.Font(family='Calibri', size=12)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creates a list of frames
        self.frames = {}
        # iterates through every object listed in brackets
        for F in (StartPage, AboutPage, VectorsPage, ToolsPage, ReferencesPage, AttackVectorOne, AttackVectorThree,
                  AttackVectorTwo, PortScan, TestSniff, MacChange, BannerGrab, MsfPayloadGen, MsfListener, MimtDnsSpoof,
                  DTFuzz,
                  FTPBruteForce, IMDExtractor, AttackVectorSeven, AttackVectorEight, AttackVectorNine, AttackVectorFour,
                  SshBrute, HashAn, PHCracker, ZipBF, ICMP, HTTPheaders, WalkthroughClass):
            # sets page_name variable equal to current object's name
            page_name = F.__name__
            # creates new frame
            frame = F(parent=container, controller=self)
            # updates list of frames contained within self with the page_name variable
            # and links the page_name to the new frame just created
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # shows the start page by default
        self.show_frame("StartPage")

    # function that takes a page_name as a string and raises that page up to the top (meaning it is now visible)
    def show_frame(self, page_name):
        # new frame variable points to the frame associated with the page name passed to it
        frame = self.frames[page_name]
        # frame is raised up to be visible
        frame.tkraise()


if __name__ == "__main__":
    app = GUIApp()

    app.title("Deakin Detonator Toolkit")
    # getting the width & height of display screen
    screenwidth = app.winfo_screenwidth()
    screenheight = app.winfo_screenheight()
    # setting the size of window %d refers to the numbers contained within the brackets eg screenwidth
    app.geometry("%dx%d" % (screenwidth, screenheight))

    app.mainloop()
