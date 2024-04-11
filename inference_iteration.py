from openai import OpenAI

import os
import re
from time import sleep
import pandas as pd
import random
import difflib
import json
import csv
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

api_key = "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"
client = OpenAI(api_key=api_key)


class Programmer:
    def program(self, code: str) -> str:
        #Programmer's main method. Takes a processed python file and returns a logged file.
        #Should be implemented by child classes.
        raise NotImplementedError()

class PythonProgrammer(Programmer):
    def __init__(
            self,
            model: str,
            temperature: float,
            max_tokens: int,

    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    
    def program(self, file_name: int, code:str, messages: str) -> str:
        # Program a code snippet for the given question

        prompt = self._generate_prompt(code=code, messages=messages)
        response = self._chatgpt_response_with_backoff(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        print("Response: ", response)

        #sleep for 1 or 2 seconds to avoid hitting the rate limit
        sleep(random.uniform(1, 2))

        response_content = ""

        try:
            #check reason for completition - if not "stop" then log error (stop means completed successfully)
            finish_reason = response.choices[0].finish_reason
            print("Finish reason: " + finish_reason)
            if finish_reason != 'stop':
                self._log_error(file_name, finish_reason)

            else:
                print(response.choices[0].message.content)
                response_content = response.choices[0].message.content
        except:
            self._log_error(file_name, "No finish reason")
        
        return response.choices[0].message.content

    # exponential backoff decorator for the ChatGPT API call
    # source: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_handle_rate_limits.ipynb
    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(4))
    def _chatgpt_response_with_backoff(self, **kwargs):
        return client.chat.completions.create(**kwargs)

    def _read_python_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    def _write_to_python_file(self, file_path, text):
        with open(file_path, 'w') as file:
            file.write(text)

    #CHANGE YOUR PROMPT HERE
    def _generate_prompt(self, code=None, messages=None):

        prompt = f""" You are an expert Python developer.
                    You will receive a class that has one or multiple code smells.
                    These are the list of smells: ```{messages}```
                    This is the class snippet: ```{code}```
                    Return the complete class with the code smells fixed."""

        print(prompt)
        return prompt

    def _log_error(self, code_id: int, finish_reason: str):
        # Log the question ID for which the code generation failed
        error_file_path = os.path.join(os.getcwd(), "error_log.txt")

        with open(error_file_path, 'a') as file:
            file.write(f"{code_id}, {finish_reason}\n")

if __name__ == "__main__":
    
    # #CHANGE PARAMS AS NEEDED. 
    # file_path = "test.py"

    programmer = PythonProgrammer('gpt-3.5-turbo', 0, 3019)
    # python_code = programmer._read_python_file(file_path)
    # print(python_code)

    # #prompt = programmer._generate_prompt(python_code)

    # output = programmer.program(1, python_code)

    # result_path = "results.py"

    # programmer._write_to_python_file(result_path, output)
    # print(f"Text written to '{result_path}' successfully.")

    # print(output)

    # with open("category_counts.csv", 'r') as file:
    #     content = file.read()

    # findings = preliminary code smells analysis - findings
    filename = "findings.csv"

    df = pd.read_csv(filename)
    grouped = df.groupby('project')
    for group_name, group_data in grouped:
        print(f"Group Name: {group_name}")
        print(group_data)
        messages = ""
        for index, row in group_data.iterrows():
            messages += row['code_smell'] + "\n"
        print(messages)

        python_code = programmer._read_python_file("output/generation/pys/" + group_name + ".py")
        output = programmer.program(group_name, python_code, messages)
        programmer._write_to_python_file("output/fix_code_smells/" + group_name + ".py", output)

print("Text files created successfully.")
