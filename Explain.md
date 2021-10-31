# Explain some line of code

```python
for number in range(10):
    exec(f'btn{number} = window.findChild(QPushButton, "pushButton_{number}")')
    exec(f"btnG_operands.addButton(btn{number},number)")

```

**is equivalent to :**

> `exec(f'btn{number} = window.findChild(QPushButton, "pushButton_{number}")')`

```python
btn0 = window.findChild(QPushButton, "pushButton_0")
btn1 = window.findChild(QPushButton, "pushButton_1")
btn2 = window.findChild(QPushButton, "pushButton_2")
btn3 = window.findChild(QPushButton, "pushButton_3")
btn4 = window.findChild(QPushButton, "pushButton_4")
btn5 = window.findChild(QPushButton, "pushButton_5")
btn6 = window.findChild(QPushButton, "pushButton_6")
btn7 = window.findChild(QPushButton, "pushButton_7")
btn8 = window.findChild(QPushButton, "pushButton_8")
btn9 = window.findChild(QPushButton, "pushButton_9")

```

> `exec(f"btnG_operands.addButton(btn{number},number)")`

```python
btnG_operands.addButton(btn0,number)
btnG_operands.addButton(btn1,number)
btnG_operands.addButton(btn2,number)
btnG_operands.addButton(btn3,number)
btnG_operands.addButton(btn4,number)
btnG_operands.addButton(btn5,number)
btnG_operands.addButton(btn6,number)
btnG_operands.addButton(btn7,number)
btnG_operands.addButton(btn8,number)
btnG_operands.addButton(btn9,number)
```

---

```python
operator = ["Sub","Add","Div","Mod","Mul","Point","Equal","Clear","Back","Rand",]
for opr in operator:
    exec(f'btn{opr} = window.findChild(QPushButton, "pushButton_{opr}")')
    if opr in operator[0:6]:
        exec(f"btnG_operator.addButton(btn{opr})")

```

**is equevalent to :**

> `exec(f'btn{opr} = window.findChild(QPushButton, "pushButton_{opr}")')`

```python
    btnSub = window.findChild(QPushButton, "pushButton_Sub")
    btnAdd = window.findChild(QPushButton, "pushButton_Add")
    btnDiv = window.findChild(QPushButton, "pushButton_Div")
    btnMod = window.findChild(QPushButton, "pushButton_Mod")
    btnMul = window.findChild(QPushButton, "pushButton_Mul")
    btnPoint = window.findChild(QPushButton, "pushButton_Point")
    btnEqual = window.findChild(QPushButton, "pushButton_Equal")
    btnClear = window.findChild(QPushButton, "pushButton_Clear")
    btnBack = window.findChild(QPushButton, "pushButton_Back")
    btnRand = window.findChild(QPushButton, "pushButton_Rand")

```

> `exec(f"btnG_operator.addButton(btn{opr})")`

```python
btnG_operator.addButton(btnSub)
btnG_operator.addButton(btnAdd)
btnG_operator.addButton(btnDiv)
btnG_operator.addButton(btnMod)
btnG_operator.addButton(btnMul)
btnG_operator.addButton(btnPoint)
```

---

```python
slots = ["calcul_operation", "clear", "back", "rand"]
for i, j in zip(operator[6:], slots):
    exec(f"btn{i}.clicked.connect({j})")

```

**is equivalent to :**

```python
btnEqual.clicked.connect(calcul_operation)
btnClear.clicked.connect(clear)
btnBack.clicked.connect(back)
btnRand.clicked.connect(rand)
```

---

## Regex explain

```python
x = re.sub("[',[\] ]", "", str(BtnList))
```

**_delete one of :_**

![this](https://i.imgur.com/oPhHRdx.png)

> **['7', '+', '2'] => 7+2**

---

```python
re.findall(r"[\]+\.[0-9]+\.", x)
```

**_find all of_**
![this1](https://i.imgur.com/i5zomhz.png)

**example:**

> 18.15.

> 12..1
