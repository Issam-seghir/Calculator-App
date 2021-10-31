# Calculator Application 

[![GitHub Stars](https://img.shields.io/github/stars/Issam-seghir/CalculatorApp-v1)](https://github.com/Issam-seghir/CalculatorApp-v1/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/Issam-seghir/CalculatorApp-v1)](https://github.com/Issam-seghir/CalculatorApp-v1/issues) [![Current Version](https://img.shields.io/badge/version-1.0-yellow.svg)](https://github.com/Issam-seghir/CalculatorApp-v1)

Simple **calculator** with **random** number button and **_dark gray theme_** created with :

- PyQt6
- Python 3.9.7

> you can download the dark gray style from this [source](https://github.com/mstuttgart/qdarkgraystyle/tree/master)  
> (**you don't need it to run the script**)

## **on Windows 10**

## ![in windows](https://i.imgur.com/fddyaGC.png)

## **on Linux Ubuntu 20.04**

## ![in linux](https://i.imgur.com/HhVN6wh.png)

## Table of contents

  - [1. Setup](#1-setup)
    - [1.1. install python 3.x](#11-install-python-3x)
    - [1.2. install PyQt6](#12-install-pyqt6)
  - [2. Launch](#2-launch)
  - [3. License](#3-license)

---

<!--
## Features
## To-do
## Team
-->

## 1. Setup

### 1.1. install python 3.x

from [pthon.org](https://www.python.org/downloads/) website

### 1.2. install PyQt6

`pip3 install PyQt6`

if you want to use **PyQt5** :

1. `pip3 install PyQt5`
2. replace this lines :

   ```python
   from PyQt6.QtCore import ...
   from PyQt6.QtGui import ...
   from PyQt6.QtWidgets import ...
   from PyQt6.uic.load_ui import loadUi

   ```

   with

   ```python
   from PyQt5.QtCore import ...
   from PyQt5.QtGui import ...
   from PyQt5.QtWidgets import ...
   from PyQt5.uic import loadUi

   ```

## 2. Launch

Launch **calculator.exe**

or in your **terminal**_**/**_**cmd** :

`python path/main.py`

## 3. License

- This programme is under GPLv3 license
- [QDarkGrayStyle](https://github.com/mstuttgart/qdarkgraystyle/tree/master) is under MIT license
