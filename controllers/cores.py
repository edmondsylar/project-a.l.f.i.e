
from config import Config
import json
import random
import commands as cmd
import memory as mem
import data
import chat
from colorama import Fore, Style
from spinner import Spinner
import time
import speak
from enum import Enum, auto
import sys
from config import Config
from json_parser import fix_and_parse_json
from ai_config import AIConfig
import traceback
import yaml
import argparse
from terminal_display import display

cfg = Config()

def parse_arguments():
    global cfg
    cfg.set_continuous_mode(False)
    cfg.set_speak_mode(False)
    
    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument('--continuous', action='store_true', help='Enable Continuous Mode')
    parser.add_argument('--speak', action='store_true', help='Enable Speak Mode')
    parser.add_argument('--debug', action='store_true', help='Enable Debug Mode')
    parser.add_argument('--gpt3only', action='store_true', help='Enable GPT3.5 Only Mode')
    args = parser.parse_args()

    if args.continuous:
        print_to_console("Continuous Mode: ", Fore.RED, "ENABLED")
        print_to_console(
            "WARNING: ",
            Fore.RED,
            "Continuous mode is not recommended. It is potentially dangerous and may cause your AI to run forever or carry out actions you would not usually authorise. Use at your own risk.")
        cfg.set_continuous_mode(True)

    if args.speak:
        print_to_console("Speak Mode: ", Fore.GREEN, "ENABLED")
        cfg.set_speak_mode(True)

    if args.gpt3only:
        print_to_console("GPT3.5 Only Mode: ", Fore.GREEN, "ENABLED")
        cfg.set_smart_llm_model(cfg.fast_llm_model)

def construct_prompt():
    config = AIConfig.load()
    if config.ai_name:
        print_to_console(
            f"Welcome back! ",
            Fore.GREEN,
            f"Would you like me to return to being {config.ai_name}?",
            speak_text=True)
        should_continue = input(f"""Continue with the last settings? 
Name:  {config.ai_name}
Role:  {config.ai_role}
Goals: {config.ai_goals}  
Continue (y/n): """)
        if should_continue.lower() == "n":
            config = AIConfig()

    if not config.ai_name:         
        config = prompt_user()
        config.save()

    # Get rid of this global:
    global ai_name
    ai_name = config.ai_name
    
    full_prompt = config.construct_full_prompt()
    return full_prompt
