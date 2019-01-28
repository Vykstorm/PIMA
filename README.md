## Introduction

This repository contains multiple esimators created by different machine learning techniques to solve the binary classification
problem on Pima Indians diabetes.
Data can be downloaded here: https://www.kaggle.com/uciml/pima-indians-diabetes-database

Python language is used in conjunction with numpy, sklearn, scipy stack and keras (to build neuronal networks)


## Build & Run

You need to install python >= 3.7 on your system as well as anaconda
Then, go to the directory where you downloaded this repository and run the next command
in order to satisfy all needed dependencies to execute the programs
```
conda env create -f environment.yml
```

Activate the environment with:
```
conda activate pima
```

Finally create a jupyter's notebook with the next command:
```
cd estimators
jupyter notebook
```

A new page will be opened in your web browser. A few scripts will be avaliable.
Each of them will create an specific estimator to solve the pima diabetes classification
problem.
