import pyautogui
import time

try:
    while True:
        # Obter e imprimir as coordenadas do cursor a cada segundo
        x, y = pyautogui.position()
        print(f"Coordenadas do Cursor: X={x}, Y={y}")

        # Aguarde 1 segundo
        time.sleep(1)

except KeyboardInterrupt:
    # Se o usuário pressionar Ctrl+C, encerre o loop
    print("Script encerrado pelo usuário.")
