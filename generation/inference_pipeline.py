import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, AutoModel
import json
from time import sleep
import random
from tqdm import tqdm
from inference_util import InferenceUtil, ModelName, GenerationStrategy
import os
import openai

class InferencePipeline:

    def __init__(self, args):
        with open(args.data_path, 'r', encoding = 'utf-8') as f:
            self.file_cont = json.load(f)
        self.greedy = args.greedy
        self.output_path = args.output_path
        self.output_path_2 = args.output_path_2
        self.cuda = "cuda"
        if args.cuda is not None:
            os.environ["CUDA_VISIBLE_DEVICES"] = ','.join([str(i) for i in args.cuda])
        self.generation_strategy = args.generation_strategy
        self.model_name = args.model
        self.checkpoint = args.checkpoint
        self.temperature = args.temperature
        self.max_length = args.max_length
        self.openai_key = args.openai_key
        self.openai_base = args.openai_base
        self.google_api_key = args.google_api_key

        self.get_model_tokenizer_and_config()
        self.SAMPLE_NUMS = 1 if self.greedy == 1 else args.sample
        self.do_sample = False if self.greedy == 1 else True

    def get_model_tokenizer_and_config(self):
        if self.model_name == ModelName.GPT_3_5.value or self.model_name == ModelName.GPT_4.value:
            return
   
    def save_result(self, result):
        with open(self.output_path, 'w', encoding = 'utf-8') as f:
            json.dump(result, f, indent=4)

    def save_result_as_files(self, result, filename):
        with open(self.output_path_2 + '/' + filename, 'w', encoding = 'utf-8') as f:
            f.write(result)

    def model_generate(self, prompt):
        if self.model_name == ModelName.GPT_3_5.value or self.model_name == ModelName.GPT_4.value:
            openai.api_key = self.openai_key
            openai.api_base = self.openai_base
            if self.model_name == ModelName.GPT_3_5.value:
                response = openai.ChatCompletion.create(
                    max_tokens=self.max_length,
                    temperature=0 if self.greedy == 1 else self.temperature,
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert Python Programmer."},
                        {"role": "user", "content": prompt}
                    ]
                )

                sleep(random.uniform(1, 2))
            
            outputs = response.choices[0]["message"]["content"]
            return outputs

    def construct_prompt(self, strategy, info):
        prompt = ""
        if strategy == GenerationStrategy.Holistic:
            if self.model_name == ModelName.PolyCoder.value or self.model_name == ModelName.SantaCoder.value:
                skeleton = info['skeleton']
                prompt = skeleton
            else:
                class_name = info['class_name']
                skeleton = info['skeleton']
                test = info['test']
                # instruction = f""" Provided below is an instruction detailing a task.
                #             Compose a response that aptly fulfills the request. 
                #             The class contains a class description and each method contains a method description
                #             taking all of that into consideration complete the entire class with the described logic

                #             Please complete the class {class_name} in the subsequent code.
                # """

                instruction = f""" Provided below are unit tests for the class {class_name}. 
                                Using these tests, generate the code that correctly addresses all unit tests.
                                Return the complete definition of the class."""

                instruction = instruction + '\n' + test


                
                prompt = InferenceUtil.generate_prompt(instruction, self.model_name)

        return prompt

    def post_process(self, result):
        if self.generation_strategy == GenerationStrategy.Incremental.value:
            for cont in result:
                pred = []
                for result in cont['predict']:
                    pred.append(result[-1])
                cont['predict'] = pred
        elif self.generation_strategy == GenerationStrategy.Compositional.value:
            for cont in result:
                cont['raw_output'] = cont['predict'].copy()
            for cont in result:
                cont['predict'] = []
                for raw_output in cont['raw_output']:
                    class_code = '\n'.join(cont['import_statement']) + '\n' + cont['class_constructor']
                    for i in range(len(raw_output)):
                        method_name = cont['methods_info'][i]['method_name']
                        code = raw_output[i]
                        method_code = InferenceUtil.extract_method_code(code, method_name)
                        class_code += '\n\n' + method_code
                    cont['predict'].append(class_code)

    def pipeline(self):
        error_task_id_list = []
        if self.generation_strategy == GenerationStrategy.Holistic.value:
            result = []
            for cont in tqdm(self.file_cont):
                pred = []
                try:
                    prompt = self.construct_prompt(GenerationStrategy.Holistic, cont)
                    for _ in range(self.SAMPLE_NUMS):
                        outputs = self.model_generate(prompt)
                        self.save_result_as_files(outputs[10:-3], 'Task_'+ cont['task_id']+ '__k' + str(_) + '.py')
                        pred.append(outputs)
                    cont['predict'] = pred
                    result.append(cont)
                    self.save_result(result)

                except Exception as e:
                    print(e)
                    print("IDX: ", cont['task_id'])
                    error_task_id_list.append(cont['task_id'])
        else:
            print("Unknown Generation Strategy")
            return
        
        print("error_task_id_list: ", error_task_id_list)
        self.post_process(result)
        self.save_result(result)