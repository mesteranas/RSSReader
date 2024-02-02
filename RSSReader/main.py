import sys
from custome_errors import *
sys.excepthook = my_excepthook
import feedparser
import update
import gui
import guiTools
from settings import *
import json
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
language.init_translation()
if not os.path.exists(os.path.join(os.getenv('appdata'),settings_handler.appName,"websites.json")):
    with open(os.path.join(os.getenv('appdata'),settings_handler.appName,"websites.json"),"w",encoding="utf-8") as file:
        file.write("{}")
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        with open(os.path.join(os.getenv('appdata'),settings_handler.appName,"websites.json"),"r",encoding="utf-8") as file:
            self.website=json.load(file)

        layout=qt.QVBoxLayout()
        self.websites=qt.QListWidget()
        self.websites.setAccessibleName(_("websites"))
        self.websites.addItems(self.website.keys())
        self.websites.setContextMenuPolicy(qt2.Qt.ContextMenuPolicy.CustomContextMenu)
        self.websites.customContextMenuRequested.connect(self.oncontext)
        layout.addWidget(self.websites)
        self.open=qt.QPushButton(_("open"))
        self.open.setDefault(True)
        self.open.clicked.connect(self.onRSS)
        layout.addWidget(self.open)
        self.add=qt.QPushButton(_("Add website"))
        self.add.setDefault(True)
        self.add.clicked.connect(lambda:gui.ADD(self).exec())
        layout.addWidget(self.add)
        qt1.QShortcut("delete",self).activated.connect(self.ondelete)
        self.setting=qt.QPushButton(_("settings"))
        self.setting.setDefault(True)
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        githup=qt1.QAction(_("Github"),self)
        cus.addAction(githup)
        githup.triggered.connect(lambda: guiTools.OpenLink(self,"https://Github.com/mesteranas"))
        X=qt1.QAction(_("x"),self)
        cus.addAction(X)
        X.triggered.connect(lambda:guiTools.OpenLink(self,"https://x.com/mesteranasm"))
        email=qt1.QAction(_("email"),self)
        cus.addAction(email)
        email.triggered.connect(lambda: guiTools.sendEmail("anasformohammed@gmail.com","project_type=GUI app={} version={}".format(app.name,app.version),""))
        Github_project=qt1.QAction(_("visite project on Github"),self)
        help.addAction(Github_project)
        Github_project.triggered.connect(lambda:guiTools.OpenLink(self,"https://Github.com/mesteranas/{}_GUI".format(settings_handler.appName)))
        Checkupdate=qt1.QAction(_("check for update"),self)
        help.addAction(Checkupdate)
        Checkupdate.triggered.connect(lambda:update.check(self))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
        if settings_handler.get("update","autoCheck")=="True":
            update.check(self,message=False)
    def closeEvent(self, event):
        with open(os.path.join(os.getenv('appdata'),settings_handler.appName,"websites.json"),"w",encoding="utf-8") as file:
            file.write(str(self.website).replace("'",'"'))
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def oncontext(self):
        m=qt.QMenu()
        delete=qt1.QAction(_("delete"),self)
        m.addAction(delete)
        delete.triggered.connect(self.ondelete)
        m.exec()
    def ondelete(self):
        try:
            del(self.website[self.websites.currentItem().text()])
            self.websites.clear()
            self.websites.addItems(self.website)
            guiTools.speak(_("deleted"))
        except:
            guiTools.speak(_("error"))
    def onRSS(self):
        try:
            p=feedparser.parse(self.website[self.websites.currentItem().text()])
            dic={}
            if p.bozo==0:
                for i in p.entries:
                    dic[i.title]=i.link
                gui.Open(self,dic).exec()
            else:
                qt.QMessageBox.information(self,"error",_("no RSS"))
        except:
            qt.QMessageBox.information(self,_("error"),_("please try later"))
App=qt.QApplication([])
w=main()
w.show()
App.exec()