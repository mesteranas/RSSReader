import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Open (qt.QDialog):
    def __init__ (self,p,dic):
        super().__init__(p)
        self.p=dic
        layout=qt.QVBoxLayout(self)
        self.results=qt.QListWidget()
        self.results.addItems(self.p.keys())
        self.results.setAccessibleName(_("articals"))
        self.setWindowTitle(_("results"))
        layout.addWidget(self.results)
        self.open=qt.QPushButton(_("Open"))
        self.open.clicked.connect(self.onopen)
        layout.addWidget(self.open)
    def onopen(self):
        guiTools.OpenLink(self,self.p[self.results.currentItem().text()])