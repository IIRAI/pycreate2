"""

Sensor list:

    - 'bumps_wheeldrops',
    - 'wall',
    - 'cliff_left',
    - 'cliff_front_left',
    - 'cliff_front_right',
    - 'cliff_right',
    - 'virtual_wall',
    - 'overcurrents',
    - 'dirt_detect',
    - 'ir_opcode',
    - 'buttons',
    - 'distance',
    - 'angle',
    - 'charger_state',
    - 'voltage',
    - 'current',
    - 'temperature',
    - 'battery_charge',
    - 'battery_capacity',
    - 'wall_signal',
    - 'cliff_left_signal',
    - 'cliff_front_left_signal',
    - 'cliff_front_right_signal',
    - 'cliff_right_signal',
    - 'charger_available',
    - 'open_interface_mode',
    - 'song_number',
    - 'song_playing',
    - 'oi_stream_num_packets',
    - 'velocity',
    - 'radius',
    - 'velocity_right',
    - 'velocity_left',
    - 'encoder_counts_left',
    - 'encoder_counts_right',
    - 'light_bumper',
    - 'light_bumper_left',
    - 'light_bumper_front_left',
    - 'light_bumper_center_left',
    - 'light_bumper_center_right',
    - 'light_bumper_front_right',
    - 'light_bumper_right',
    - 'ir_opcode_left',
    - 'ir_opcode_right',
    - 'left_motor_current',
    - 'right_motor_current',
    - 'main_brush_current',
    - 'side_brush_current',
    - 'statis'
"""


from nicegui import ui
from  pycreate2 import Create2


