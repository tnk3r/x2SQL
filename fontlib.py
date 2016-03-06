#!/usr/bin/python


#Common fonts and Button styles I use

class fontlib():

    def __init__(self):
        self.base_font = "Helvetica"
        self.notify_text25 = "font-family: Helvetica; color: White; font-size: 25px; qproperty-alignment: AlignCenter;"
        self.system_font50_italic = "background: Black; " \
                                    "font-family: Helvetica; " \
                                    "color: Gray; " \
                                    "font-size: 50px; " \
                                    "qproperty-alignment: AlignCenter;" \
                                    "font-style: italic;"

        self.system_font30_italic = "background: Black; " \
                                    "font-family: Helvetica; " \
                                    "color: Gray; " \
                                    "font-size: 30px; " \
                                    "qproperty-alignment: AlignCenter;" \
                                    "font-style: italic;"
        self.system_font50 = "background: Black; " \
                             "font-family: Helvetica; " \
                             "color: White; " \
                             "font-size: 50px; " \
                             "border: 1px solid white; " \
                             "qproperty-alignment: AlignCenter;"
        self.system_font40 = "background: Black; font-family: Helvetica; color: White; font-size: 40px; border: 1px solid white;"
        self.system_font35_noborder = " font-family: Helvetica; color: White; font-size: 35px;"
        self.system_font30 = "font-family: Helvetica; color: White; font-size: 30px;"
        self.system_font25 = "font-family: Helvetica; color: White; font-size: 25px;"

        self.system_font20 = "font-family: Helvetica; color: White; font-size: 20px;"
        self.system_font15 = "font-family: Helvetica; color: White; font-size: 15px;"
        self.system_font12 = "font-family: Helvetica; color: White; font-size: 12px;"
        self.system_font35_noborder = " font-family: Helvetica; color: White; font-size: 35px;"
        self.system_font100_noborder = " font-family: Helvetica; color: White; font-size: 80px; qproperty-alignment: AlignCenter;"
        self.system_font60_noborder = " font-family: Helvetica; color: White; font-size: 60px; qproperty-alignment: AlignCenter;"

        self.label_box = "font-family: Helvetica; " \
                         "color: White; font-size: 80px; " \
                         "border: 4px solid white; " \
                         "border-radius: 10px;" \
                         "qproperty-alignment: AlignCenter;"
        self.label_box60 = "font-family: Helvetica; " \
                           "color: White; font-size: 60px; " \
                           "border: 4px solid white; " \
                           "border-radius: 10px;" \
                           "qproperty-alignment: AlignCenter;"


        self.button_font_wb_35 = "background: Black; " \
                                 "font-family: Helvetica; " \
                                 "color: White;" \
                                 " font-size: 35px; " \
                                 "border: 1px solid white; " \
                                 "qproperty-alignment: AlignCenter;"

        self.button_font_wb_40 = "background: Black; " \
                                 "font-family: Helvetica; " \
                                 "color: White;" \
                                 " font-size: 40px; " \
                                 "border: 2px solid white; " \
                                 "border-radius: 5px; " \
                                 "qproperty-alignment: AlignCenter;"

        self.button_font_wb_40_pressed = "background: Black; " \
                                         "font-family: Helvetica; " \
                                         "color: White;" \
                                         " font-size: 40px; " \
                                         "border: 2px solid yellow; " \
                                         "qproperty-alignment: AlignCenter;"

        self.cancel_font_wb_40 = "background: Black; " \
                                 "font-family: Helvetica; " \
                                 "color: White;" \
                                 "font-size: 30px; " \
                                 "border: 2px solid red; " \
                                 "border-radius: 5px;" \
                                 "font-style: italic;" \
                                 "qproperty-alignment: AlignCenter;"

        self.button_font_wb_40_highlighted = "background: Black; " \
                                             "font-family: Helvetica; " \
                                             "color: White;" \
                                             " font-size: 40px; " \
                                             "border: 5px solid white; " \
                                             "border-radius: 5px; " \
                                             "qproperty-alignment: AlignCenter;"

        self.button_font_wb_50 = "background: Black; " \
                                 "font-family: Helvetica; " \
                                 "color: White;" \
                                 " font-size: 50px; " \
                                 "border: 2px solid white; " \
                                 "border-radius: 5px;" \
                                 "qproperty-alignment: AlignCenter;"

        self.button_font_wb_50_highlighted_thin_border = "background: Black; " \
                                                         "font-family: Helvetica; " \
                                                         "color: White;" \
                                                         " font-size: 50px; " \
                                                         "border: 2px solid white; " \
                                                         "border-radius: 5px;" \
                                                         "qproperty-alignment: AlignCenter;"
        self.label_font_30 = "background: Black; " \
                             "font-family: Helvetica; " \
                             "color: White;" \
                             " font-size: 30px; " \
                             "border: 2px solid white; " \
                             "border-radius: 5px; " \
                             "qproperty-alignment: AlignCenter;"


        self.button_font_wb_25 = "background: Black; " \
                                 "font-family: Helvetica; " \
                                 "color: White;" \
                                 " font-size: 25px; " \
                                 "border: 1px solid white; " \
                                 "border-radius: 10px;" \
                                 "qproperty-alignment: AlignCenter;"

        self.button_round_40 = "background: Black; " \
                               "font-family: Helvetica; " \
                               "color: White;" \
                               " font-size: 40px; " \
                               "border: 1px solid white; " \
                               "border-radius: 10px;" \
                               "qproperty-alignment: AlignCenter;"


        self.ok_button_italic40 = "font-family: Helvetica; " \
                                  "color: White; " \
                                  "font-size: 40px; " \
                                  "qproperty-alignment: AlignCenter;" \
                                  "font-style: italic;" \
                                  "border: 2px solid white;" \
                                  "border-radius: 5px;"
        self.ok_button_italic40_yellow = "font-family: Helvetica; " \
                                         "color: White; " \
                                         "font-size: 40px; " \
                                         "qproperty-alignment: AlignCenter;" \
                                         "font-style: italic;" \
                                         "border: 2px solid yellow;" \
                                         "border-radius: 5px;"
        self.redB_colorwin = "background: Black; " \
                             "font-family: Helvetica; " \
                             "color: White;" \
                             " font-size: 30px; " \
                             "border: 1px solid red; " \
                             "border-radius: 5px; " \
                             "qproperty-alignment: AlignCenter;"
        self.blueB_colorwin = "background: Black; " \
                              "font-family: Helvetica; " \
                              "color: White;" \
                              " font-size: 30px; " \
                              "border: 2px solid blue; " \
                              "border-radius: 5px; " \
                              "qproperty-alignment: AlignCenter;"

        self.greenB_colorwin = "background: Black; " \
                               "font-family: Helvetica; " \
                               "color: White;" \
                               " font-size: 30px; " \
                               "border: 2px solid lime; " \
                               "border-radius: 5px; " \
                               "qproperty-alignment: AlignCenter;" \
 \
        self.red_cdl = "background: Black; " \
                       "font-family: Helvetica; " \
                       "color: White;" \
                       " font-size: 35px; " \
                       "border: 2px solid red; " \
                       "border-radius: 10px;" \
                       "qproperty-alignment: AlignCenter;"

        self.blue_cdl = "background: Black; " \
                        "font-family: Helvetica; " \
                        "color: White;" \
                        " font-size: 35px; " \
                        "border: 2px solid blue; " \
                        "border-radius: 10px;" \
                        "qproperty-alignment: AlignCenter;"

        self.green_cdl = "background: Black; " \
                         "font-family: Helvetica; " \
                         "color: White;" \
                         " font-size: 35px; " \
                         "border: 2px solid lime; " \
                         "border-radius: 10px;" \
                         "qproperty-alignment: AlignCenter;"

        self.set_button_font30 = "background: Black; " \
                                 "font-family: Helvetica; " \
                                 "color: White;" \
                                 " font-size: 30px; " \
                                 "border: 6px solid yellow;" \
                                 "border-radius: 16px;" \
                                 "qproperty-alignment: AlignCenter;"

        self.alert_text = "font-family: Helvetica; background: black; font-size: 30px;" \
                          "color: yellow; border: 5px solid yellow;"

        self.alert_ok = "background: Black; " \
                        "font-family: Helvetica; " \
                        "color: White;" \
                        " font-size: 40px; " \
                        "border: 6px solid red; " \
                        "border-radius: 16px;" \
                        "qproperty-alignment: AlignCenter;"

        self.small_label = "font-family: Helvetica; color: white; font-size: 15px;"

        self.italic40 = "font-family: Helvetica; " \
                        "color: White; " \
                        "font-size: 40px; " \
                        "qproperty-alignment: AlignCenter;" \
                        "font-style: italic;"

        self.italic30 = "font-family: Helvetica; " \
                        "color: White; " \
                        "font-size: 30px; " \
                        "qproperty-alignment: AlignCenter;" \
                        "font-style: italic;"

        self.italic20 = "font-family: Helvetica; " \
                        "color: White; " \
                        "font-size: 20px; " \
                        "font-style: italic;"

        self.gray_italic25 = "font-family: Helvetica; " \
                             "color: Gray; " \
                             "font-size: 25px; " \
                             "qproperty-alignment: AlignCenter;" \
                             "font-style: italic;"

        self.button_italic30 = "font-family: Helvetica; " \
                               "color: White; " \
                               "font-size: 30px; " \
                               "qproperty-alignment: AlignCenter;" \
                               "font-style: italic;" \
                               "border: 2px solid white;" \
                               "border-radius: 5px"

        self.status_italic30 = "font-family: Helvetica; " \
                               "color: White; " \
                               "font-size: 30px; " \
                               "font-style: italic;" \
                               "border: 2px solid white;" \
                               "border-radius: 5px"

        self.button_italic30_highlighted = "font-family: Helvetica; " \
                                           "color: White; " \
                                           "font-size: 30px; " \
                                           "qproperty-alignment: AlignCenter;" \
                                           "font-style: italic;" \
                                           "border: 5px solid white;" \
                                           "border-radius: 5px"

        self.button_italic30_yellow = "font-family: Helvetica; " \
                                      "color: White; " \
                                      "font-size: 30px; " \
                                      "qproperty-alignment: AlignCenter;" \
                                      "font-style: italic;" \
                                      "border: 5px solid yellow;" \
                                      "border-radius: 5px"

        self.italic40_red = "font-family: Helvetica; " \
                            "color: Red; " \
                            "font-size: 40px; " \
                            "qproperty-alignment: AlignCenter;" \
                            "font-style: italic;"

