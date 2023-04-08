# this is the main A.L.F.I.E entry point
# A.L.F.I.E (Artificial Life Form Interactive Entity)
from rich.prompt import Prompt
import os
from controllers.terminal_display import display
from SystemData.systemThreads import system_threds
from controllers.config import Config
from controllers.cores import parse_arguments

# create trigger function (command_panel) that adds items to the system_threads list.
# we are going to use multi threading to run the system threads.

def command_panel(user_prompt):
    # create a list of system threads.
    system_threds.append(user_prompt)



parse_arguments()
ai_name = ""
prompt = construct_prompt()
# print(prompt)
# Initialize variables
full_message_history = []
result = None
# Make a constant:
user_input = "Determine which next command to use, and respond using the format specified above:"