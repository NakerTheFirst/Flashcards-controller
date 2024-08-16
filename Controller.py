import pygame
import time
import psutil
import pyautogui as pag


def custom_functionality(button):
    print(f"Button {button} pressed")
    if button == 1:
        pag.press('3')
        # pag.press('right')
    elif button == 3:
        pag.press('1')
        # pag.press('left')
    elif button == 0:
        pag.press('2')
    elif button == 2:
        pag.press('Enter')
    elif button == 7:
        pag.press('f11')


# Count the number of processes already running
i = 0
for x in psutil.process_iter():
    if x.name() == "Controller.exe":
        i += 1

# Run only if there are no more than 2 "Controller.exe" processes
if i <= 2:
    pygame.init()
    is_joystick_connected = False
    last_check_time = time.time()
    check_interval = 5

    # Initial joystick connection attempt
    while not is_joystick_connected:
        try:
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            is_joystick_connected = True
        except pygame.error:
            pygame.joystick.quit()
        time.sleep(2)

    try:
        while True:
            current_time = time.time()
            if current_time - last_check_time >= check_interval:
                try:
                    pygame.joystick.quit()
                    pygame.joystick.init()
                    joystick = pygame.joystick.Joystick(0)
                    joystick.init()
                    is_joystick_connected = True
                except pygame.error:
                    is_joystick_connected = False
                last_check_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    custom_functionality(event.button)

            time.sleep(0.01)
    except KeyboardInterrupt:
        # Clean up on exit
        pygame.joystick.quit()
        pygame.quit()
