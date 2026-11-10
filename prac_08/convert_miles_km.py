from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometers."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, miles):
        """Handle calculation from miles to kilometers when button is pressed."""
        self.output_km = str(self.convert_to_float(miles) * MILES_TO_KM)

    def handle_increment(self, miles, change):
        """Handle increment when the up or down button is pressed, updating the input with new value."""
        miles = self.convert_to_float(miles) + change
        self.root.ids.input_miles.text = str(miles)

    def convert_to_float(self, text):
        """Convert the text to a float if valid number, otherwise set it to 0.0."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
