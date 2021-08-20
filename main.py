from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from tools.iconfonts import register

font_folder = "assets/font/"
register("icon", f"{font_folder}MaterialIconsRound-Regular.otf", f"{font_folder}googleIconRound.fontd")
Config.set("kivy", "exit_on_escape", "0")
Window.softinput_mode = 'below_target'


class CodeRED(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A700"
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

    def build(self):
        Builder.load_file("imports.kv")
        return Builder.load_file("manager.kv")


CodeRED().run()
