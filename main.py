import calendar
from datetime import date
from datetime import *
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
from kivymd.uix.picker import MDDatePicker
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
calendar.setfirstweekday(calendar.SUNDAY)
KV = '''
<IconListItem>

    IconLeftWidget:
        icon: root.icon
<ContentNavigationDrawer>:
    ScrollView:        
        MDList:
            MDFloatingActionButton:
            OneLineListItem:
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"
                    app.calendarBtnColorUpdate()
            OneLineListItem:
                text: "Calender"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                    app.calendarBtnColorUpdate()
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDNavigationLayout:
        id: layout
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            Screen:
                name: "scr 1"
                MDLabel:
                    text: "hola"
                    halign: "center"
            Screen:
                id: user_data_scr
                name: "scr data"
                MDDropDownItem:
                    id: dropItemCategory
                    pos_hint: {'center_x': .3, 'center_y': .46}
                    text: 'Item'
                    on_release: app.menuCategory.open()
                MDRaisedButton:
                    text: "hola soy yo"
                    pos_hint: {'center_x': .3, 'center_y': .6}
                    on_press:
                        app.userPush()
                MDRaisedButton:
                    text: "hola"
                    on_press:
                        app.showDatePicker()
                MDDropDownItem:
                    id: dropItemRepeat
                    pos_hint: {'center_x': .6, 'center_y': .46}
                    text: 'hehe'
                    on_release: app.menuRepeat.open()
                MDTextField:
                    id: Time
                    hint_text: "Time"
                    pos_hint: {"center_x": .6,"center_y": .4}
                    multiline: False
                    size_hint: .25, .04
                    mode: "rectangle"
                    on_text_validate: app.pullDataTime()
            Screen:
                id: calendar_scr
                name: "scr 2"
                MDFloatingActionButton:
                    on_press:
                        screen_manager.current = "scr data"
                    pos_hint:{"center_x":.8,"center_y":.8}
                GridLayout:
                    id: calendar_layout
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
class IconListItem(OneLineIconListItem):
    icon = StringProperty()
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class App(MDApp):
    def build(self):
        self.userDataTemp = {
                "Category": 0,
                "Month": 0,
                "Day" : 0,
                "RepeatType": 0,
                "Time": 0
                }
        self.screen = Builder.load_string(KV)
        self.screen.ids.screen_manager.current = "scr 2"
        self.screen.ids.screen_manager.current = "scr 1"
        self.backend = Backend()
        self.parser = self.backend.getParser()
        self.data = self.backend.getData()
        self.init()
        return self.screen
    def addCalendar(self):
        self.calenderArray = []
        self.days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
        self.dataTypes = ["Category","Month", "Day", "RepeatMonth", "Time"]
        firstDay = 1 + calendar.monthrange(2022,helper.getMonth())[0]
        print(firstDay)
        a = 0
        for i in range(1,calendar.monthrange(2022,helper.getMonth())[1]+1 + firstDay):            
            button = MDRaisedButton()
            if(i > firstDay):
                a += 1
                button.on_press = self.calenderBtnFunc
                button.text = str(a)
                button
                self.calenderArray.append(button)
                print(a)
            else:
                button.md_bg_color=[1,1,1,1]
                button.elevation = 0
            self.screen.ids.calendar_layout.add_widget(button)
        self.calendarBtnColorUpdate()
    def init(self):
        self.addCalendar()
        categories = ["Monthly", "Weekly", "Bi-Weekly", "Do Not Reapeat"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"{i}",
                "height": dp(56),
                "on_release": lambda x=f"{i}": self.set_itemRepeat(x),
            } for i in categories
        ]
        self.menuRepeat = MDDropdownMenu(
            caller=self.screen.ids.dropItemRepeat,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        categories = ["School", "Sports", "Extracurriculars"]
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "git",
                "text": f"{i}",
                "height": dp(56),
                "on_release": lambda x=f"{i}": self.set_itemCategory(x),
            } for i in categories
        ]
        self.menuCategory = MDDropdownMenu(
            caller=self.screen.ids.dropItemCategory,
             items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menuRepeat.bind()
        self.menuCategory.bind()
        self.calenderArray = []
    def calendarBtnColorUpdate(self):
        counter = 0
        for i in self.calenderArray:
            lol = self.data.getDataFiltered(counter, "Day", "Time")
            if not len(lol) == 0:
                i.md_bg_color = [helper.colorCurve(lol[0]), .1, .1, 1]
            else:
                i.md_bg_color = [.8,.8,.8,1]
            counter +=1
    def calenderBtnFunc(self):
        print(self)
    def on_save(self, instance, value, date_range):
        strDate = str(value)
        self.userDataTemp["Day"] = strDate[8] + strDate[9]
        self.userDataTemp["Month"] = strDate[5] + strDate[6]
    def on_cancel(self, instance, value):
        pass
    def showDatePicker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    def pullDataTime(self):
        self.userDataTemp["Time"] = (self.screen.ids.Time.text)
    def set_itemRepeat(self, text_item):
        self.screen.ids.dropItemRepeat.set_item(text_item)
        self.menuRepeat.dismiss()
        self.userDataTemp["RepeatType"] = text_item
        print(self.userDataTemp)
    def set_itemCategory(self, text_item):
        self.screen.ids.dropItemCategory.set_item(text_item)
        self.menuCategory.dismiss()
        self.userDataTemp["Category"] = text_item
        print(self.userDataTemp)
    def userPush(self):
        self.parser.addData(self.data.convertData(self.userDataTemp))
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
        return (.25 * (input ** .5))
    @staticmethod
    def getMonth():
        return datetime.now().month
    @staticmethod
    def getDayArray():
        lol = calendar.Calendar()
        array = []
        for i in range(1,calendar.monthrange(2022,helper.getMonth())[1]+1):
            print(calendar.weekday(2022,helper.getMonth(),i))
helper.getDayArray();
App().run()
