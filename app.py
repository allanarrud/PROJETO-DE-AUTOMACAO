import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(985,547,duration=2)
pyautogui.write('beto')
# 2 - Clicar e digitar minha senha
pyautogui.click(1011,584,duration=2)
pyautogui.write('123456')
# 3 - clicar em 'Entrar'
pyautogui.click(813,616,duration=2)
# 4-  Extrair cada produto
with open('arquivo.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #1 - clicar e digitar produto
        pyautogui.click(592,516,duration=2)
        pyautogui.write(produto)
        #2 - clicar e digitar quantidade
        pyautogui.click(592,566,duration=2)
        pyautogui.write(quantidade)
        #3 - clicar e digitar preço
        pyautogui.click(592,600,duration=2)
        pyautogui.write(preco)
        #4 - clicar em 'Registrar'
        pyautogui.click(406,833,duration=1)
        sleep(1)