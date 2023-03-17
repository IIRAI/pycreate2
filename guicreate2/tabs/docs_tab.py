"""
"""


from nicegui import ui
from nicegui.events import MouseEventArguments


class DocsTab:

    def __init__(self, name: str):
        with open('guicreate2/docs/docs_page.md', 'r') as file:
            docs = file.read()
            ui.markdown(docs)
