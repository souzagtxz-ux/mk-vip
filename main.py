from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import threading

class MkVipApp(App):
    def build(self):
        self.title = "mk vip"
        layout = BoxLayout(orientation='vertical', padding=20)
        self.lbl = Label(text="Aguardando comando...", font_size='20sp')
        
        btn = Button(
            text="TRADUZIR PARA PORTUGUÊS",
            background_color=(0, 0.7, 0, 1), # Verde
            font_size='18sp'
        )
        btn.bind(on_press=self.start_translation)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def start_translation(self, instance):
        self.lbl.text = "Ouvindo áudio interno..."
        # Aqui entra a lógica de tradução que já testamos
        
if __name__ == "__main__":
    MkVipApp().run()
