# Stress Predictor

## Overview:
Decision Tree Regressor that predicts a person's stress level on a scale from 1-10 based on health and lifestyle factors. GUI for easy interaction with the Stress Predictor.

## Project Description:
Implemented a Decision Tree Regressor using scikit-learn, considering factors such as gender, age, blood pressure, and sleep quality to predict stress levels. Utilized Tkinter to create a user-friendly GUI where users input their health and lifestyle information and receive the model's stress level prediction.

## To Run:
1. Download and unzip all files into a single folder.
2. Install dependencies: Pandas, Numpy, Scikit-learn, Tkinter.
3. Two versions of the Decision Tree Regressor model are available:
   - `stressModel.py` (originally used in the project, requires a personal SQL database).
   - `stressModelAlt.py` (imports dataset directly, ensure `stressDataset.csv` is in the same folder).
   - Note: In `stressModel.py`, personal database details have been removed for security reasons.

## Demo:
A demo video is included. Please check the "Demo" folder.

## Dependencies:
- Pandas
- Numpy
- Scikit-learn
- Tkinter
- SQL
