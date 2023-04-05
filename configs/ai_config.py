import yaml
from ..SystemData.prompting import load_prompt



# function first_run() is called when the system is running for the first time.
# it prints a welcome msg to the user and also takes the user's name and role as input.

def first_run():
    print("Welcome to ALFIE, the Automated Legal Framework for Intelligent Engagement.")
    print("This is the first time you are running the system.")
    print("Please enter your name and role.")
    print("Your name: ", end="")
    name = input()
    print("Your role: ", end="")
    role = input()
    print("Thank you. You are now ready to run the system.")
    print("Please run the system again to start the game.")
    return (name, role)

class AIConfig:
    def __init__(self, ai_name="", ai_role="", ai_goals=[]):
        self.ai_name = ai_name
        self.ai_role = ai_role
        self.ai_goals = ai_goals

    # Soon this will go in a folder where it remembers more stuff about the run(s)
    SAVE_FILE = "last_run_ai_settings.yaml"

    @classmethod
    def load(cls, config_file=SAVE_FILE):
        # Load variables from yaml file if it exists
        try:
            with open(config_file) as file:
                config_params = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            config_params = {}

        ai_name = config_params.get("ai_name", "")
        ai_role = config_params.get("ai_role", "")
        ai_goals = config_params.get("ai_goals", [])

        return cls(ai_name, ai_role, ai_goals)

    def save(self, config_file=SAVE_FILE):
        config = {"ai_name": self.ai_name, "ai_role": self.ai_role, "ai_goals": self.ai_goals}
        with open(config_file, "w") as file:
            yaml.dump(config, file)

    def construct_full_prompt(self):
        prompt_start = """Your decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies with no legal complications."""

        # Construct full prompt
        full_prompt = f"You are {self.ai_name}, {self.ai_role}\n{prompt_start}\n\nGOALS:\n\n"
        for i, goal in enumerate(self.ai_goals):
            full_prompt += f"{i+1}. {goal}\n"

        full_prompt += f"\n\n{load_prompt()}"
        return full_prompt