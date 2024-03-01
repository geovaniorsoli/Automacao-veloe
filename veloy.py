import pyautogui
import time
import threading

# Função para esperar pela tecla 'q' para parar a execução
def check_stop():
    global stop_flag
    while True:
        if input() == 'q':
            stop_flag = True
            break

# Função para clicar nas coordenadas especificadas
def click_coordinates(x, y):
    pyautogui.click(x=x, y=y)
    time.sleep(2)

# Inicializar o sinalizador de parada
stop_flag = False

# Iniciar a thread para verificar a tecla 'q'
threading.Thread(target=check_stop).start()

# Repetir o código 10 vezes
while True:
    try:
        time.sleep(1)

        click_coordinates(x=86, y=632) #checkbox
        
        click_coordinates(x=1748, y=501) #subtituir / cancelar
                
        click_coordinates(x=63, y=718) #outro motivo
        
        click_coordinates(x=200, y=773) #box devolvido
        
        pyautogui.write("Devolvido")
        
        click_coordinates(x=395, y=893) #cancelar
                
        click_coordinates(x=303, y=981) #cancelar tag
        
        click_coordinates(x=1146, y=609) #botao ok

        time.sleep(2) #tempo para carregar tela

        click_coordinates(x=1184, y=192) #minhas tags

        click_coordinates(x=1177, y=234) #tags ativas e canceladas

    except KeyboardInterrupt:
        print("Script encerrado pelo usuário.")
        break


