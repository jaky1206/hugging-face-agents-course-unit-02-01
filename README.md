# Hugging Face Agents Course Unit 02-01

- https://huggingface.co/learn/agents-course
- https://github.com/huggingface/agents-course

## Overview


## Conda Environment Setup

### Create a new conda environment
```shell
conda create -n huggingface_agents_course-unit-02-01
```

### Activate the environment
```shell
conda activate huggingface_agents_course-unit-02-01
```

### Export configuration to a file
```shell
conda env export > requirements.yml
```

### Create a new conda environment from the config file
```shell
conda env create -f requirements.yml
```

## Pip Environment Setup

### Create a new virtual environment
```shell
python -m venv huggingface_agents_course-unit-02-01
```

### Activate the environment
- On Windows:
  ```shell
  .\huggingface_agents_course-unit-02-01\Scripts\activate
  ```
- On macOS/Linux:
  ```shell
  source huggingface_agents_course-unit-02-01/bin/activate
  ```

### Install dependencies from a requirements file
1. Create a `requirements.txt` file with your dependencies.
2. Run:
   ```shell
   pip install -r requirements.txt
   ```

### Export the environment configuration to a file
```shell
pip freeze > requirements.txt
```
for pip packages from a conda environment
```
pip list --format=freeze > requirements.txt
```

### Create a new virtual environment and install dependencies from the `requirements.txt` file
1. Create a new virtual environment as shown above.
2. Activate the environment.
3. Run:
   ```shell
   pip install -r requirements.txt
   ```


