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
        time.sleep(0.5)
        
        click_coordinates(x=-574, y=247) #subtituir / cancelar
        time.sleep(0.5)
                
        click_coordinates(x=-1828, y=427) #outro motivo
        time.sleep(0.5)
        
        click_coordinates(x=-1774, y=474) #box devolvido
        time.sleep(0.5)
        
        pyautogui.write("Devolvido")
        time.sleep(0.5)
        
        click_coordinates(x=-1614, y=564) #cancelar
        time.sleep(2)
                
        click_coordinates(x=-1670, y=629)
        time.sleep(0.5)
        
        click_coordinates(x=-1018, y=339)
        time.sleep(0.5)

        time.sleep(3)

        click_coordinates(x=-970, y=5)
        time.sleep(0.5)

        click_coordinates(x=-1014, y=40)
        time.sleep(0.5)

    except KeyboardInterrupt:
        print("Script encerrado pelo usuário.")
        break


