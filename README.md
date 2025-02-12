# Data Science / Machine Learning Portfolio

Repository containing a portfolio of data science projects done by me for self-learning and hobby purposes. Each mini project is presented via Jupyter Notebook and associated Python scripts.

_Note: Data used in the projects (accessed under data directory) is for demonstration purposes only._

## Instructions for Running Python Notebooks Locally

1. Create an isolated custom environment (recommended - see instructions below)
2. Install dependencies using requirements.txt.
3. Run notebooks as usual by using a jupyter notebook server, Vscode etc.

## Contents

This portolio consists of several directories:

- `projects` folder contains various stand-alone microprojects I've been working on during my learning journey
- `notebooks` folder contains several Jupyter Notebooks, each of which addresses specific area of interest, topic or skillset.
- `data` folder contains some commonly used datasets that are used for demo purposes.

### Micro Projects

- Bike Sharing Demand Forecast utilizing Autogluon
- Training and Deploying Image Classifier on AWS
- Disaster Message Classifier

> **Skills & Tools:** building API, fast api, Javasript, CSS, AWS (Sagemaker, Lambda, Step Functions)

### Notebooks

#### 1. Data Analysis and Visualization

> **Skills & Tools:** Pandas, Matplotlib, Seaborn, Plotly, Folium

#### 2. Statistical Simulations, Regression Analysis

> **Skills & Tools:** A/B Testing, T-tests

#### 3. Machine Learning

> **Skills & Tools:** Supervised Algorithms (Linear Regression, Logistic Regression, Deep Learning, RNN) Unsupervised Algorithms (Clustering), Reinforcement Learning.

#### 4. Natural Languaage Processing

> **Skills & Tools:** spacy, nltk, NLP feature engineering, transformers

#### 5. Big Data

> **Skills & Tools:** PySpark, Hadoops

#### 6. Optimization

> **Skills & Tools:** Linear/Non-linear Programming, Integer Programming, PuLP library

#### 7. Cloud Technology Stacks

> **Skills & Tools:** AWS Sagemaker, Azure Machine Learning

#### 8. Miscellaneous

> **Skills & Tools:** Causal Inference, Code optimization using JIT

## Create environments

### Mac
If using Mac OS, you may use the following shell script to setup your custom environment:

```
brew install pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile

pyenv install 3.8.10
pyenv virtualenv 3.8.10 env-3.8.10

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv activate env-3.8.10
pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name env-3.8.10
```

### Windows
If using Windows OS, you may use the following Powershell script to setup your custom environment:

```
python -m venv my_env
./my_env/Scripts/activate

python -m pip install --upgrade pip 
python -m pip install -r requirements.txt --trusted-host=objects.githubusercontent.com  --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org 
python -m pip install -e .
python -m ipykernel install --user --name my_env
```

---

If you want to have a chat with me about the portfolio, work opportunities, or collaboration, send me an email at narmina.yadullayeva@gmail.com.
