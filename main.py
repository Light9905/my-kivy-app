from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CuaApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.spinner = Spinner(
            text='Chọn loại cửa',
            values=('Cửa đi 1 cánh', 'Cửa sổ lùa 2 cánh'),
            size_hint=(1, None),
            height=44
        )
        self.add_widget(self.spinner)

        self.input_a = TextInput(hint_text='Nhập chiều rộng (A)', input_filter='int', multiline=False)
        self.add_widget(self.input_a)

        self.input_b = TextInput(hint_text='Nhập chiều cao (B)', input_filter='int', multiline=False)
        self.add_widget(self.input_b)

        self.result = Label(size_hint=(1, 0.5))
        self.add_widget(self.result)

        btn = Button(text='Tính toán', size_hint=(1, None), height=44)
        btn.bind(on_press=self.tinh_toan)
        self.add_widget(btn)

    def tinh_toan(self, instance):
        try:
            A = int(self.input_a.text)
            B = int(self.input_b.text)
            loai = self.spinner.text

            if loai == 'Cửa đi 1 cánh':
                C = A - 58
                D = B - 35
            elif loai == 'Cửa sổ lùa 2 cánh':
                C = (A + 20) / 2
                D = B - 68
            else:
                self.result.text = "Vui lòng chọn loại cửa."
                return

            self.result.text = f"Chiều rộng = {C}\nChiều cao = {D}"
        except:
            self.result.text = "Vui lòng nhập A và B là số nguyên."

class MyApp(App):
    def build(self):
        return CuaApp()

MyApp().run()