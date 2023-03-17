"""_summary_
"""


from typing import Dict
from nicegui import ui, app

from  pycreate2 import Create2

from tabs.control_tab import ControlTab
from tabs.sensors_tab import SensorTab
from tabs.docs_tab import DocsTab

# define roomba 

port = "/dev/ttyS0"
bot = Create2(port)


# define interface folders
app.add_static_files('/images', 'guicreate2/images')


with ui.header().classes(replace='row items-center') as header:
    with ui.tabs() as tabs:
        ui.tab('control', icon='smart_toy')
        ui.tab('sensors', icon='sensors')
        ui.tab('docs',    icon='description')

with ui.tab_panels(tabs, value='control'):
    with ui.tab_panel('control'):
        ControlTab(bot)
    with ui.tab_panel('sensors'):
        SensorTab(bot)
    with ui.tab_panel('docs'):
        DocsTab("test")

with ui.footer(value=False) as footer:
    ui.label('V0.0.0')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle).props('fab icon=contact_support')

ui.run()
