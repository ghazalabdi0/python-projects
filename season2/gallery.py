import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class GalleryApp(App):
    def build(self):
        self.image_folder = "images"  #the name of folder, it should ne in as same root as the main file

      #reading the images from folder
        self.images = [
            os.path.join(self.image_folder, file)
            for file in os.listdir(self.image_folder)
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        ]

        self.current_index = 0

        layout = BoxLayout(orientation="vertical")

        self.image_widget = Image()
        if self.images:
            self.image_widget.source = self.images[self.current_index]

        next_button = Button(text="next", size_hint=(1, 0.15))
        next_button.bind(on_press=self.show_next_image)

        layout.add_widget(self.image_widget)
        layout.add_widget(next_button)

        return layout

    def show_next_image(self, instance):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.image_widget.source = self.images[self.current_index]


GalleryApp().run()