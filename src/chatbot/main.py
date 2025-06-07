#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from chatbot.crew import Chatbot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.

    """
    i = 0 
    while(True):
        i += 1
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        try:
            inputs = {
                'question': user_input,
                'current_year': str(datetime.now().year),
                'i': i
            }
            Chatbot().crew().kickoff(inputs=inputs)
        except Exception as e:
            print(f"An error occurred: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "question": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Chatbot().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Chatbot().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "question": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Chatbot().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
