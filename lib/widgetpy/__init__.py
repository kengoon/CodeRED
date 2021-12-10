from kivy.properties import NumericProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard


class MD3Card(MDCard, FakeRectangularElevationBehavior):
    """Implements a material design v3 card."""
