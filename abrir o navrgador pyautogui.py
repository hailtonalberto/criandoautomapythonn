import pyautogui
import webbrowser
pyautogui.PAUSE = 2
opc = pyautogui.confirm(text="voçê esta pronto para abrir o site de noticias?",title="site",buttons=["sim","não"])

if opc=="sim":
    webbrowser.open("www.uol.com.br")
else:
    pyautogui.alert("fim","sair")
