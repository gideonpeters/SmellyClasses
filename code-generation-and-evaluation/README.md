# SMELLY CLASSES: ANALYZING CODE SMELLS FOR CLASS-LEVEL CODE GENERATION.

This project investigates code smells in class-level code generation by GPT3.5-turbo, to do this, we make use of ClassEval. ClassEval is the first class-level code generation benchmark described in the paper ["ClassEval: A Manually-Crafted Benchmark
for Evaluating LLMs on Class-level Code Generation"](http://arxiv.org/abs/2308.01861). 

## Benchmark Dataset

We forked part of this repository from the [ClassEval repo](https://github.com/FudanSELab/ClassEval). 

Previous work has manually built ClassEval of 100 class-level Python coding tasks, consists of 100 classes and 412 methods, and average 33.1 test cases per class.

For 100 class-level tasks, diversity is maintained by encompassing these tasks over a wide spectrum of topics, including *Management Systems*, *Data Formatting*, *Mathematical Operations*, *Game Development*, *File Handing*, *Database Operations* and *Natural Language Processing*.

For 412 methods, they have been constructed with diverse dependencies, including (i) *Library Dependency*, where the methods rely on specific external libraries; (ii) *Field Dependency*, in which the methods are contingent on class instance variables, or fields; (iii) *Method Dependency*, where the methods are dependent on other methods within the same class; and (iv) *Standalone*, wherein the methods operate independently without reliance on fields, other methods, or external libraries. 

## Benchmark Format

ClassEval has been meticulously structured and saved in the JSON format, accessible at [ClassEval Data](https://github.com/gideonpeters/SmellyClasses/blob/main/code-generation-and-evaluation/data/ClassEval_data.json). The specific data fields for each task are delineated as follows:

* task_id: the unique identifier for each task.

* skeleton: the class skeleton, including all input descriptions in our class-level coding tasks. 

* test: all test cases for the whole class.

* solution_code: the ground-truth class-level code for each task.

More fine-grained class-level information from the class skeleton, including:

* import_statement: the import statements for each task.

* class_name: the name of the class.

* class_description: a concise description of the purpose and functionality of the class.

* class_constructor: the whole constructor of the class.

* fields: the fields defined in the class_constructor.

Detailed information for each method in the "methods_info" field, including:

* method_name: the method signature.

* method_input: the method contract design, including all input descriptions in the method.

* test_code: the test cases for the method.

* solution_code: the ground-truth method-level code.

* dependencies: the dependency information of the method.

For more details in benchmark construction, go [here](https://github.com/FudanSELab/ClassEval/blob/master/data/README.md).

For the comparison of the inputs for the ClassEval, HumanEval, and MBPP benchmarks go [here](https://github.com/FudanSELab/ClassEval?tab=readme-ov-file#benchmark-format)

## Implementation

We implement the ClassEval for code generation using greedy sampling, where only one single solution code sample is generated for each task using greedy decoding, i.e., setting the “do_sample” hyperparameter to false (with a temperature of 0).

## Results

### Overall Correctness

The following figure shows the class-level and method-level Pass@1 with greedy sampling of studied LLMs on ClassEval and HumanEval:

<img src="output\images\C_pass1_bar.png" alt="C_pass1_bar" style="zoom: 29%;" />

The following table presents the class-level and method-level Pass@k
with nucleus sampling on ClassEval:

<img src="output\images\pass@k.png" alt="pass@k" style="zoom: 50%;" />

Notably, we only present the best class-level Pass@1 (and corresponding method-level Pass@1) for each model among the three generation strategies.


## Usage

Ensure you're using the right setup and following the proper directory structure to seamlessly evaluate class-level code generation this tool.

### 🛠️ Setup

1. Environment Setup

Ensure you're running Python 3.8 or newer. We recommend setting up a virtual environment:
```
$ conda create -n classeval python=3.8
$ conda activate classeval
```

2. Repository Setup

Clone the repository and install necessary dependencies:
```
$ git clone https://github.com/gideonpeters/SmellyClasses
$ cd code-generation-and-evaluation
$ pip install -e ClassEval
```

### 📁 Data & Output Structure
**Data**: Ensure `ClassEval_data.json` is placed in the `data` directory

**Model Outputs**: Keep all model-generated outputs in `output/model_output`. These outputs should be in JSON format, with predictions under the `predict` key, pointing to the list of generated code samples.

**Iterative prompting **: `inference_iteration.py` is the script that handles grouping the code smells in our dataset by class, and prompting GPT for a solution.

### 🔍 Deep Dives
**Class-Level Code Generation**: Dive into the ClassEval implementation details [here](https://github.com/FudanSELab/ClassEval/blob/master/generation).

**Evaluation Process**: Explore in-depth [here](https://github.com/FudanSELab/ClassEval/blob/master/classeval_evaluation).

