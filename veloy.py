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
for _ in range(10):
    try:
        click_coordinates(x=-1855, y=354) #checkbox
        
        click_coordinates(x=-574, y=247) #subtituir / cancelar
                
        click_coordinates(x=-1828, y=427) #outro motivo
        
        click_coordinates(x=-1774, y=474) #box devolvido
        
        pyautogui.write("Devolvido")
        
        click_coordinates(x=-1614, y=564) #cancelar
                
        click_coordinates(x=-1670, y=629) #cancelar tag
        
        click_coordinates(x=-1018, y=339) #botao ok

        time.sleep(2) #tempo para carregar tela

        click_coordinates(x=-970, y=5) #minhas tags

        click_coordinates(x=-1014, y=40) #tags ativas e canceladas

    except KeyboardInterrupt:
        print("Script encerrado pelo usuário.")
        break


