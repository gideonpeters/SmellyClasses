# ClassEval: Manually-Crafted Benchmark on Class-level Code Generation

ClassEval is the first class-level code generation benchmark described in the paper "ClassEval: A Manually-Crafted Benchmark
for Evaluating LLMs on Class-level Code Generation". 

## Benchmark Dataset

We manually build ClassEval of 100 class-level Python coding tasks, consists of 100 classes and 412 methods, and average 33.1 test cases per class.

For 100 class-level tasks, diversity is maintained by encompassing these tasks over a wide spectrum of topics， including *Management Systems*, *Data Formatting*, *Mathematical Operations*, *Game Development*, *File Handing*, *Database Operations* and *Natural Language Processing*.

For 412 methods, these have been constructed with diverse dependencies, including (i) *Library Dependency*, where the methods rely on specific external libraries; (ii) *Field Dependency*, in which the methods are contingent on class instance variables, or fields; (iii) *Method Dependency*, where the methods are dependent on other methods within the same class; and (iv) *Standalone*, wherein the methods operate independently without reliance on fields, other methods, or external libraries. 

## Benchmark Format

ClassEval has been meticulously structured and saved in the JSON format, accessible at [ClassEval Data](https://github.com/FudanSELab/ClassEval/blob/master/data/ClassEval_data.json). The specific data fields for each task are delineated as follows:"

* task_id: the unique identifier for each task.

* skeleton: the class skeleton, including all input descriptions in our class-level coding tasks. 

* test: all test cases for the whole class.

* solution_code: the ground-truth class-level code for each task.

Moreover, we have extracted more fine-grained class-level information from the class skeleton, including:

* import_statement: the import statements for each task.

* class_name: the name of the class.

* class_description: a concise description of the purpose and functionality of the class.

* class_constructor: the constructor of the class.

* fields: the fields defined in the class_constructor.

In addition, to facilitate the assessment and generation of method-level code, we also provide detailed information for each method in the "methods_info" field, including:

* method_name: the method signature.

* method_input: the method contract design, including all input descriptions in the method.

* test_code: the test cases for the method.

* solution_code: the ground-truth method-level code.

* dependencies: the dependency information of the method.

## Generation Strategies

For class-level code generation tasks, we devise three distinct generation strategies as follows:

**Holistic Generation**: the model is asked to generate the entire class all at once with the class skeleton as inputs. 

**Incremental Generation**: the model is asked to generate the class in a method-by-method manner. Each iteration is based on the method bodies that have been generated in previous iterations. The iterative process repeats until all methods in the class are generated.  

**Compositional Generation**: the model is asked to generate the class in a method-by-method manner. Each iteration is independent, without considering the other generated methods. All the generated methods are assembled to form the class lastly.

The holistic generation strategy evaluates the model ability of handling long and complicated coding tasks all at once, while the incremental and compositional generation strategies focus on step-by-step class completion. The incremental strategy simulates progressive software development, where developers incrementally implement current methods based on existing ones. In constrast, the compositional strategy simulates real-world programming scenarios, where developers implement current methods based on other available method signatures.
