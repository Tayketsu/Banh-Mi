#from kivy.app import App
#
#class MyFirebase():
#    wak = "AIzaSyB49T25fdl4v4vNNycrlLISaRc2Op8-z-Y"  # Web Api Key
#
#    def sign_up(self, email, password):
#        app = App.get_running_app()
#        app.on_start()
#
#
#if __name__ == '__main__':
#    # example modified from the scrollview example
#
#    from kivy.uix.gridlayout import GridLayout
#    from kivy.uix.button import Button
#    from kivy.uix.scrollview import ScrollView
#    from kivy.garden.roulettescroll import RouletteScrollEffect
#    from kivy.base import runTouchApp
#
#    layout = GridLayout(cols=1, padding=10,
#            size_hint=(None, None), width=500)
#
#    layout.bind(minimum_height=layout.setter('height'))
#
#    for i in range(30):
#        btn = Button(text=str(i), size=(480, 40),
#                     size_hint=(None, None))
#        layout.add_widget(btn)
#
#    root = ScrollView(size_hint=(None, None), size=(500, 320),
#            pos_hint={'center_x': .5, 'center_y': .5}
#            , do_scroll_x=False)
#    root.add_widget(layout)
#
#    root.effect_y = RouletteScrollEffect(anchor=20, interval=40)
#    runTouchApp(root)