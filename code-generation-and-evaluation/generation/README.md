## Generation 
We provide `inference.py` script to to produce class-level code outputs, supporting various models and generation strategies.

Navigate to the generation directory and execute the following command:
```
python inference.py \
--model 8 \
--checkpoint model_path \
--output_path model_output.json \
--output_path_2 ../output/generation/pys \
--greedy 1 \
--data_path ../data/ClassEval_data.json \
--cuda 0 1 \
--generation_strategy 0

```

## Parameter Guide

### Supported Models

Specify the model using the `--model` argument. Each model might have its own unique API.

Supported models:

0: Instruct_CodeGen
1: WizardCoder
2: Instruct_StarCoder
...
8: GPT-3.5
...

For a detailed list of models and their respective identifiers, check the help associated with the `--model` parameter in `inference.py`. To integrate new models, append the appropriate model identifier in `inference.py` and ensure its API is also added.

Currently, we cater to 9 models: Instruct_CodeGen, WizardCoder, Instruct_StarCoder, InCoder, PolyCoder, SantaCoder, Vicuna, ChatGLM, GPT-3.5, and GPT-4. For GPT-3.5 and GPT-4, supply your personal OpenAI key using the `--openai_key` parameter.

For this project, we make use of GPT3.5.

### Sampling Methods

Specify your desired sampling method with the `--greedy` argument:

- 0: Nucleus sampling. 
- 1: Greedy sampling.

For nucleus sampling, ensure you also provide the sample number using the `--sample` argument.

### Generation Strategies
Determine your generation strategy with the `--generation_strategy` argument:

- 0: Holistic Generation
- 1: Incremental Generation
- 2: Compositional Generation

For this project, we make use of the Holisitic Generation. For insights on the practical implementation of these generation strategies, see the `def pipeline` within `inference_pipeline.py`.


### Further Parameters

For a comprehensive overview of all parameters and their valid values, either peruse the `inference.py` script or run with the `--help` flag.

### Additional Documentation

For additional documentation on the code generation pipeline, kindly refer to the [ClassEval Project](https://github.com/FudanSELab/ClassEval/blob/master/generation/README.md)