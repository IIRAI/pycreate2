
import copy
from nicegui import ui
from  pycreate2 import Create2


class ControlTab:

    def __init__(self, bot: Create2):

        self.bot_width_mm_ = 230
        self.max_lin_speed_mm_ = 250
        self.max_ang_speed_rad_ = 70 * 3.141592 / 180

        self.bot = bot
        self.control = [0, 0]
        self.control_old = [0, 0]
        self._start_robot()

        timer_period = 0.1

        # start, close
        with ui.grid(columns=3).classes('w-full h-full'):
            with ui.card().classes('items-center col-span-1'):
                self.left_joy = ui.joystick(color='blue', size=50,
                            on_move=lambda e: self._update_control_left(e.x),
                            on_end=lambda _: self._update_control_left(0),
                            lockX=True)
                self.left_control = ui.label('0 deg/s')
            with ui.card().classes('items-center col-span-1'):
                ui.button('start', on_click=lambda _: self._start_robot())
                self.mode_dict = {0: 'stop', 1:'passive', 2:'safe', 3:'full'}
                robot_mode = ui.toggle(self.mode_dict, value = 0,
                                       on_change=lambda mode: self._update_mode(mode.value))
            with ui.card().classes('items-center col-span-1'):
                self.right_joy = ui.joystick(color='blue', size=50,
                            on_move=lambda e: self._update_control_right(e.y),
                            on_end=lambda _: self._update_control_right(0),
                            lockY=True)
                self.right_control = ui.label('0 mm/s')

        self.timer = ui.timer(timer_period, self.timer_callback)

    def _start_robot(self):
        self.bot.start()
        ui.notify('start')

    def _update_control_left(self, x):
        speed = - x * self.max_ang_speed_rad_
        self.left_control.set_text(f"{speed * 180 / 3.141592:.0f} deg/s")
        self.control[0] = int(speed)

    def _update_control_right(self, x):
        speed = x * self.max_lin_speed_mm_
        self.right_control.set_text(f"{speed:.0f} mm/s")
        self.control[1] = int(speed)

    def timer_callback(self):
        if self.control != self.control_old:
            self.control_old = copy.deepcopy(self.control)
            right_wheel_speed, left_wheel_speed = self.wheels_speed(self.control[1], self.control[0])
            self.bot.drive_direct(right_wheel_speed, left_wheel_speed)

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

    def wheels_speed(self, linear_speed_mm, angular_speed):
        right_wheel = linear_speed_mm + (angular_speed * self.bot_width_mm_)
        left_wheel  = linear_speed_mm - (angular_speed * self.bot_width_mm_)
        return right_wheel, left_wheel
