import kivy
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton
import random
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager

kivy.require("1.10.1")
screen_helper = """
<ScrollableLabel>:
  Label:
    size_hint_y: None
    height: self.texture_size[1]
    text_size: self.width, None
    text: root.text
    font_size: '40sp'

<QuizSelect>:
  FloatLayout:
    MDScrollView:
      pos_hint:{"center_x":0.5,"top":0.8}
      do_scroll_x: False
      do_scroll_y: True
      scroll_y: 1
      MDList:
        OneLineAvatarIconListItem:
          text: "Quiz 1"
          on_release: 
            root.screen_manager.current = "q1"
          IconLeftWidget: 
            icon: "alphabetical"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "q2"
          text: "Quiz 2"
          IconLeftWidget:
            icon: "account-hard-hat"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "q3"
          text: "Quiz 3"
          IconLeftWidget:
            icon: "brain"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "q4"
          text: "Quiz 4"
          IconLeftWidget:
            icon: "arrow-down"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "q5"
          text: "Quiz 5"
          IconLeftWidget:
            icon: "hammer"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "q6"
          text: "Quiz 6"
          IconLeftWidget:
            icon: "hammer"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "q7"
          text: "Quiz 7"
          IconLeftWidget:
            icon: "cat"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "q8"
          text: "Quiz 8"
          IconLeftWidget:
            icon: "brush"



<LevelSelect>:
  FloatLayout:
    MDScrollView:
      pos_hint:{"center_x":0.5,"top":0.8}
      do_scroll_x: False
      do_scroll_y: True
      scroll_y: 1
      MDList:
        OneLineAvatarIconListItem:
          text: "Pronunciation"
          on_release: root.screen_manager.current = "lvl1"
          IconLeftWidget: 
            icon: "alphabetical"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl2"
          text: "Starting Sentences"
          IconLeftWidget:
            icon: "account-hard-hat"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl3"
          text: "Adding More"
          IconLeftWidget:
            icon: "brain"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl4"
          text: "Using 'ni'"
          IconLeftWidget:
            icon: "arrow-down"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl5"
          text: "Some Stuff"
          IconLeftWidget:
            icon: "hammer"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl6"
          text: "Prepositions 1"
          IconLeftWidget:
            icon: "hammer"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl7"
          text: "Prepositions + Animals"
          IconLeftWidget:
            icon: "cat"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl8"
          text: "Colors, Questions and more"
          IconLeftWidget:
            icon: "brush"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl9"
          text: "la + pi"
          IconLeftWidget:
            icon: "brush"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl10"
          text: "Time and numbers"
          IconLeftWidget:
            icon: "brush"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl11"
          text: "Time and numbers"
          IconLeftWidget:
            icon: "brush"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl12"
          text: "Extra words"
          IconLeftWidget:
            icon: "dog"
        OneLineAvatarIconListItem:
          text: ""
        OneLineAvatarIconListItem:
          text: ""
        OneLineAvatarIconListItem:
          text: ""
        OneLineAvatarIconListItem:
          text: ""
        OneLineAvatarIconListItem:
          text: ""
        OneLineAvatarIconListItem:  
          text: ""

<StorySelect>:
  FloatLayout:
    MDScrollView:
      pos_hint:{"center_x":0.5,"top":0.8}
      do_scroll_x: False
      do_scroll_y: True
      scroll_y: 1
      MDList:
        OneLineAvatarIconListItem:
          text: "First Meetings"
          on_release: 
            root.screen_manager.current = "story1"
          IconLeftWidget: 
            icon: "alphabetical"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "story2"
          text: "How to Order"
          IconLeftWidget:
            icon: "account-hard-hat"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "story3"
          text: "A Wild Animal"
          IconLeftWidget:
            icon: "brain"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "story4"
          text: "A New Pet"
          IconLeftWidget:
            icon: "arrow-down"
        OneLineAvatarIconListItem:
          on_release: root.screen_manager.current = "lvl5"
          text: "How Have You Been?"
          IconLeftWidget:
            icon: "hammer"





<MenuButton>:
  text: "Go to Menu"
  on_press: root.screen_manager.current = "levels"


<ContentNavigationDrawer>:
  ScrollView:
    MDList:
      OneLineListItem:
        text: "Levels"
        on_press:
          root.nav_drawer.set_state("close")
          root.screen_manager.current = "levels"

      OneLineListItem:
        text: "Quiz"
        on_press:
          root.nav_drawer.set_state("close")
          root.screen_manager.current = "quiz"

      OneLineListItem:
        text: "Stories"
        on_press:
          root.nav_drawer.set_state("close")
          root.screen_manager.current = "story"


<OriginalScreen>:
  MDTopAppBar:
    id: toolbar
    pos_hint: {"top": 1}
    title: 'Toki Pona'
    left_action_items: [["menu",lambda x: nav_drawer.set_state('open')]]

  MDNavigationLayout:
    x: toolbar.height

    ScreenManager:
      id: screen_manager
      Screen: 
        name: "levels"
        LevelSelect:
          screen_manager: screen_manager


      Screen: 
        name: "quiz"
        QuizSelect:
          screen_manager: screen_manager


      Screen: 
        name: "story"
        StorySelect:
          screen_manager: screen_manager

      Screen:
        screen_manager: screen_manager
        name: "story1"
        id: story1
        MDFillRoundFlatButton:
          text: "Start Story!"
          on_press: 
            root.s1time()
            root.butspress()
            screen_manager.current = "storyactual"

      Screen:
        screen_manager: screen_manager
        name: "story2"
        id: story2
        MDFillRoundFlatButton:
          text: "Start Story!"
          on_press: 
            root.s2time()
            root.butspress()
            screen_manager.current = "storyactual"

      Screen:
        screen_manager: screen_manager
        name: "story3"
        id: story3
        MDFillRoundFlatButton:
          text: "Start Story!"
          on_press: 
            root.s3time()
            root.butspress()
            screen_manager.current = "storyactual"

      Screen:
        screen_manager: screen_manager
        name: "storyactual"
        id: storyactual
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              id: storytexter
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: ""
              font_size: "18sp"
              color: 0.41,0.75,1,1
          MDFillRoundFlatButton:
            pos_hint:{"center_x":0.8,"top":0.8}
            text: "Next!"
            on_press: root.butspress()
          MDFillRoundFlatButton:
            pos_hint:{"center_x":0.8,"top":0.7}
            text: "Switch Languages"
            on_press: root.switchmodes()



      Screen:
        screen_manager: screen_manager
        name: "q1"
        id: q1
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q1time()
            screen_manager.current = "ques1"
            root.addno()
      Screen:
        screen_manager: screen_manager
        name: "q2"
        id: q2
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q2time()
            screen_manager.current = "ques1"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "q3"
        id: q3
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q3time()
            screen_manager.current = "ques1"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "q4"
        id: q4
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q4time()
            screen_manager.current = "ques1"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "q5"
        id: q5
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q5time()
            screen_manager.current = "ques1"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "q6"
        id: q6
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q6time()
            screen_manager.current = "ques1"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "q7"
        id: q7
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q7time()
            screen_manager.current = "ques1"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "q8"
        id: q8
        MDFillRoundFlatButton:
          text: "Start Quiz!"
          on_press: 
            root.q8time()
            screen_manager.current = "ques1"
            root.addno()


      Screen:
        screen_manager: screen_manager
        name: "ques1"
        id: ques1
        Label:
          id: q1q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field1
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques2"
            root.addno()


      Screen:
        screen_manager: screen_manager
        name: "ques2"
        id: ques2
        Label:
          id: q2q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field2
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques3"
            root.addno()
      Screen:
        screen_manager: screen_manager
        name: "ques3"
        id: ques3
        Label:
          id: q3q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field3
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques4"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "ques4"
        id: ques4
        Label:
          id: q4q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field4
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques5"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "ques5"
        id: ques5
        Label:
          id: q5q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field5
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques6"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "ques6"
        id: ques6
        Label:
          id: q6q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field6
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques7"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "ques7"
        id: ques7
        Label:
          id: q7q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field7
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques8"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "ques8"
        id: ques8
        Label:
          id: q8q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field8
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques8"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "ques8"
        id: ques8
        Label:
          id: q8q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field8
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques9"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "ques9"
        id: ques9
        Label:
          id: q9q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field9
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques10"
            root.addno()


      Screen:
        screen_manager: screen_manager
        name: "ques10"
        id: ques10
        Label:
          id: q10q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field10
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "ques11"
            root.addno()


      Screen:
        screen_manager: screen_manager
        name: "ques11"
        id: ques11
        Label:
          id: q11q
          text: "eee"
          pos_hint:{"center_x":0.5,"center_y":0.75}
          font_size: "18sp"
          color: 0.41,0.75,1,1
        MDTextField:
          id: text_field11
          pos_hint:{"center_y":0.5}
          hint_text: "Enter word"
          helper_text: "What is the Toki Pona translation?"
          helper_text_mode: "on_focus"
          mode: "rectangle"
        MDRectangleFlatButton:
          on_release: root.check_ans1(self)
          text: "Check answer!"
          pos_hint:{"center_x":0.5, "center_y":0.25}
        MDFillRoundFlatButton:
          text: "Next Question"
          pos_hint:{"center_x":0.5, "center_y":0.1}
          on_press: 
            screen_manager.current = "quiz"
            root.addno()

      Screen:
        screen_manager: screen_manager
        name: "lvl12"
        id: lvl12
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]\\nnamako - extra, additional, spice\\nkin - also, too\\noko - eye\\nkipisi - cut, divide\\nleko - square, block\\nmonsuta - monster, scary\\nmisikeke - medicine, cure\\ntonsi - non-binary, gender-nonconforming\\njasima - mirror, reflect, opposite\\nsoko - mushroom, fungus\\nmeso - average, middle\\nepiku - epic, amazing\\nkokosila - to speak something other than toki pona while in a toki pona group\\nlanpan - take, seize, steal\\nn - hmm..., uh, um\\nkijetesantakalu - raccoon, musteloid\\n\\n[b]Extra Words[/b]\\n\\nThese are the main words you should know if you want to dig deeper into toki pona. These are known as 'nimi ku suli'. Many of these words are synonyms for old words, such as 'oko' and 'lukin'. If you want to know more uncommon words, go to linku.la. It's a very useful dictionary that helped me create this app.\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1

      Screen:
        screen_manager: screen_manager
        name: "lvl11"
        id: lvl11
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]\\nsijelo - body, torso\\nalasa - hunt, search\\npilin - feeling, touch, heart\\nuta - mouth, lips\\ntaso - but, however, only\\nweka - absent, remote, away\\npu - 'Toki Pona: The Language of Good', interacting with it\\nsinpin - face, front, wall\\nlupa - door, window, hole\\nunpa - sexual relations\\nku - interacting with 'Toki Pona Dictionary'\\n\\n[b]Comparative Sentences[/b]\\n\\nIn toki pona, you combine two sentences for comparative sentences. For example: \\n\\nmi pona mute. sina pona. - I am better than you\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1

      Screen:
        screen_manager: screen_manager
        name: "lvl10"
        id: lvl10
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]\\ntenpo - time, moment  \\npini - finish, end, close  \\nken - may, can  \\nwan - one, part, united  \\ntu - two, divide  \\nsike - circle, round, ball\\nesun - market, shop, trade  \\nmun - moon, star, celestial object  \\nsuno - light, brightness, shine  \\nnanpa - number\\nopen - start, begin, open  \\n\\n[b]Time[/b]\\n\\nThe word 'tenpo' is used when combined with 'la' to describe what time something occurred. 'tenpo pini' is used for things in the past and 'tenpo kama' is used for things in the future. 'tenpo ni' is used for things in the present.\\n\\ntenpo ni la mi moku e pan - Now, I am eating bread.\\ntenpo pini la jan li pali. - A person worked.  \\ntenpo kama la ona li moli - He will die in the future.\\n\\nUsing 'tenpo' with 'mun', 'suno', and 'sike' create some periods of time.  \\n\\ntenpo suno - daytime\\ntenpo pimeja - night\\ntenpo mun/tenpo sike mun - month\\ntenpo sike/tenpo suno sike - year\\n\\n[b]Some Pre-Verbs[/b]\\n\\nWhen the word 'kama' is used as a pre-verb, it means that something is current.\\n\\nmi kama jo e moku. - I am getting food.\\n\\nAs a pre-verb, 'ken' is basically 'can'.\\n\\nmi ken pali e tomo. - I can build a house.\\n\\n'open' and 'pini' mean 'to start [verb]' and 'to finish [verb]' respectively.\\n\\nmi open lukin e lipu - I am starting to read a book\\nmi pini lukin e lipu - I finished reading a book  \\n\\n[b]Numbers[/b]\\n\\nHere is the list of toki pona numbers.  \\n\\nala - 0\\nwan - one\\ntu - two\\nmute - 3+\\n\\nAlternatively:\\n\\nluka (hand) - 5\\nmute (many) - 20\\nale (all) - 100\\n\\nIn toki pona, you add up numbers to make other numbers. \\n\\n42 - mute mute tu (20 + 20 + 2)  \\n\\nWith ordinal numbers, you have to use 'nanpa'.  \\n\\njan nanpa wan - the first person\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1

      Screen:
        screen_manager: screen_manager
        name: "lvl9"
        id: lvl9
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]\\nla - if/when, conditional  \\npi - of, regroups words\\nluka - hand, arm\\nnoka - foot, leg, to kick\\nnena - hill, protrusion, nose\\nlinja - string, hair, long and flexible item\\npalisa - stick, branch, long and solid item\\nwawa - strong, energy, powerful\\nsona - to know, intelligence, to be skilled in\\nmusi - fun, art, music, game\\nlipu - document, paper, card, book\\n\\n[b]la[/b]\\n\\nla is similar to 'if' in English. It allows the forming of two sentences to create conditions and context. The sentence structure of la is [sentence 1] la [sentence 2], with the meaning of In case of [sentence 1], [sentence 2.] Here are a few examples.\\n\\nmi lape la ale li pona - When I sleep, everything is good.\\nmi kama sona la, mi sona mute - If I learn, I'll be smart.\\n\\n[b]pi[/b]\\n\\nHere comes the most confusing word in toki pona. 'pi' is used to regroup adjectives. For example, if you wanted to say weak people, you might say [b]'jan wawa ala'[/b], but that would mean 'no strong people'. To regroup the words to make the meaning 'weak people', you use pi.\\n\\njan pi wawa ala - weak person (person of no strength)\\n\\nHere are a few more examples.\\n\\ntomo telo nasa - crazy bathroom\\ntomo pi telo nasa - bar\\n\\njan toki utala - a speaker warrior\\njan pi toki utala - a critic\\n\\nIf you want to use possessives with a proper noun, use pi.\\n\\ntomo pi jan Susan - Susan's house\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1

      Screen:
        screen_manager: screen_manager
        name: "lvl8"
        id: lvl8
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]\\nsama - same as, similar, like\\ntan - reason, cause, because\\nseme - signifies questions  \\no - particle for ccommands, adressing people  \\na - interjection, !\\nkule - color, colorful \\npimeja - black, dark\\njelo - yellow\\nlaso - blue, green\\nloje - red  \\nwalo - white, bright  \\n\\n[b]Even MORE prepositions[/b]\\n\\nsama has multiple meanings. Let's give a few examples:\\n\\njan ni li sama mi - That person is like me.  \\nsina lukin sama ona - You look like him.\\nsama li pona - Equality is good.  \\njan ni li jan sama mi - This person is my sibling (jan sama = sibling)\\n\\ntan means from by itself, but when combined with 'ni':, it can be used as 'because'.  \\n\\nmi pana e telo lukin tan ni: mi ike - I am crying because I am sad. (pana e telo lukin = cry)\\n\\n[b]Questions, Interjections, Commands[/b]\\n\\n[b]seme[/b]\\n\\nIn toki pona, you create questions using 'seme'. Unlike english, you put 'seme' in the place of where the answer to your question would be, similar to Chinese. For example, the question 'sina lukin e seme?' means 'What are you looking at?'. In toki pona, the question is formulated as 'You are looking at what?' with 'what' replacing the object. Let's give a few more examples.\\n\\nsina lon seme - Where are you? (lit. you in what?)\\nseme li lon sewi mi? - What is above me?\\nona li jo e seme? - What does he have? (lit. he has what?)\\nona moku e kili seme? - Which fruit did you eat? (lit. you eat fruit what?)\\n\\n[b]o[/b]\\n\\nThe word 'o' is used to address individuals and provide orders. When used by itself at the start of a sentence, it transforms the remaining text into a command. When placed after a noun, it calls a person.\\n\\no kute e mi! - Listen to me!\\nsina o - You!\\n\\n[b]a[/b]a is an interjection that is very similar to an exclamation mark. It is an interjection that signifies emotion. It is used at the end of a sentence.\\n\\nsina ike a! - You are horrible!\\n\\n[b]Yes or No Questions[/b]\\n\\nIf you want to use a yes or no question, you use this phrase structure: [word] ala [word]. For example:\\n\\nsina pona ala pona? - Are you okay? (lit you good not good?)\\n\\nIf you want to respond with 'yes', repeat the given word. If you use 'no', repeat the given word with 'ala.'\\n\\npona - Yes.\\npona ala - No.\\n\\n[b]Unofficial Words[/b]\\n\\nIf you want to use proper nouns in toki pona, you need to make an unofficial word. You take your word, change it so that it is viable to toki pona's pronunciation rules, and put it next to a noun so that the unofficial word is an adjective to the noun. Examples:\\n\\njan Misali - Mitch\\nma Palata - India (Bharat)\\ntoki Inli - The English Language\\n\\n[b]Colors[/b]\\n\\nIn toki pona, there are 5 basic colors. You can combine these colors with colors and other things to create extra colors!\\n\\njelo loje - orange\\nlaso loje - purple\\nlaso sewi - sky blue\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1
      Screen:
        screen_manager: screen_manager
        name: "lvl7"
        id: lvl7
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]  \\nsewi - high, above, top, sky  \\ninsa - inside, stomach  \\nanpa - ground, low, deep, to defeat  \\nmonsi - back, behind  \\npoka - near, nearby, side  \\nakesi - reptile, amphibian, not cute creature  \\nmu - animal onomatopoeia  \\nkala - sea creature, fish  \\nsoweli - animal  \\nwaso - bird  \\n\\n[b]More Prepositions...[/b] \\nsewi, insa, anpa, monsi and poka by themselves are used as nouns. However, when paired with other verbs like tawa and lon, they can be used as prepositions.  \\n\\nsina lon sewi mi - You are above me (lit. you are in my above)  \\nona li lon anpa mi - He is under me.  \\nmoku li lon insa mi - Food is inside me.  \\npipi moku lon poka ona - The bug is eating beside him.  \\n\\n[b]Animals[/b] \\n\\nLet's start with soweli. soweli means animal and usually refers to mammals and land animals. \\nkala is used as fish or any marine animal.  \\nThe original meaning of akesi was an animal that wasn't cute, but has also came to mean reptiles or amphibians.  \\nmu can refer to any animal noise, whether it be 'meow', 'woof' or 'oink'.  \\n\\nThere is a word that is well known in the toki pona community that refers to a certain type of animal... let's talk about it later.  \\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1

      Screen:
        screen_manager: screen_manager
        name: "lvl6"
        id: lvl6
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]  \\nlon - to be, at, in, on, exist  \\nkepeken - to use, using, with  \\ntawa - to go, to move, to, for  \\nkama - come  \\npoki - box, container, bowl etc.  \\nkon - air, wind, spirit  \\nsewi - high, sky  \\njaki - disgusting, yucky, nasty  \\nlen - clothing, cloth  \\nnasa - crazy, silly, weird  \\npakala - destroy, mess up, an expletive similar to damn  \\n\\n[b]lon[/b]\\n\\nlon can be used as both a verb (to be, to exist) and a preposition (in, at, on). For example:  \\n\\nmi lon poki - I am in the box.  \\nmi moku lon tomo - I am eating inside the house.  \\n\\n[b]kepeken[/b]  \\n\\nSimilar to lon, kepeken can be used as a verb (to use) and a preposition (using).  \\n\\nmi kepeken e ilo = I'm using tools.  \\nmi moku kepeken ilo moku. = I eat using a fork.\\n\\n[b]tawa[/b]  \\n\\nIf you are using tawa to say 'I am going', do not use [b]e[/b].  \\n\\sina tawa tomo mi - You are going to my house.  \\n\\nHowever, if you are using tawa to say 'I am moving (something)', then use [b]e[/b].  \\n\\nmi tawa e len mi - I moved my clothes.  \\n\\ntawa is also a preposition, meaning 'to'.  \\n\\nona li kama tawa tomo mi - He is coming to my house.\\n\\nThe word 'to like' in toki pona is translated by using tawa.  \\n\\nkili li pona tawa mi - I like fruit (lit. fruit is good to me)\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n" 
              font_size: "18sp"
              color: 0.41,0.75,1,1


      Screen:
        screen_manager: screen_manager
        name: "lvl5"
        id: lvl5
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]  \\njo - have  \\nsitelen - symbol, sign, image, to draw  \\nkiwen - rock, hard object, metal  \\nkasi - plant, grass, leaf \\npali - to work, to build, create  \\npan - bread, grain, cereal \\nko - clay, semi-solid material, powder  \\nolin - love, like, compassion  \\nmama - parent, ancestor, creator  \\nala - not, no  \\nale/ali - all, everything  \\n\\n[b]ale or ali?[/b]  \\n\\n[b]ali[/b] was the original word for 'all', but the pronunciation was similar to [b]'ala'[/b], so [b]ale[/b] was created as a replacement for ali. Both words are used but [b]ale[/b] is more common.\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n" 
              font_size: "18sp"
              color: 0.41,0.75,1,1


      Screen:
        screen_manager: screen_manager
        name: "lvl4"
        id: lvl4
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]  \\nni - this, that  \\nlape - sleep, rest  \\nmute - a lot, very, much, many  \\nseli - heat, fire, warmth  \\nkalama - noise, sound  \\nkute - ear, sound, hear  \\nlawa - lead, head, main  \\nlete - cold, coldness  \\nma - land, country, earth  \\nmani - money, wealth, currency  \\nmoli - death, die, kill  \\n\\n[b]Plural[/b]\\n\\nYou can pluralize words in Toki Pona using 'mute'.\\n\\njan lawa mute - many leaders\\nmi mute - we\\n\\n[b]'ni'[/b]\\n\\n'ni' can mean this or that.\\n\\nma ni li pona - this country is good.  \\n\\n'ni' can also be used to talk about what others say, or provide a more detailed description of something using the phrase 'e ni:'.  \\n\\njan lili toki e ni: sina ike - The child said you're bad.  \\njan utala toki e ni: ona li suli - The soldier said they were important.\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1


      Screen:
        screen_manager: screen_manager
        name: "lvl3"
        id: lvl3
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]  \\ne - object marker  \\nmeli - woman, female  \\nmije - man, male  \\ntomo - house  \\nijo - thing  \\nilo - tool, machine  \\nlukin - look, see, eye \\npana - to give, to emit  \\nkili - fruit, vegetable  \\nwile - want, need, must  \\nutala - fight, war\\n\\n[b]Specifying the object[/b]  \\nWhen you want to specify the object in a sentence, use 'e'. For example,  \\nmi moku [b]e[/b] kili - I am eating a fruit \\n\\n For the verb 'wile', you put 'e' after the infinitive. \\n\\nmi wile lukin [b]e[/b] tomo - I want to see the house. \\n\\n[b]Adjectives[/b]\\n\\nIn Toki Pona, you put the adjectives after the noun. For example, \\n\\nilo suli - big tool\\nijo pona - good thing\\n\\nPronouns also work as adjectives.\\n\\nmije mi - my husband\\nmeli sina - your wife\\n\\nYou can use multiple adjectives at a time. \\n\\njan utala ike - bad soldier (jan utala - soldier, knight etc.)\\n\\nSome compound words have specific meanings and have turned into phrases.\\n\\njan pona - friend  \\n\\n[b]Adverbs[/b]\\n\\nAdverbs are used the same way adjectives would be used.  \\n\\nmi lukin lili e ona - I barely saw it.\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1

      Screen:
        screen_manager: screen_manager
        name: "lvl2"
        id: lvl2
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "[b]Vocabulary[/b]  \\nmi - I, me  \\nsina - you  \\nona - he, she, they  \\npona - good, simple, to fix  \\nmoku - food, eat  \\nsuli - big, tall, important  \\nlili - small, unimportant, short  \\njan - person, human  \\ntelo - drink, water, liquid  \\nli - subject marker  \\ntoki - talk, speak, hello/hi\\n\\nWe will be learning about how to make basic sentences in Toki Pona. \\n\\nWords in Toki Pona have many different meanings. For example, 'suli' can mean big or important. That's how Toki Pona keeps the word count low. It may seem confusing and vague at first, but once you try it out and use these words more, you'll get used to it.  \\n\\n[b]To Be [/b]\\nToki Pona has no equivalent to the verb 'to be'. Let's take these examples. \\n\\nmi pona - I [b]am[/b] good. \\nsina lili - You [b]are[/b] small.  \\n\\nWhenever you use 'mi' or 'sina', you can just put the adjective or verb you want to use without having to use anything else. Simple! You may be wondering, don't some sentences have double meanings? This is true. The sentence 'mi moku' can mean 'I eat' or 'I am food'. You do not have to worry about this, as most times the meaning is shown through context.  \\n\\n[b]Using 'li'[/b]  \\nWhenever you have a sentence that doesnt use 'mi' or 'sina' as its subject, you use 'li'. For example,  \\n\\nmoku [b]li[/b] pona - Food [b]is[/b] good.  \\njan [b]li[/b] suli. - The person [b]is[/b] tall.  \\n\\nThere are no verb conjugations in Toki Pona. 'moku' can mean 'eating', 'will eat' or 'ate'. \\n\\nThere are no capitals in Toki Pona except when using proper nouns, every letter is lowercase.\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1

      Screen:
        screen_manager: screen_manager
        name: "lvl1"
        id: lvl1
        FloatLayout:
          cols: 1
          ScrollView:
            pos_hint:{"center_x":0.5,"top":0.8}
            do_scroll_x: False
            do_scroll_y: True
            scroll_y: 1
            Label:
              padding_x: 10
              markup: True
              size_hint_y: None
              height: self.texture_size[1]
              text_size: self.width, None
              text: "This is the first lesson of this app! Today we will we be learning about pronunciation. Toki Pona has just 14 letters! Below is a table on how to pronounce the letters. The letters in bold are how to pronounce the given letter.  \\n\\n[b]a[/b] - f[b]a[/b]ther\\n[b]e[/b] - m[b]e[/b]t\\n[b]i[/b] - st[b]ea[/b]l\\n[b]o[/b] - p[b]o[/b]le\\n[b]u[/b] - r[b]oo[/b]t\\n\\n[b]k[/b] - [b]k[/b]ra[b]k[/b]en\\n[b]m[/b] - [b]m[/b]an\\n[b]p[/b] - [b]p[/b]ress\\n[b]l[/b] - [b]l[/b]ess  \\n[b]n[/b] - [b]n[/b]est\\n[b]s[/b] - [b]s[/b]ore\\n[b]t[/b] - [b]t[/b]ree\\n[b]w[/b] - [b]w[/b]ater\\n[b]j[/b] - [b]y[/b]ellow\\n\\n\\n\\n\\n\\n\\n\\n\\n"
              font_size: "18sp"
              color: 0.41,0.75,1,1















    MDNavigationDrawer:
      id: nav_drawer

      ContentNavigationDrawer:
        screen_manager: screen_manager
        nav_drawer: nav_drawer



OriginalScreen:        

"""


