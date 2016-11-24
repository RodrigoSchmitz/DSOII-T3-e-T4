import sys,math
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from math import sqrt
 
num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""
 
opVar = True
 
sumIt = 0
 
para = 0
paraVar = False
firstNum = 0
firstOp = ""
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.centralwidget = QtGui.QWidget(self)
 
        self.line = QtGui.QLineEdit(self)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setMinimumSize(200,25)
 
        zero = QtGui.QPushButton("0",self)
        zero.setMinimumSize(35,30)
 
        one = QtGui.QPushButton("1",self)
        one.setMinimumSize(35,30)
 
        two = QtGui.QPushButton("2",self)
        two.setMinimumSize(35,30)
 
        three = QtGui.QPushButton("3",self)
        three.setMinimumSize(35,30)
 
        four = QtGui.QPushButton("4",self)
        four.setMinimumSize(35,30)
 
        five = QtGui.QPushButton("5",self)
        five.setMinimumSize(35,30)
 
        six = QtGui.QPushButton("6",self)
        six.setMinimumSize(35,30)
 
        seven = QtGui.QPushButton("7",self)
        seven.setMinimumSize(35,30)
 
        eight = QtGui.QPushButton("8",self)
        eight.setMinimumSize(35,30)
 
        nine = QtGui.QPushButton("9",self)
        nine.setMinimumSize(35,30)
 
        switch = QtGui.QPushButton("+/-",self)
        switch.setMinimumSize(35,30)
        switch.clicked.connect(self.Switch)
 
        point = QtGui.QPushButton(".",self)
        point.setMinimumSize(35,30)
        point.clicked.connect(self.pointClicked)
 
        div = QtGui.QPushButton("/",self)
        div.move(130,75)
        div.setMinimumSize(35,30)
 
        mult = QtGui.QPushButton("*",self)
        mult.setMinimumSize(35,30)
 
        minus = QtGui.QPushButton("-",self)
        minus.setMinimumSize(35,30)
 
        plus = QtGui.QPushButton("+",self)
        plus.setMinimumSize(35,30)
 
        sqrt = QtGui.QPushButton("√",self)
        sqrt.setMinimumSize(35,30)
 
        squared = QtGui.QPushButton("x²",self)
        squared.setMinimumSize(35,30)
 
        equal = QtGui.QPushButton("=",self)
        equal.setMinimumSize(35,65)
        equal.clicked.connect(self.Equal)
 
        c = QtGui.QPushButton("C",self)
        c.setMinimumSize(70,30)
        c.clicked.connect(self.C)
 
        ce = QtGui.QPushButton("CE",self)
        ce.setMinimumSize(70,30)
        ce.clicked.connect(self.CE)
 
        back = QtGui.QPushButton("Back",self)
        back.setMinimumSize(35,30)
        back.clicked.connect(self.Back)
 
        self.para = QtGui.QPushButton("( )",self)
        self.para.setMinimumSize(35,30)
        self.para.clicked.connect(self.Para)
        self.para.hide()
 
        self.power = QtGui.QPushButton("x^y",self)
        self.power.setMinimumSize(35,30)
 
        self.perc = QtGui.QPushButton("%",self)
        self.perc.setMinimumSize(35,30)
 
        self.ln = QtGui.QPushButton("ln",self)
        self.ln.setMinimumSize(35,30)
         
        self.fact = QtGui.QPushButton("n!",self)
        self.fact.setMinimumSize(35,30)
 
        self.eu = QtGui.QPushButton("e",self)
        self.eu.setMinimumSize(35,30)
        self.eu.hide()
 
        self.pi = QtGui.QPushButton("π",self)
        self.pi.setMinimumSize(35,30)
        self.pi.hide()
 
        self.sin = QtGui.QPushButton("sin",self)
        self.sin.setMinimumSize(35,30)
 
        self.cos = QtGui.QPushButton("cos",self)
        self.cos.setMinimumSize(35,30)
 
        self.tan = QtGui.QPushButton("tan",self)
        self.tan.setMinimumSize(35,30)
 
        self.asin = QtGui.QPushButton("asin",self)
        self.asin.setMinimumSize(35,30)
 
        self.acos = QtGui.QPushButton("acos",self)
        self.acos.setMinimumSize(35,30)
 
        self.sp1 = QtGui.QPushButton(self)
        self.sp1.setMinimumSize(35,30)
        self.sp1.hide()
        self.sp1.setStyleSheet("border-radius:5px;")
 
        self.sp2 = QtGui.QPushButton(self)
        self.sp2.setMinimumSize(35,30)
        self.sp2.hide()
        self.sp2.setStyleSheet("border-radius:5px;")
 
        self.sp3 = QtGui.QPushButton(self)
        self.sp3.setMinimumSize(35,30)
        self.sp3.hide()
        self.sp3.setStyleSheet("border-radius:5px;")
 
        self.sp4 = QtGui.QPushButton(self)
        self.sp4.setMinimumSize(35,30)
        self.sp4.hide()
        self.sp4.setStyleSheet("border-radius:5px;")
 
        nums = [zero,one,two,three,four,five,six,seven,eight,nine,self.pi,self.eu]
 
        self.ops = [equal,self.para,back,c,ce,div,mult,minus,plus,self.power,self.perc,self.ln,self.fact,self.sin,self.cos,self.tan,self.asin,self.acos,sqrt,squared]
 
        for i in nums:
            i.setStyleSheet("color:blue;")
            i.clicked.connect(self.Nums)
 
        for i in self.ops:
            i.setStyleSheet("color:red;")
 
        for i in self.ops[5:10]:
            i.clicked.connect(self.Operator)
 
        for i in self.ops[10:]:
            i.clicked.connect(self.SpecialOperator)
             
        for i in self.ops[9:-2]:
            i.hide()
 
        self.grid = QtGui.QGridLayout()
 
