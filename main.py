import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class WebPageApp(App):
    def build(self):
        self.content_label = Label(text="Conteúdo da página será exibido aqui.")
        self.fetch_button = Button(text="Buscar Conteúdo", on_press=self.fetch_content)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.content_label)
        layout.add_widget(self.fetch_button)

        return layout

    def fetch_content(self, instance):
        url = "http://localhost:1880/mensagem"  # Substitua pelo URL da página que deseja buscar
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content = response.text
                self.content_label.text = content
                
            else:
                self.content_label.text = f"Erro ao buscar conteúdo. Código de status: {response.status_code}"
        except Exception as e:
            print("Erro ao buscar conteúdo:", e)
            self.content_label.text = "Erro ao buscar conteúdo. Verifique sua conexão com a internet."

if __name__ == '__main__':
    WebPageApp().run()



