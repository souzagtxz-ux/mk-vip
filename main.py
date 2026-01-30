from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock

class MkVipOverlay(App):
    def build(self):
        # Configura o tamanho da janelinha de tradução
        Window.size = (800, 200) 
        # Tenta manter a janela sempre no topo (sobreposição)
        Window.always_on_top = True
        
        self.label = Label(
            text="MK VIP: Aguardando áudio do YouTube...",
            font_size='18sp',
            bold=True,
            color=(1, 1, 0, 1) # Texto Amarelo para destacar no vídeo
        )
        return self.label

    # Aqui entraria a função que escuta o áudio e muda o self.label.text
if __name__ == "__main__":
    MkVipOverlay().run()