#------------ Normal ------------------------
 
        self.grid.addWidget(self.line,0,0, 1, 5)
        self.grid.addWidget(seven,2,0, 1, 1)
        self.grid.addWidget(eight,2,1, 1, 1)
        self.grid.addWidget(nine,2,2, 1, 1)
        self.grid.addWidget(div,2,3, 1, 1)
        self.grid.addWidget(sqrt,2,4, 1, 1)
        self.grid.addWidget(four,3,0, 1, 1)
        self.grid.addWidget(five,3,1, 1, 1)
        self.grid.addWidget(six,3,2, 1, 1)
        self.grid.addWidget(mult,3,3, 1, 1)
        self.grid.addWidget(squared,3,4, 1, 1)
        self.grid.addWidget(one,4,0, 1, 1)
        self.grid.addWidget(two,4,1, 1, 1)
        self.grid.addWidget(three,4,2, 1, 1)
        self.grid.addWidget(minus,4,3, 1, 1)
        self.grid.addWidget(equal,4,4, 1, 1)
        self.grid.addWidget(zero,5,0, 1, 1)
        self.grid.addWidget(switch,5,1, 1, 1)
        self.grid.addWidget(point,5,2, 1, 1)
        self.grid.addWidget(plus,5,3, 1, 1)
        self.grid.addWidget(back,1,0, 1, 1)
        self.grid.addWidget(c,1,1, 1, 1)
        self.grid.addWidget(ce,1,3, 1, 1)
 
#------------ Scientific ----------------
         
        self.grid.addWidget(self.para,2,6, 1, 1)
        self.grid.addWidget(self.power,3,6, 1, 1)
        self.grid.addWidget(self.perc,4,6, 1, 1)
        self.grid.addWidget(self.ln,5,6, 1, 1)
        self.grid.addWidget(self.fact,2,7, 1, 1)
        self.grid.addWidget(self.pi,3,7, 1, 1)
        self.grid.addWidget(self.eu,4,7, 1, 1)
        self.grid.addWidget(self.sin,5,7, 1, 1)
        self.grid.addWidget(self.cos,2,8, 1, 1)
        self.grid.addWidget(self.asin,3,8, 1, 1)
        self.grid.addWidget(self.acos,4,8, 1, 1)
        self.grid.addWidget(self.tan,5,8, 1, 1)
 
        self.grid.addWidget(self.sp1,2,5,1,1)
        self.grid.addWidget(self.sp2,3,5,1,1)
        self.grid.addWidget(self.sp3,4,5,1,1)
        self.grid.addWidget(self.sp4,5,5,1,1)
         
        self.centralwidget.setLayout(self.grid)
         
             
#---------Window settings --------------------------------
         
        self.setGeometry(300,300,210,220)
        self.setFixedSize(212,240)
        self.setWindowTitle("PyCalc")
        self.show()
 
        self.setCentralWidget(self.centralwidget)
 
