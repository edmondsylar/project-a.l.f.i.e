# this is going to be the file to add a function to the system_threads listt.
import threading
import os 
from ..SystemData.systemThreads import system_threds

# import the rendering engine.
from ..controllers.terminal_display import display

# define the worker function.
def worker():
    # using display show alert additino of the functin to the system_threads
    display.display_text(["[bold green] System Thread Added"])
