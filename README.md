# Predicting Heart Disease Using Machine Learning

This project demonstrates a machine learning workflow for predicting the presence of heart disease using tabular patient data.

## Project Overview

The notebook performs the following steps:
- Exploratory data analysis (EDA) with summary statistics and visualizations
- Data preparation and splitting into training and test sets
- Training and comparing multiple classification models:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Random Forest
- Hyperparameter tuning using `RandomizedSearchCV` and `GridSearchCV`
- Model evaluation with metrics including accuracy, ROC/AUC, confusion matrix, precision, recall, and F1-score
- Feature importance analysis for model interpretation

## Files

- `notebook/hd.ipynb` - main Jupyter notebook containing the full analysis and model training pipeline
- `data/heart-disease.csv` - dataset used for training and evaluation

## Dataset

The dataset includes medical attributes for patients and a binary target column named `target` indicating heart disease presence.

## Dependencies

The notebook uses standard Python data science libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

If you do not already have these installed, you can install them with pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## How to Run

1. Open `notebook/hd.ipynb` in Jupyter Notebook or JupyterLab.
2. Verify the dataset path is correct: `../data/heart-disease.csv`.
3. Run the notebook cells sequentially to reproduce the analysis and model results.

## What You Can Learn

- How to inspect and visualize medical dataset features
- How to prepare data for supervised learning
- How to train and compare classification models
- How to tune hyperparameters for better model performance
- How to evaluate models using multiple metrics
- How to interpret feature importance

## Notes

This project is intended for learning and experimentation with machine learning for heart disease prediction. The notebook is self-contained and is the primary entry point for understanding the workflow.