#----------- Menubar ----------------------------------
 
        self.menubar = self.menuBar()
        menu = self.menubar.addMenu("View")
 
        normal = QtGui.QAction("Normal",self)
        scientific = QtGui.QAction("Scientific",self)
 
        menu.addAction(normal)
        menu.addAction(scientific)
 
        normal.triggered.connect(self.Normal)
        scientific.triggered.connect(self.Scientific)
 
    def Nums(self):
        global opVar
         
        sender = self.sender()
         
        newNum = sender.text()
 
        print(newNum)
 
        if opVar == False:
            if newNum == "e":
                self.line.setText(self.line.text() + str(math.e))
                 
            elif newNum == "π":
                self.line.setText(self.line.text() + str(math.pi))
                 
            else:
                self.line.setText(self.line.text() + newNum)
 
        else:
            if newNum == "e":
                print(math.e)
                self.line.setText(str(math.e))
                 
            elif newNum == "π":
                print(math.pi)
                self.line.setText(str(math.pi))
                 
            else:
                self.line.setText(newNum)
            opVar = False
             
         
 
    def pointClicked(self):
         
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")
             
 
    def Switch(self):
        global num
         
        try:
            num = int(self.line.text())
             
        except:
            num = float(self.line.text())
      
        num = num - num * 2
 
        numStr = str(num)
         
        self.line.setText(numStr)
 
    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt
 
        sumIt += 1
 
        if sumIt > 1:
            self.Equal()
 
        num = self.line.text()
 
        sender = self.sender()
 
        operator = sender.text()
        print(operator)
         
        opVar = True
 
    def SpecialOperator(self):
 
        sender = self.sender()
        operator = sender.text()
        num = float(self.line.text())
 
        if operator == "ln":
            num = math.log(num)
 
        elif operator == "√":
            num = math.sqrt(num)
 
        elif operator == "x²":
            num = num ** 2
 
        elif operator == "n!":
            num = math.factorial(num)
 
        elif operator == "sin":
            num = math.sin(num)
 
        elif operator == "cos":
            num = math.cos(num)
 
        elif operator == "tan":
            num = math.tan(num)
 
        elif operator == "acos":
            num = math.acos(num)
 
        elif operator == "asin":
            num = math.asin(num)
 
        elif operator == "%":
            num = num / 100
 
        self.line.setText(str(num))
 
    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar
        global sumIt
        global paraVar
        global firstNum
        global firstOp
 
        sumIt = 0
        if paraVar == True:
            num = firstNum
            operator = firstOp
             
        newNum = self.line.text()
 
        print(num)
        print(operator)
        print(newNum)
         
        if operator == "+":
            sumAll = float(num) + float(newNum)
 
        elif operator == "-":
            sumAll = float(num) - float(newNum)
 
        elif operator == "/":
            sumAll = float(num) / float(newNum)
 
        elif operator == "*":
            sumAll = float(num) * float(newNum)
 
        elif operator == "x^y":
            sumAll = math.pow(float(num),float(newNum)) 
             
        print(sumAll)
        self.line.setText(str(sumAll))  
        opVar = True
        paraVar = False
 
    def Back(self):
        self.line.backspace()
 
    def C(self):
        self.line.clear()
 
    def CE(self):
        global newNum
        global sumAll
        global operator
        global num
        global sumIt
         
        self.line.clear()
 
        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""
        sumIt = 0
 
    def Para(self):
        global para
        global paraVar
        global operator
        global num
        global sumAll
        global newNum
        global firstNum
        global firstOp
        global sumIt
 
        if para == 0:
            self.line.setText("(")
 
            firstNum = num
            firstOp = operator
 
            para = 1
            sumIt = 0
             
        else:
            self.Equal()
 
            paraVar = True
 
            para = 0
 
    def Normal(self):
        self.setFixedSize(212,240)
 
        self.grid.addWidget(self.line,0,0, 1, 5)
 
        self.para.hide()
        self.pi.hide()
        self.eu.hide()
 
        self.sp1.hide()
        self.sp2.hide()
        self.sp3.hide()
        self.sp4.hide()
 
        for i in self.ops[9:-2]:
            i.hide()
         
    def Scientific(self):
        self.setFixedSize(370,240)
 
        self.grid.addWidget(self.line,0,0, 1, 9)
 
        self.para.show()
        self.pi.show()
        self.eu.show()
 
        self.sp1.show()
        self.sp2.show()
        self.sp3.show()
        self.sp4.show()
 
        for i in self.ops[9:-2]:
            i.show()
 
