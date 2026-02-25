# ///////////////////////////////////////////////////////////////
import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from PySide6.QtCore import Qt, QEvent
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Genius FAE"
        description = "Genius FAE"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget_msg.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.tableWidget_analyzer.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_hwcheck.clicked.connect(self.buttonClick)
        widgets.btn_uart.clicked.connect(self.buttonClick)
        widgets.btn_i2c.clicked.connect(self.buttonClick)
        # widgets.btn_wired_prot.clicked.connect(self.buttonClick)
        # widgets.btn_qi_prot.clicked.connect(self.buttonClick)
        widgets.btn_chg_monitor.clicked.connect(self.buttonClick)
        
        # AI DIALOG BUTTONS
        widgets.btn_send.clicked.connect(self.buttonClick)
        widgets.btn_add_file.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False 
        themeFile = "themes\py_ui_style_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.hwcheck)
        widgets.btn_uart.setStyleSheet(UIFunctions.selectMenu(widgets.btn_uart.styleSheet()))
        
        # CONNECT RETURN KEY TO SEND BUTTON
        # ///////////////////////////////////////////////////////////////
        widgets.ai_input.installEventFilter(self)
        
    def eventFilter(self, obj, event):
        if obj == widgets.ai_input and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                # Trigger button click
                widgets.btn_send.click()
                return True
        return super().eventFilter(obj, event)


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_hwcheck":
            widgets.stackedWidget.setCurrentWidget(widgets.hwcheck)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_uart":
            widgets.stackedWidget.setCurrentWidget(widgets.uart)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_i2c":
            widgets.stackedWidget.setCurrentWidget(widgets.i2c) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SHOW NEW PAGE
        if btnName == "btn_qi_prot":
            widgets.stackedWidget.setCurrentWidget(widgets.qi_prot) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_chg_monitor":
            widgets.stackedWidget.setCurrentWidget(widgets.chg_monitor) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            # print("register BTN clicked!")

        if btnName == "btn_send":
            pass
            # widgets.stackedWidget.setCurrentWidget(widgets.hwcheck) # SET PAGE
            # UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_add_file":
            pass
            # widgets.stackedWidget.setCurrentWidget(widgets.hwcheck) # SET PAGE
            # UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_send":
            # Get message from input
            message = widgets.ai_input.toPlainText().strip()
            if message:
                # Add message to output with right-aligned style
                current_output = widgets.ai_output.toHtml()
                new_message = f'<div style="text-align: right; margin: 10px 0;"><div style="display: inline-block; background-color: #dcf8c6; padding: 10px 15px; border-radius: 18px; max-width: 70%;">{message}</div></div>'
                widgets.ai_output.setHtml(current_output + new_message)
                
                # Clear input
                widgets.ai_input.clear()
                
                # Scroll to bottom
                widgets.ai_output.verticalScrollBar().setValue(widgets.ai_output.verticalScrollBar().maximum())



        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("GeniusFAE.ico"))
    window = MainWindow()
    sys.exit(app.exec())
