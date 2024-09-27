
from nicegui import ui
from  pycreate2 import Create2



class ControlTab:

    def __init__(self, bot: Create2):

        self.bot = bot
        self._start_robot()

        # start, close
        with ui.column():

            ui.button('start', on_click=lambda _: self._start_robot())

            self.mode_dict = {0: 'stop', 1:'passive', 2:'safe', 3:'full'}
            robot_mode = ui.toggle(self.mode_dict, value = 0,
                                   on_change=lambda mode: self._update_mode(mode.value))

            self.control = [0, 0]
            ui.joystick(color='blue', size=50,
                        on_move=lambda e: self._update_control(e.x, e.y),
                        on_end=lambda _: self._update_control(0, 0))
            self.label_control = ui.label('0, 0')

    def _start_robot(self):
        self.bot.start()
        ui.notify('start')

    def _update_control(self, x, y):
        self.label_control.set_text(f"{x * 100:.3f}, {y * 100:.3f}")
        self.control = [x, y]
        # bot.drive_direct(lft, rht)
        self.bot.drive_direct(int(x * 100), int(y * 100))

    def _update_mode(self, value):
        match self.mode_dict[value]:
            case "stop":
                self.bot.stop()
                ui.notify('stop')
            case "passive":
                self.bot.power()
                ui.notify('passive')
            case "safe":
                self.bot.safe()
                ui.notify('safe')
            case "full":
                self.bot.full()
                ui.notify('full')