def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()import sys,math
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from math import sqrt
 
num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""
 
opVar = True
 
sumIt = 0
 
para = 0
paraVar = False
firstNum = 0
firstOp = ""
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.centralwidget = QtGui.QWidget(self)
 
        self.line = QtGui.QLineEdit(self)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setMinimumSize(200,25)
 
        zero = QtGui.QPushButton("0",self)
        zero.setMinimumSize(35,30)
 
        one = QtGui.QPushButton("1",self)
        one.setMinimumSize(35,30)
 
        two = QtGui.QPushButton("2",self)
        two.setMinimumSize(35,30)
 
        three = QtGui.QPushButton("3",self)
        three.setMinimumSize(35,30)
 
        four = QtGui.QPushButton("4",self)
        four.setMinimumSize(35,30)
 
        five = QtGui.QPushButton("5",self)
        five.setMinimumSize(35,30)
 
        six = QtGui.QPushButton("6",self)
        six.setMinimumSize(35,30)
 
        seven = QtGui.QPushButton("7",self)
        seven.setMinimumSize(35,30)
 
        eight = QtGui.QPushButton("8",self)
        eight.setMinimumSize(35,30)
 
        nine = QtGui.QPushButton("9",self)
        nine.setMinimumSize(35,30)
 
        switch = QtGui.QPushButton("+/-",self)
        switch.setMinimumSize(35,30)
        switch.clicked.connect(self.Switch)
 
        point = QtGui.QPushButton(".",self)
        point.setMinimumSize(35,30)
        point.clicked.connect(self.pointClicked)
 
        div = QtGui.QPushButton("/",self)
        div.move(130,75)
        div.setMinimumSize(35,30)
 
        mult = QtGui.QPushButton("*",self)
        mult.setMinimumSize(35,30)
 
        minus = QtGui.QPushButton("-",self)
        minus.setMinimumSize(35,30)
 
        plus = QtGui.QPushButton("+",self)
        plus.setMinimumSize(35,30)
 
        sqrt = QtGui.QPushButton("√",self)
        sqrt.setMinimumSize(35,30)
 
        squared = QtGui.QPushButton("x²",self)
        squared.setMinimumSize(35,30)
 
        equal = QtGui.QPushButton("=",self)
        equal.setMinimumSize(35,65)
        equal.clicked.connect(self.Equal)
 
        c = QtGui.QPushButton("C",self)
        c.setMinimumSize(70,30)
        c.clicked.connect(self.C)
 
        ce = QtGui.QPushButton("CE",self)
        ce.setMinimumSize(70,30)
        ce.clicked.connect(self.CE)
 
        back = QtGui.QPushButton("Back",self)
        back.setMinimumSize(35,30)
        back.clicked.connect(self.Back)
 
        self.para = QtGui.QPushButton("( )",self)
        self.para.setMinimumSize(35,30)
        self.para.clicked.connect(self.Para)
        self.para.hide()
 
        self.power = QtGui.QPushButton("x^y",self)
        self.power.setMinimumSize(35,30)
 
        self.perc = QtGui.QPushButton("%",self)
        self.perc.setMinimumSize(35,30)
 
        self.ln = QtGui.QPushButton("ln",self)
        self.ln.setMinimumSize(35,30)
         
        self.fact = QtGui.QPushButton("n!",self)
        self.fact.setMinimumSize(35,30)
 
        self.eu = QtGui.QPushButton("e",self)
        self.eu.setMinimumSize(35,30)
        self.eu.hide()
 
        self.pi = QtGui.QPushButton("π",self)
        self.pi.setMinimumSize(35,30)
        self.pi.hide()
 
        self.sin = QtGui.QPushButton("sin",self)
        self.sin.setMinimumSize(35,30)
 
        self.cos = QtGui.QPushButton("cos",self)
        self.cos.setMinimumSize(35,30)
 
        self.tan = QtGui.QPushButton("tan",self)
        self.tan.setMinimumSize(35,30)
 
        self.asin = QtGui.QPushButton("asin",self)
        self.asin.setMinimumSize(35,30)
 
        self.acos = QtGui.QPushButton("acos",self)
        self.acos.setMinimumSize(35,30)
 
        self.sp1 = QtGui.QPushButton(self)
        self.sp1.setMinimumSize(35,30)
        self.sp1.hide()
        self.sp1.setStyleSheet("border-radius:5px;")
 
        self.sp2 = QtGui.QPushButton(self)
        self.sp2.setMinimumSize(35,30)
        self.sp2.hide()
        self.sp2.setStyleSheet("border-radius:5px;")
 
        self.sp3 = QtGui.QPushButton(self)
        self.sp3.setMinimumSize(35,30)
        self.sp3.hide()
        self.sp3.setStyleSheet("border-radius:5px;")
 
        self.sp4 = QtGui.QPushButton(self)
        self.sp4.setMinimumSize(35,30)
        self.sp4.hide()
        self.sp4.setStyleSheet("border-radius:5px;")
 
        nums = [zero,one,two,three,four,five,six,seven,eight,nine,self.pi,self.eu]
 
        self.ops = [equal,self.para,back,c,ce,div,mult,minus,plus,self.power,self.perc,self.ln,self.fact,self.sin,self.cos,self.tan,self.asin,self.acos,sqrt,squared]
 
        for i in nums:
            i.setStyleSheet("color:blue;")
            i.clicked.connect(self.Nums)
 
        for i in self.ops:
            i.setStyleSheet("color:red;")
 
        for i in self.ops[5:10]:
            i.clicked.connect(self.Operator)
 
        for i in self.ops[10:]:
            i.clicked.connect(self.SpecialOperator)
             
        for i in self.ops[9:-2]:
            i.hide()
 
        self.grid = QtGui.QGridLayout()
 
