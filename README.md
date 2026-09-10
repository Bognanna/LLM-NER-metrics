# Evaluation metrics for large language models in a named entity extraction task

This repository is connected to the master's thesis in which I introduce the CDEF metric. It contains implementation of the CDEF metric as well as two component measures: CDE and EF. 

## Description
CDEF is a metric for evaluating performance of LLMs in a NER task. It incorporates embeddings of entities in order to measure semantic similarity between lists of generated and reference (gold) entities.

The notebooks section contains three Jupyter notebooks:
- `test_on_benchmark.ipynb` in which I performed tests of the metric on 3 benchmarks. The results of these tests I discuss in the master's thesis.
- `test_on_use_cases.ipynb` in which I show, through particular examples, how the metric behaves. The description of these use cases can be found in the master's thesis.
- `tutorial.ipynb` in which I present step by step how to use the functions implemented in this project in order to calculate CDEF.

## Installation
I haven't prepared a sophisticated installation method. If you want to run notebooks or use the implemented metric, just clone the repository, ensure all libraries listed in `requirements.txt` are installed, and that you have Ollama running locally on your computer.

## Usage

For usage instructions, see `tutorial.ipynb`.

## License

[MIT](https://choosealicense.com/licenses/mit/)