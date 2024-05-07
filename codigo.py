# pip install pyautogui
import pyautogui

import time

pyautogui.PAUSE = 0.5


# 1 - Acessar o sistema
# abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# acessar o sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pausa para o site carregar
time.sleep(3)


# 2 - Fazer login
# clicar na barra de login e escrever
pyautogui.click(x=1205, y=1212)
pyautogui.write("davi@gmail.com")

# clicar na barra de senha e escrever
pyautogui.press("tab")
pyautogui.write("123456")

pyautogui.click(x=1977, y=1697)

# 3 - Abrir e importar a base de dados
# biblioteca de leitura de arquivos
# pip install pandas numpy openpyxl
import pandas as pd

table = pd.read_csv("produtos.csv")
print(table)

time.sleep(2)

# 4 - Cadastrar um produto
# escrevendo no campo código
for linha in table.index:
    codigo = str(table.loc[linha, "codigo"])
    pyautogui.click(x=1176, y=875)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca 
    marca = str(table.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # tipo
    tipo = str(table.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = str(table.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # preço_unitário
    preco = str(table.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # custo
    custo = str(table.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # obs
    obs = str(table.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)


# 5 - Repetir o processo até o final