#------------ Normal ------------------------
 
        self.grid.addWidget(self.line,0,0, 1, 5)
        self.grid.addWidget(seven,2,0, 1, 1)
        self.grid.addWidget(eight,2,1, 1, 1)
        self.grid.addWidget(nine,2,2, 1, 1)
        self.grid.addWidget(div,2,3, 1, 1)
        self.grid.addWidget(sqrt,2,4, 1, 1)
        self.grid.addWidget(four,3,0, 1, 1)
        self.grid.addWidget(five,3,1, 1, 1)
        self.grid.addWidget(six,3,2, 1, 1)
        self.grid.addWidget(mult,3,3, 1, 1)
        self.grid.addWidget(squared,3,4, 1, 1)
        self.grid.addWidget(one,4,0, 1, 1)
        self.grid.addWidget(two,4,1, 1, 1)
        self.grid.addWidget(three,4,2, 1, 1)
        self.grid.addWidget(minus,4,3, 1, 1)
        self.grid.addWidget(equal,4,4, 1, 1)
        self.grid.addWidget(zero,5,0, 1, 1)
        self.grid.addWidget(switch,5,1, 1, 1)
        self.grid.addWidget(point,5,2, 1, 1)
        self.grid.addWidget(plus,5,3, 1, 1)
        self.grid.addWidget(back,1,0, 1, 1)
        self.grid.addWidget(c,1,1, 1, 1)
        self.grid.addWidget(ce,1,3, 1, 1)
 
#------------ Scientific ----------------
         
        self.grid.addWidget(self.para,2,6, 1, 1)
        self.grid.addWidget(self.power,3,6, 1, 1)
        self.grid.addWidget(self.perc,4,6, 1, 1)
        self.grid.addWidget(self.ln,5,6, 1, 1)
        self.grid.addWidget(self.fact,2,7, 1, 1)
        self.grid.addWidget(self.pi,3,7, 1, 1)
        self.grid.addWidget(self.eu,4,7, 1, 1)
        self.grid.addWidget(self.sin,5,7, 1, 1)
        self.grid.addWidget(self.cos,2,8, 1, 1)
        self.grid.addWidget(self.asin,3,8, 1, 1)
        self.grid.addWidget(self.acos,4,8, 1, 1)
        self.grid.addWidget(self.tan,5,8, 1, 1)
 
        self.grid.addWidget(self.sp1,2,5,1,1)
        self.grid.addWidget(self.sp2,3,5,1,1)
        self.grid.addWidget(self.sp3,4,5,1,1)
        self.grid.addWidget(self.sp4,5,5,1,1)
         
        self.centralwidget.setLayout(self.grid)
         
             
#---------Window settings --------------------------------
         
        self.setGeometry(300,300,210,220)
        self.setFixedSize(212,240)
        self.setWindowTitle("PyCalc")
        self.show()
 
        self.setCentralWidget(self.centralwidget)
 
