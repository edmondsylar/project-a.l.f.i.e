# this file is going to act as a controller for the terminal display.

from rich.console import Console
from rich.table import Table
from time import sleep
from rich.spinner import Spinner
import time

class ResponseEngine:
    def __init__(self):
        self.console = Console()
    
    def display(self, data, output_type):
        if output_type == 'table':
            self.display_table(data)
        elif output_type == 'text':
            self.display_text(data)
        else:
            self.console.print(f"Unknown output type: {output_type}")
    
    # display tables
    def display_table(self, data):
        table = Table()
        for header in data[0].keys():
            table.add_column(header)
        for row in data:
            table.add_row(*row.values())
        self.console.print(table)
    
    # display text
    def display_text(self, data):
        for item in data:
            self.console.print(item)

    # create a rule.
    def rule(self, content):
        self.console.rule(f"{content}")

    
    # function to show system booting up simple spinner.
    def _loading(self, msg):
        console = Console()
        with console.status(f"[bold green] {msg}") as status:
            for i in range(10):
                time.sleep(1)
                status.update(f"[bold green] {msg} {i+1}0%") 

