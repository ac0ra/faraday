'''
Faraday Penetration Test IDE
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information

'''
#!/usr/bin/env python
import PyQt4 as qt
from PyQt4 import QtGui

class LocationToolbar(QtGui.QToolBar):

    def __init__(self, parent, name, *args, **kwargs):
        QtGui.QToolBar.__init__(self, parent, name)
        self.setName(name)
        hb = QtGui.QHBoxLayout(self)
        self._lstr = qt.QLabel("Filter: ", hb, "Filter label")
                                                                              
                                                
                                                                      
                                                      
        self._lcombo = CustomQCombobox(True, hb, 'Filter ComboBox',parent.setFilter)
        self._values = [""]
        self._lcombo.insertStrList(self._values)
        self._lcombo.setFixedSize(300, 25)
        self._lbutton = qt.QPushButton("Set", hb, "Filter Toggle Button")
        self._lbutton.setFixedSize(50, 25)
        self.connect(self._lbutton, qt.SIGNAL('clicked()'), parent.setFilter)


    def getSelectedValue(self):
        return str(self._lcombo.currentText())

    def addFilter(self, new_filter):
        self._lcombo.insertItem(new_filter)

class CustomQCombobox(QtGui.QComboBox):
    def __init__(self, rw, parent, name,callback):
        QtGui.QComboBox.__init__(self, rw, parent, name)
        self.callback=callback

                                    
                          
                                     
                             
               
                            
              
                        
                       

    def keyReleaseEvent(self, event):
                                     
                             
               
                            
        self.callback()
        event.ignore()       

class PerspectiveToolbar(QtGui.QHBoxLayout):
    def __init__(self, parent, name, *args, **kwargs):
        QtGui.QHBoxLayout.__init__(self, parent, name)
        self.setName(name)
        self.setSpacing(0)
        hb = QtGui.QHBoxLayout(self)
        self._lstr = qt.QLabel("Perspective", hb, "perspective_label")
        self._lcombo = QtGui.QComboBox(hb,'Perspective_ComboBox')
        self.connect(self._lcombo, qt.SIGNAL('activated(int)'), parent.setActivePerspective)

    def addPerspective(self, new):
        self._lcombo.insertItem(new)

    def getSelectedValue(self):
        return str(self._lcombo.currentText())

    def sizeHint(self):
        return qt.QSize(70, 20)
