"""This module contains the editor window."""
import knittingpattern
import os
from kivy.app import App
from .KnittingPatternWidget import KnittingPatternWidget
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button

class EditorWindow(App):

    """The editor window."""

    def build(self):
        """Build the UI elements."""
        self._patterns = knittingpattern.load_from().example("negative-rendering.json")
        pattern = self._patterns.patterns.at(0)
        self.pattern = KnittingPatternWidget()
        self.pattern.show_pattern(pattern)
        self.pattern.mark_row(pattern.rows.at(0))
        self.root = PageLayout()
        self.root.add_widget(self.pattern)
        self.root.add_widget(Button(text='Hello world'))


def main():
    """Open the editor window."""
    EditorWindow().run()

__all__ = ["main", "EditorWindow"]