class SensorTab:

    def __init__(self, bot: Create2):

        ui.markdown('''### Roomba sensors''')

        self.bot = bot
        self.s = self.bot.get_sensors()

        t = ui.timer(interval=1, callback=lambda: self.update())
        ui.checkbox('read sensors').bind_value(t, 'active')

        ui.markdown('''#### general data''')
        self.grid_general = ui.aggrid({
            'columnDefs': [
                {'headerName': 'sensor', 'field': 'sensor'},
                {'headerName': 'value',  'field': 'value'},
                {'headerName': 'unit',  'field': 'unit'},
            ],
            'rowData': [
                {'sensor': 'open_interface_mode',   'value': self.open_interface_mode(self.s.open_interface_mode), 'unit': '-'},
                {'sensor': 'dirt_detect',           'value': self.s.dirt_detect,           'unit': '-'},
                {'sensor': 'ir_opcode',             'value': self.s.ir_opcode,             'unit': '-'},
                {'sensor': 'buttons',               'value': self.s.buttons,               'unit': '-'},
                {'sensor': 'song_number',           'value': self.s.song_number,           'unit': '-'},
                {'sensor': 'song_playing',          'value': self.s.song_playing,          'unit': '-'},
                {'sensor': 'oi_stream_num_packets', 'value': self.s.oi_stream_num_packets, 'unit': '-'},
                {'sensor': 'ir_opcode_left',        'value': self.s.ir_opcode_left,        'unit': '-'},
                {'sensor': 'ir_opcode_right',       'value': self.s.ir_opcode_right,       'unit': '-'},
                {'sensor': 'stasis',                'value': self.s.stasis,                'unit': '-'},
            ],
            'rowSelection': 'multiple',
        }).style('width:600px; height:330px')

        ui.markdown('''#### robot state''')
        self.grid_robot_state = ui.aggrid({
            'columnDefs': [
                {'headerName': 'sensor', 'field': 'sensor'},
                {'headerName': 'value',  'field': 'value'},
                {'headerName': 'unit',  'field': 'unit'},
            ],
            'rowData': [
                {'sensor': 'distance',             'value': self.s.distance,             'unit': 'mm'},
                {'sensor': 'angle',                'value': self.s.angle,                'unit': 'degrees'},
                {'sensor': 'velocity',             'value': self.s.velocity,             'unit': 'mm/s'},
                {'sensor': 'radius',               'value': self.s.radius,               'unit': 'mm'},
                {'sensor': 'velocity_right',       'value': self.s.velocity_right,       'unit': 'mm/s'},
                {'sensor': 'velocity_left',        'value': self.s.velocity_left,        'unit': 'mm/s'},
                {'sensor': 'encoder_counts_left',  'value': self.s.encoder_counts_left,  'unit': 'tick'},
                {'sensor': 'encoder_counts_right', 'value': self.s.encoder_counts_right, 'unit': 'tick'},
            ],
            'rowSelection': 'multiple',
        }).style('width:600px; height:270px')

        ui.markdown('''#### obstacle data''')
        self.grid_obstacle = ui.aggrid({
            'columnDefs': [
                {'headerName': 'sensor', 'field': 'sensor'},
                {'headerName': 'value',  'field': 'value'},
                {'headerName': 'unit',  'field': 'unit'},
            ],
            'rowData': [
                {'sensor': 'bumps_wheeldrops',          'value': self.s.bumps_wheeldrops,          'unit': '-'},
                {'sensor': 'wall_signal',               'value': self.s.wall_signal,               'unit': '-'},
                {'sensor': 'wall',                      'value': self.s.wall,                      'unit': 'bool'},
                {'sensor': 'cliff_left',                'value': self.s.cliff_left,                'unit': 'bool'},
                {'sensor': 'cliff_front_left',          'value': self.s.cliff_front_left,          'unit': 'bool'},
                {'sensor': 'cliff_front_right',         'value': self.s.cliff_front_right,         'unit': 'bool'},
                {'sensor': 'cliff_right',               'value': self.s.cliff_right,               'unit': 'bool'},
                {'sensor': 'cliff_left_signal',         'value': self.s.cliff_left_signal,         'unit': '-'},
                {'sensor': 'cliff_front_left_signal',   'value': self.s.cliff_front_left_signal,   'unit': '-'},
                {'sensor': 'cliff_front_right_signal',  'value': self.s.cliff_front_right_signal,  'unit': '-'},
                {'sensor': 'cliff_right_signal',        'value': self.s.cliff_right_signal,        'unit': '-'},
                {'sensor': 'light_bumper',              'value': self.s.light_bumper,              'unit': '-'},
                {'sensor': 'light_bumper_left',         'value': self.s.light_bumper_left,         'unit': '-'},
                {'sensor': 'light_bumper_front_left',   'value': self.s.light_bumper_front_left,   'unit': '-'},
                {'sensor': 'light_bumper_center_left',  'value': self.s.light_bumper_center_left,  'unit': '-'},
                {'sensor': 'light_bumper_center_right', 'value': self.s.light_bumper_center_right, 'unit': '-'},
                {'sensor': 'light_bumper_front_right',  'value': self.s.light_bumper_front_right,  'unit': '-'},
                {'sensor': 'light_bumper_right',        'value': self.s.light_bumper_right,        'unit': '-'},
                {'sensor': 'virtual_wall',              'value': self.s.virtual_wall,              'unit': 'bool'},
            ],
            'rowSelection': 'multiple',
        }).style('width:600px; height:570px')

        ui.markdown('''#### battery state''')
        self.grid_battery = ui.aggrid({
            'columnDefs': [
                {'headerName': 'sensor', 'field': 'sensor'},
                {'headerName': 'value',  'field': 'value'},
                {'headerName': 'unit',  'field': 'unit'},
            ],
            'rowData': [
                {'sensor': 'charger_state',       'value': self.charge_state(self.s.charger_state), 'unit': '-'},
                {'sensor': 'voltage',             'value': self.s.voltage,             'unit': 'mV'},
                {'sensor': 'current',             'value': self.s.current,             'unit': 'mA'},
                {'sensor': 'temperature',         'value': self.s.temperature,         'unit': 'deg C'},
                {'sensor': 'battery_charge',      'value': self.s.battery_charge,      'unit': 'mAh'},
                {'sensor': 'battery_capacity',    'value': self.s.battery_capacity,    'unit': 'mAh'},
                {'sensor': 'charger_available',   'value': self.charger_available_state(self.s.charger_available),   'unit': '-'},
                {'sensor': 'left_motor_current',  'value': self.s.left_motor_current,  'unit': 'mA'},
                {'sensor': 'right_motor_current', 'value': self.s.right_motor_current, 'unit': 'mA'},
                {'sensor': 'main_brush_current',  'value': self.s.main_brush_current,  'unit': 'mA'},
                {'sensor': 'side_brush_current',  'value': self.s.side_brush_current,  'unit': 'mA'},
                {'sensor': 'overcurrents',        'value': self.s.overcurrents,        'unit': 'xxx'},
            ],
            'rowSelection': 'multiple',
        }).style('width:600px; height:370px')

    def update(self):
        self.s = self.bot.get_sensors()
        self.grid_general.update()
        self.grid_robot_state.update()
        self.grid_obstacle.update()
        self.grid_battery.update()

    def open_interface_mode(self, value):
        match value:
            case 0:
                return "off"
            case 1:
                return "passive"
            case 2:
                return "safe"
            case 3:
                return "full"
            
    def charge_state(self, value):
        match value:
            case 0:
                return "not charging"
            case 1:
                return "reconditioning charging"
            case 2:
                return "full charging"
            case 3:
                return "trickle charging"
            case 4:
                return "waiting"
            case 5:
                return "charging fault condition"
            
    def wheel_drops_state(self, value):
        msg = ""
        if value & 1:
            msg += "bump right; "
        if value & 2:
            msg += "bump left; "
        if value & 4:
            msg += "wheel drop right; "
        if value & 8:
            msg += "wheel drop left; "
        if msg == "":
            msg += "-"
        return msg

    def charger_available_state(self, value):
        """return the state of the available charger

        The value is decoded from the bit value of the OI.  
        The first bit is reserved for the internal charger,
        the second bit is reserved for the home base.

        Args:
            value (uint): value between 0 and 3

        Returns:
            string: meaning of the value
        """
        match value:
            case 0:
                return "nothing available"
            case 1:
                return "internal charger"
            case 2:
                return "home base"
            case 3:
                return "home base and internal charger"

    def overcurrent_state(self, value):
        msg = ""
        if value & 1:
            msg += "side brush; "
        if value & 4:
            msg += "main brush; "
        if value & 8:
            msg += "right wheel; "
        if value & 16:
            msg += "left wheel; "
        if msg == "":
            msg += "-"
        return msg
