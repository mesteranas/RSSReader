import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class ADD (qt.QDialog):
    def __init__ (self,p):
        super().__init__(p)
        self.p=p
        self.setWindowTitle(_("add website"))
        layout=qt.QVBoxLayout(self)
        self.title=qt.QLineEdit()
        self.title.setAccessibleName(_("title"))
        layout.addWidget(self.title)
        self.URL=qt.QLineEdit()
        self.URL.setAccessibleName(_("URL"))
        layout.addWidget(self.URL)
        self.add=qt.QPushButton(_("add"))
        self.add.clicked.connect(self.onAdd)
        layout.addWidget(self.add)
    def onAdd(self):
        self.p.website[self.title.text()]=self.URL.text()
        self.p.websites.addItem(self.title.text())
        self.close()