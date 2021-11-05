## Welcome to GitHub Pages




### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
`
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(540, 280)
		self.ProjectPath = QtWidgets.QLabel(Form)
		self.ProjectPath.setGeometry(QtCore.QRect(25, 50, 100, 31))
		self.MapName = QtWidgets.QLabel(Form)
		self.MapName.setGeometry(QtCore.QRect(25, 100, 100, 31))
		self.OutputPath = QtWidgets.QLabel(Form)
		self.OutputPath.setGeometry(QtCore.QRect(25, 150, 500, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.ProjectPath.setFont(font)
		self.ProjectPath.setObjectName("label_ProjectPath")
		self.MapName.setFont(font)
		self.MapName.setObjectName("label_MapName")
		font.setPointSize(9)
		self.OutputPath.setFont(font)
		self.OutputPath.setObjectName("label_OutputPath")
		self.InputLine_ProjectPath = QtWidgets.QLineEdit(Form)
		self.InputLine_ProjectPath.setGeometry(QtCore.QRect(130, 50, 371, 34))
		self.InputLine_MapName = QtWidgets.QLineEdit(Form)
		self.InputLine_MapName.setGeometry(QtCore.QRect(130, 100, 371, 34))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.InputLine_ProjectPath.setFont(font)
		self.InputLine_ProjectPath.setObjectName("InputLine")
		self.InputLine_MapName.setFont(font)
		self.InputLine_MapName.setObjectName("InputLine")
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(430, 220, 70, 34))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.getLogFilePathAndName)
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

`
[Link](url) and ![Image](src)
```