class MenuButton(MDFillRoundFlatButton):
    screen_manager = ObjectProperty()


class OriginalScreen(Screen):
    screen_manager = ObjectProperty()

    sm = ScreenManager()

    q11list = [
        "I, me", "eat, food", "drink, liquid, water, wash", "you",
        "he, she, they", "person, human", "good, simple, to fix",
        "big, important, tall", "short, unimportant, small", "subject marker",
        "talk"
    ]
    a11list = [
        "mi", "moku", "telo", "sina", "ona", "jan", "pona", "suli", "lili",
        "li", "toki"
    ]
    q22list = [
        "object marker", "woman, female", "man, male", "house", "thing",
        "tool, machine", "look, see, eye", "to give, to emit",
        "fruit, vegetable", "want, need, must", "fight, war"
    ]
    a22list = [
        "e", "meli", "mije", "tomo", "ijo", "ilo", "lukin", "pana", "kili",
        "wile", "utala"
    ]

    q33list = [
        "this, that", "sleep, rest", "a lot, very, much, many", "heat, fire, warmth", "noise, sound",
        "ear, sound, hear", "lead, head, main", "cold, coldness",
        "land, country, earth", "money, wealth, currency", "death, die, kill"
    ]
    a33list = [
        "ni", "lape", "mute", "seli", "kalama", "kute", "lawa", "lete", "ma",
        "mani", "moli"
    ]
    q44list = ["have", "symbol, sign, image, to draw", "rock, hard object, metal", "plant, grass, leaf",
               "to work, to build, create", "bread, grain, cereal", "clay, semi-solid", "love, like, compassion",
               "parent, ancestor, creator", "not, no", "all, everything"]
    a44list = ["jo", "sitelen", "kiwen", "kasi", "pali", "pan", "ko", "olin", "mama", "ala", "ale/ali"]
    q55list = ["to be, at, in, on, exist", "to use, using, with", "to go, to move, to, for", "come",
               "box, container, bowl etc.", "air, wind, spirit", "high, sky", "disgusting, yucky", "clothing, cloth",
               "crazy, silly, weird", "destroy, mess up, generic expletive"]
    a55list = ["lon", "kepeken", "tawa", "kama", "poki", "kon", "sewi", "jaki", "len", "nasa", "pakala"]
    q66list = ["high, above, top, sky", "inside, stomach", "ground, low, deep, to defeat", "back, behind",
               "near, nearby, side", "reptiel, amphibian, not cute creature", "animal onomatopoeia",
               "sea creature, fish", "animal", "bird"]
    a66list = ["sewi", "insa", "anpa", "monsi", "poka", "akesi", "mu", "kala", "soweli", "waso"]
    q77list = ["same as, similar, like", "reason, cause, because", "signifies questions",
               "particle for commands, adressing people", "interjection, !", "color, colorful", "black, dark", "yellow",
               "blue, green", "red", "white, bright"]
    a77list = ["sama", "tan", "seme", "o", "a", "kule", "pimeja", "jelo", "laso", "loje", "walo"]
    q88list = ["if/when, conditional", "of, regroups words", "hand, arm", "foot, leg, to kick",
               "hill, protrusion, nose", "string, hair, long and flexible item", "stick, branch",
               "strong, energy, powerful", "know, intelligence, to be skilled in", "fun, art, music, game",
               "document, paper, card, book"]
    a88list = ["la", "pi", "luka", "noka", "nena", "linja", "palisa", "wawa", "sona", "musi", "lipu"]

    whatnoquiz = 0
    noofq = 0
    chooser = ""
    row = ""
    eeddd = ""

    def addno(self):
        if self.whatnoquiz == 1:
            self.chooser = self.a11list[self.noofq]
        elif self.whatnoquiz == 2:
            self.chooser = self.a22list[self.noofq]
        elif self.whatnoquiz == 3:
            self.chooser = self.a33list[self.noofq]
        elif self.whatnoquiz == 4:
            self.chooser = self.a44list[self.noofq]
        elif self.whatnoquiz == 5:
            self.chooser = self.a55list[self.noofq]
        elif self.whatnoquiz == 6:
            self.chooser = self.a66list[self.noofq]
        elif self.whatnoquiz == 7:
            self.chooser = self.a77list[self.noofq]
        elif self.whatnoquiz == 8:
            self.chooser = self.a88list[self.noofq]
        self.noofq += 1
        self.eeddd = "text_field" + str(self.noofq)

    def q1time(self):
        self.ids.q1q.text = self.q11list[0]
        self.ids.q2q.text = self.q11list[1]
        self.ids.q3q.text = self.q11list[2]
        self.ids.q4q.text = self.q11list[3]
        self.ids.q5q.text = self.q11list[4]
        self.ids.q6q.text = self.q11list[5]
        self.ids.q7q.text = self.q11list[6]
        self.ids.q8q.text = self.q11list[7]
        self.ids.q9q.text = self.q11list[8]
        self.ids.q10q.text = self.q11list[9]
        self.ids.q11q.text = self.q11list[10]
        self.whatnoquiz = 1

    def q2time(self):
        self.ids.q1q.text = self.q22list[0]
        self.ids.q2q.text = self.q22list[1]
        self.ids.q3q.text = self.q22list[2]
        self.ids.q4q.text = self.q22list[3]
        self.ids.q5q.text = self.q22list[4]
        self.ids.q6q.text = self.q22list[5]
        self.ids.q7q.text = self.q22list[6]
        self.ids.q8q.text = self.q22list[7]
        self.ids.q9q.text = self.q22list[8]
        self.ids.q10q.text = self.q22list[9]
        self.ids.q11q.text = self.q22list[10]
        self.whatnoquiz = 2

    def q3time(self):
        self.ids.q1q.text = self.q33list[0]
        self.ids.q2q.text = self.q33list[1]
        self.ids.q3q.text = self.q33list[2]
        self.ids.q4q.text = self.q33list[3]
        self.ids.q5q.text = self.q33list[4]
        self.ids.q6q.text = self.q33list[5]
        self.ids.q7q.text = self.q33list[6]
        self.ids.q8q.text = self.q33list[7]
        self.ids.q9q.text = self.q33list[8]
        self.ids.q10q.text = self.q33list[9]
        self.ids.q11q.text = self.q33list[10]
        self.whatnoquiz = 3

    def q4time(self):
        self.ids.q1q.text = self.q44list[0]
        self.ids.q2q.text = self.q44list[1]
        self.ids.q3q.text = self.q44list[2]
        self.ids.q4q.text = self.q44list[3]
        self.ids.q5q.text = self.q44list[4]
        self.ids.q6q.text = self.q44list[5]
        self.ids.q7q.text = self.q44list[6]
        self.ids.q8q.text = self.q44list[7]
        self.ids.q9q.text = self.q44list[8]
        self.ids.q10q.text = self.q44list[9]
        self.ids.q11q.text = self.q44list[10]
        self.whatnoquiz = 4

    def q5time(self):
        self.ids.q1q.text = self.q55list[0]
        self.ids.q2q.text = self.q55list[1]
        self.ids.q3q.text = self.q55list[2]
        self.ids.q4q.text = self.q55list[3]
        self.ids.q5q.text = self.q55list[4]
        self.ids.q6q.text = self.q55list[5]
        self.ids.q7q.text = self.q55list[6]
        self.ids.q8q.text = self.q55list[7]
        self.ids.q9q.text = self.q55list[8]
        self.ids.q10q.text = self.q55list[9]
        self.ids.q11q.text = self.q55list[10]
        self.whatnoquiz = 5

    def q6time(self):
        self.ids.q1q.text = self.q66list[0]
        self.ids.q2q.text = self.q66list[1]
        self.ids.q3q.text = self.q66list[2]
        self.ids.q4q.text = self.q66list[3]
        self.ids.q5q.text = self.q66list[4]
        self.ids.q6q.text = self.q66list[5]
        self.ids.q7q.text = self.q66list[6]
        self.ids.q8q.text = self.q66list[7]
        self.ids.q9q.text = self.q66list[8]
        self.ids.q10q.text = self.q66list[9]

        self.whatnoquiz = 6

    def q7time(self):
        self.ids.q1q.text = self.q77list[0]
        self.ids.q2q.text = self.q77list[1]
        self.ids.q3q.text = self.q77list[2]
        self.ids.q4q.text = self.q77list[3]
        self.ids.q5q.text = self.q77list[4]
        self.ids.q6q.text = self.q77list[5]
        self.ids.q7q.text = self.q77list[6]
        self.ids.q8q.text = self.q77list[7]
        self.ids.q9q.text = self.q77list[8]
        self.ids.q10q.text = self.q77list[9]
        self.ids.q11q.text = self.q77list[10]
        self.whatnoquiz = 7

    def q8time(self):
        self.ids.q1q.text = self.q77list[0]
        self.ids.q2q.text = self.q77list[1]
        self.ids.q3q.text = self.q77list[2]
        self.ids.q4q.text = self.q77list[3]
        self.ids.q5q.text = self.q77list[4]
        self.ids.q6q.text = self.q77list[5]
        self.ids.q7q.text = self.q77list[6]
        self.ids.q8q.text = self.q77list[7]
        self.ids.q9q.text = self.q77list[8]
        self.ids.q10q.text = self.q77list[9]
        self.ids.q11q.text = self.q77list[10]
        self.whatnoquiz = 8

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def check_ans1(self, obj):
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        if self.ids[self.eeddd].text == "":
            self.row = 'Please enter an answer.'
        elif self.ids[self.eeddd].text == self.chooser:
            self.row = 'Correct!'
        else:
            self.row = 'Wrong!'

        self.dialog = MDDialog(title='Answer',
                               text=self.row,
                               size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.open()

    # storytime

    storytext = ""
    whatnostory = 0
    guy11 = [
        '[b]mi[/b]: toki! sina pilin seme?', '[b]mi[/b]: nimi sina li seme?',
        '[b]mi[/b]: sina tan ma seme?', '[b]mi[/b]: mi tawa!'
    ]
    guy21 = [
        '[b]sina[/b]: mi pilin pona!', '[b]sina[/b]: nimi mi li jan Lopin.',
        '[b]sina[/b]: mi kama tan ma Palata.', '[b]sina[/b]: tawa pona!'
    ]
    guyt11 = [
        '[b]Me[/b]: Hello! How are you?', '[b]Me[/b]: What is your name?',
        '[b]Me[/b]: Where are you from?',
        '[b]Me[/b]: Goodbye! (person leaving)'
    ]
    guyt21 = [
        '[b]You[/b]: I am good!', '[b]You[/b]: My name is Robin.',
        '[b]You[/b]: I come from India.', '[b]You[/b]: Goodbye! (other person)'
    ]
    guy12 = [
        '[b]mi[/b]: mi tawa tomo moku.',
        '[b]mi[/b]: mi tawa tomo moku tan ni: mi wile moku!'
    ]
    guy22 = ['[b]sina[/b]: sina tawa tomo moku tan seme?', '']
    guyt12 = [
        '[b]Me[/b]: I am going to the restaurant',
        '[b]Me[/b]: Because I am hungry!'
    ]
    guyt22 = ['[b]You[/b]: Why are you going to the restaurant?', '']

    guy13 = [
        'meli li toki e soweli.', '[b]mije[/b]: mi pilin e ni: soweli ni li lili.'
    ]
    guy23 = [
        '[b]meli[/b]: soweli ni li suli!', '[b]meli[/b]: soweli li suli. sina li lili!'
    ]

    guyt13 = [
        'A woman is talking about an animal.', '[b]The man[/b]: I think that this animal is small.'
    ]

    guyt23 = [
        '[b]The woman[/b]: This animal is big!', '[b]The woman[/b]: The animal is bigger than you.'
    ]

    storychooser1 = ""
    storychooser2 = ""
    storytranslation1 = ""
    storytranslation2 = ""
    translationtext = ""
    normaltext = ""
    noofs = 0
    normalmode = True
    consfinish = 0
    idrkw = ""
    idrkwas = ""

    def s1time(self):
        self.whatnostory = 1

    def s2time(self):
        self.whatnostory = 2

    def s3time(self):
        self.whatnostory = 3

    def switchmodes(self):
        if self.normalmode == True:
            print(self.idrkw)
            self.normalmode = False
            self.ids.storytexter.text = self.idrkw
        else:
            self.normalmode = True
            self.ids.storytexter.text = self.idrkwas

    def butspress(self):
        if self.consfinish % 2 == 0:
            if self.whatnostory == 1:
                self.storychooser1 = self.guy11[self.noofs]
                self.storychooser2 = self.guy21[self.noofs]
                self.storytranslation1 = self.guyt11[self.noofs]
                self.storytranslation2 = self.guyt21[self.noofs]
            elif self.whatnostory == 2:
                self.storychooser1 = self.guy12[self.noofs]
                self.storychooser2 = self.guy22[self.noofs]
                self.storytranslation1 = self.guyt12[self.noofs]
                self.storytranslation2 = self.guyt22[self.noofs]
            elif self.whatnostory == 3:
                self.storychooser1 = self.guy13[self.noofs]
                self.storychooser2 = self.guy23[self.noofs]
                self.storytranslation1 = self.guyt13[self.noofs]
                self.storytranslation2 = self.guyt23[self.noofs]
            self.noofs += 1
            print(self.storytranslation1 + "" + self.storytranslation2)

        if self.consfinish % 2 == 0:
            self.idrkwas = self.idrkwas + "\n\n" + self.storychooser1
            self.idrkw = self.idrkw + "\n\n" + self.storytranslation1
        elif self.consfinish % 2 == 1:
            self.idrkwas = self.idrkwas + "\n\n" + self.storychooser2
            self.idrkw = self.idrkw + "\n\n" + self.storytranslation2

        if self.consfinish % 2 == 0:
            if self.normalmode == True:
                self.ids.storytexter.text = self.idrkwas
            else:
                self.ids.storytexter.text = self.idrkw
        elif self.consfinish % 2 == 1:
            if self.normalmode == True:
                self.ids.storytexter.text = self.idrkwas
            else:
                self.ids.storytexter.text = self.idrkw

        self.consfinish += 1

        print(self.idrkw)


class ScrollabelLabel(ScrollView):
    pass


class LevelSelect(BoxLayout):
    screen_manager = ObjectProperty()

    def choosethis(self):
        pass


class QuizSelect(BoxLayout):
    screen_manager = ObjectProperty()

    def choosethis(self):
        pass


class StorySelect(BoxLayout):
    def choosethis(self):
        pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


Window.size = (500, 500)


class TokiPonaApp(MDApp):
    def build(self):
        return Builder.load_string(screen_helper)


TokiPonaApp().run()


