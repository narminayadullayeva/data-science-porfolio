# Data Science Portfolio

Repository containing portfolio of data science projects done by me for self-learning and hobby purposes. Each mini project is presented via Jupyter Notebook and associated Python scripts.

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

- ### Micro Projects
  - Bike Sharing Demand Forecast utilizing Autogluon
  - Disaster Message Classifier 

Skills & Tools:
* Building API, 
* fast api
* Javasript
* CSS

- ### Notebooks
- #### 1. Data Analysis and Visualization
Skills & Tools: Pandas, Matplotlib, Seaborn, Plotly, Folium
- #### 2. Statistical Simulations, Regression Analysis
Skills & Tools: A/B Testing, T-tests
- #### 3. Machine Learning
Skills & Tools:
* Deep Learning
* Linear Regression, Logistic Regression
* RNN
* Reinforcement Learning
- #### 4. Natural Languaage Processing
Skills & Tools:
* spacy 
* NLP feature engineering 
* Transformers 
- #### 5. Big Data
Skills & Tools:
* PySpark
* Hadoops
- #### 6. Optimization 
- #### 7. Cloud Stacks (AWS Sagemaker, Azure ML)
- #### 8. Miscellaneous


---

If you want to have a chat with me about the portfolio, work opportunities, or collaboration, send me an email at narmina.yadullayeva@gmail.com.



## Create environments

- If using Mac, you may use the following shell script to setup your custom environment:

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