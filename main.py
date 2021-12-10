from sys import platform
if platform == "win32":
    from os import environ
    environ["KIVY_GL_BACKEND"] = "angle_sdl2"
from kivy.core.window import Window
import os
from time import sleep
from kivy.factory import Factory  # NOQA
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from lib.widgetpy.m_cardtextfield import M_CardTextField
from tools.iconfonts import register
from multiprocessing.dummy import Process

font_folder = "assets/font/"
register("icon", f"{font_folder}MaterialIconsRound-Regular.otf", f"{font_folder}googleIconRound.fontd")
Config.set("kivy", "exit_on_escape", "0")
Window.softinput_mode = 'below_target'
r = Factory.register
r("M_CardTextField", cls=M_CardTextField)


class CodeRED(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.font_styles.update(
            {
                "H1": [f"{font_folder}DINAlternate-bold", 96, False, -1.5],
                "H2": [f"{font_folder}DINAlternate-bold", 60, False, -0.5],
                "H3": [f"{font_folder}DINAlternate-bold", 48, False, 0],
                "H4": [f"{font_folder}avenir_heavy", 34, False, 0.25],
                "H5": [f"{font_folder}DINAlternate-bold", 24, False, 0],
                "H6": [f"{font_folder}DINAlternate-bold", 20, False, 0.15],
                "Button": [f"{font_folder}DINAlternate-bold", 14, True, 1.25],
                "Body1": [f"{font_folder}DINAlternate-bold", 16, False, 0.5],
                "Body2": [f"{font_folder}DINAlternate-bold", 14, False, 0.25],
            }
        )
        self.PYTHON_FILES = "lib/libpy/"
        self.KIVY_FILES = "lib/libkv/"
        self.PYTHON_WIDGET_FILES = "lib/widgetpy/"
        self.KIVY_WIDGET_FILES = "lib/widgetkv/"

    def build(self):
        Builder.load_file("imports.kv")
        return Builder.load_file("manager.kv")

    def on_start(self):
        from kivy import platform
        if platform == "android":
            self.start_service()
        Process(target=self.initiate_load_sequence).start()

    def initiate_load_sequence(self):
        sleep(3)
        self.load_screens()
        self.load_widgets()
        Clock.schedule_once(
            lambda x: exec("self.root.ids.manager.add_widget(Factory.Manager())", {"self": self, "Factory": Factory}))
        Clock.schedule_once(
            lambda x: exec("self.root.current = 'manager'", {"self": self}))
        Clock.schedule_once(
            lambda x: exec("self.root.ids.manager.children[0].current = 'login'", {"self": self}), timeout=2)

    def load_screens(self):
        # -------- import python screens -------- #
        libpy = os.listdir(self.PYTHON_FILES)
        for modules in libpy:
            exec(f"from lib.libpy import {modules.split('.')[0]}")
        # -------------------------------- #

        # ---------- load kivy screens ---------- #
        libkv = os.listdir(self.KIVY_FILES)
        for kv in libkv:
            Builder.load_file(f"{self.KIVY_FILES}{kv}")
        # --------------------------------------- #

    def load_widgets(self):
        # -------- import python screens -------- #
        libpy = os.listdir(self.PYTHON_WIDGET_FILES)
        for modules in libpy:
            if modules == "m_cardtextfield":
                continue
            exec(f"from lib.widgetpy import {modules.split('.')[0]}")
        # -------------------------------- #

        # ---------- load kivy screens ---------- #
        libkv = os.listdir(self.KIVY_WIDGET_FILES)
        for kv in libkv:
            Builder.load_file(f"{self.KIVY_WIDGET_FILES}{kv}")
        # --------------------------------------- #

    @staticmethod
    def start_service():
        from jnius import autoclass
        service = autoclass("org.mindset.codered.ServiceCodered")
        mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
        service.start(mActivity, "")
        return service


CodeRED().run()
