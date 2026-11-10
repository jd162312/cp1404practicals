from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabelsApp(App):
    """Kivy app to create dynamic labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.number_to_name = {1: "Bob Brown", 2: "Cat Cyan", 3: "Oren Ochre"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.number_to_name.values():
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
