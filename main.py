import calendar
from datetime import date

from backend import *
from parser import *
from data import *
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu
calendar.setfirstweekday(calendar.SUNDAY)
KV = '''
<ContentNavigationDrawer>:
    ScrollView:        
        MDList:
            MDFloatingActionButton:

            OneLineListItem:
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"
                    app.calenderBtnColorUpdate()
            OneLineListItem:
                text: "Calender"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                    app.calenderBtnColorUpdate()
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDNavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            Screen:
                name: "scr 1"
                MDLabel:
                    text: "hola"
                    halign: "center"
            Screen:
                name: "scr data"
                MDLabel:
                    text: "como eres?"
                    halign: "center"
            Screen:
                name: "scr 2"
                MDFloatingActionButton:
                    on_press:
                        screen_manager.current = "scr data"
                    pos_hint:{"center_x":.8,"center_y":.8}
                GridLayout:
                    pos_hint: {'center_x':.5,'center_y':.5}
                    size_hint: (None, None)
                    size: self.minimum_size
                    top: self.height
                    cols: 7
                    spacing: 10, 10
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class App(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        self.screen.children[0].children[1].current = "scr 2"
        self.screen.children[0].children[1].current = "scr 1"
        self.backend = Backend()
        self.max = 16
        self.data = self.backend.getData()
        self.init()
        return self.screen
    def init(self):
        self.calenderArray = []
        self.days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
        self.dataTypes = ["Category","Month", "Day", "RepeatMonth", "Time"]
        firstDay = 1 + calendar.monthrange(2022,1)[0]
        a = 0
        for i in range (1,calendar.monthrange(2022,1)[1]+ 1 + firstDay):            
            button = MDRaisedButton()
            if(i > firstDay):
                a += 1
                button.on_press = self.calenderBtnFunc
                button.text = str(a)
                button
                self.calenderArray.append(button)
            else:
                button.md_bg_color=[1,1,1,1]
                button.elevation = 0
            self.screen.children[0].children[1].children[1].children[0].add_widget(button)
    def calenderBtnColorUpdate(self):
        counter = 0
        for i in self.calenderArray:
            lol = self.data.getDataFiltered(counter, "Day", "Time")
            if not len(lol) == 0:
                i.md_bg_color = [helper.colorCurve(lol[0]), helper.colorCurveMain(lol[0]), helper.colorCurve(lol[0]), 1]
            else:
                i.md_bg_color = [.8,.8,.8,1]
            counter +=1
    def calenderBtnFunc(self):
        print(self)

class helper:
    @staticmethod
    def max(array):
        max = array[0]
        for i in array:
            if i > max:
                max = i
        return i

    @staticmethod
    def colorCurveMain(input):
        return .137 * (input ** .5)
    
    @staticmethod
    def colorCurve(input):
        return .05 * (input ** .5)

    @staticmethod
    def getMonth():
        return datetime.datetime.now().month

    @staticmethod
    def getDayArray():
        lol = calendar.Calendar()
        array = []
        #for i in lol.iterweekdays():
        for i in range(1,calendar.monthrange(2022,1)[1]+1):
            print(calendar.weekday(2022,1,i))

#helper.getDayArray()
App().run()