#----------- Menubar ----------------------------------
 
        self.menubar = self.menuBar()
        menu = self.menubar.addMenu("View")
 
        normal = QtGui.QAction("Normal",self)
        scientific = QtGui.QAction("Scientific",self)
 
        menu.addAction(normal)
        menu.addAction(scientific)
 
        normal.triggered.connect(self.Normal)
        scientific.triggered.connect(self.Scientific)
 
    def Nums(self):
        global opVar
         
        sender = self.sender()
         
        newNum = sender.text()
 
        print(newNum)
 
        if opVar == False:
            if newNum == "e":
                self.line.setText(self.line.text() + str(math.e))
                 
            elif newNum == "π":
                self.line.setText(self.line.text() + str(math.pi))
                 
            else:
                self.line.setText(self.line.text() + newNum)
 
        else:
            if newNum == "e":
                print(math.e)
                self.line.setText(str(math.e))
                 
            elif newNum == "π":
                print(math.pi)
                self.line.setText(str(math.pi))
                 
            else:
                self.line.setText(newNum)
            opVar = False
             
         
 
    def pointClicked(self):
         
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")
             
 
    def Switch(self):
        global num
         
        try:
            num = int(self.line.text())
             
        except:
            num = float(self.line.text())
      
        num = num - num * 2
 
        numStr = str(num)
         
        self.line.setText(numStr)
 
    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt
 
        sumIt += 1
 
        if sumIt > 1:
            self.Equal()
 
        num = self.line.text()
 
        sender = self.sender()
 
        operator = sender.text()
        print(operator)
         
        opVar = True
 
    def SpecialOperator(self):
 
        sender = self.sender()
        operator = sender.text()
        num = float(self.line.text())
 
        if operator == "ln":
            num = math.log(num)
 
        elif operator == "√":
            num = math.sqrt(num)
 
        elif operator == "x²":
            num = num ** 2
 
        elif operator == "n!":
            num = math.factorial(num)
 
        elif operator == "sin":
            num = math.sin(num)
 
        elif operator == "cos":
            num = math.cos(num)
 
        elif operator == "tan":
            num = math.tan(num)
 
        elif operator == "acos":
            num = math.acos(num)
 
        elif operator == "asin":
            num = math.asin(num)
 
        elif operator == "%":
            num = num / 100
 
        self.line.setText(str(num))
 
    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar
        global sumIt
        global paraVar
        global firstNum
        global firstOp
 
        sumIt = 0
        if paraVar == True:
            num = firstNum
            operator = firstOp
             
        newNum = self.line.text()
 
        print(num)
        print(operator)
        print(newNum)
         
        if operator == "+":
            sumAll = float(num) + float(newNum)
 
        elif operator == "-":
            sumAll = float(num) - float(newNum)
 
        elif operator == "/":
            sumAll = float(num) / float(newNum)
 
        elif operator == "*":
            sumAll = float(num) * float(newNum)
 
        elif operator == "x^y":
            sumAll = math.pow(float(num),float(newNum)) 
             
        print(sumAll)
        self.line.setText(str(sumAll))  
        opVar = True
        paraVar = False
 
    def Back(self):
        self.line.backspace()
 
    def C(self):
        self.line.clear()
 
    def CE(self):
        global newNum
        global sumAll
        global operator
        global num
        global sumIt
         
        self.line.clear()
 
        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""
        sumIt = 0
 
    def Para(self):
        global para
        global paraVar
        global operator
        global num
        global sumAll
        global newNum
        global firstNum
        global firstOp
        global sumIt
 
        if para == 0:
            self.line.setText("(")
 
            firstNum = num
            firstOp = operator
 
            para = 1
            sumIt = 0
             
        else:
            self.Equal()
 
            paraVar = True
 
            para = 0
 
    def Normal(self):
        self.setFixedSize(212,240)
 
        self.grid.addWidget(self.line,0,0, 1, 5)
 
        self.para.hide()
        self.pi.hide()
        self.eu.hide()
 
        self.sp1.hide()
        self.sp2.hide()
        self.sp3.hide()
        self.sp4.hide()
 
        for i in self.ops[9:-2]:
            i.hide()
         
    def Scientific(self):
        self.setFixedSize(370,240)
 
        self.grid.addWidget(self.line,0,0, 1, 9)
 
        self.para.show()
        self.pi.show()
        self.eu.show()
 
        self.sp1.show()
        self.sp2.show()
        self.sp3.show()
        self.sp4.show()
 
        for i in self.ops[9:-2]:
            i.show()
 
def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
