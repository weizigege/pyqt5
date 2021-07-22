import sys
from  PyQt5.QtWidgets import  QApplication,QWidget




if __name__=='__main__':
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(400,400)
    w.setWindowTitle('你是猪吗')
    w.show()
    sys.exit(app.exec_())
