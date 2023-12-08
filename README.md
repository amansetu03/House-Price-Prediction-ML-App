# House Price Prediction ML App

This repository contains code for a Machine Learning (ML) application that predicts house prices. It utilizes a Python-based Flask API for the backend and integrates with an Android app for a user-friendly interface.

## Overview

The project aims to create a house price prediction system. It employs a machine learning model trained on housing data with a Flask API serving predictions. The Android app interacts with this API, enabling users to input house features and receive price estimates.

## Features

- Predicts house prices based on provided features.
- RESTful API built with Flask for handling prediction requests.
- Android app interface for easy user interaction.

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/amansetu03/House-Price-Prediction-ML-App.git
    cd house-price-prediction-ml-app
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the Flask API:**
    ```
    python app.py
    ```

4. **Launch the Android app on an emulator or device.**

## Usage

After setting up the project, you can:

- Access the Flask API endpoints to make house price predictions.
- Utilize the Android app to input house features and obtain price predictions.

## API Endpoints

- `POST /predict`: Endpoint for making house price predictions. Requires input parameters for house features.

Example request:
```json
{
    "loc": "banjara layout",
    "sqft": 1000,
    "bath": 2,
    "bhk": 2
}

```
Example response: in lakh
```json
{
    "Price": 47.81
}
```



<img src="https://github.com/amansetu03/House-Price-Prediction-ML-App/assets/106844274/68f5c988-b87f-4dc4-ae1b-27e31721e8a8" style="width:30%; float:left; margin:35px;">
<img src="https://github.com/amansetu03/House-Price-Prediction-ML-App/assets/106844274/5053e165-bc5d-4170-9d20-f585029475f2" style="width:30%; float:left; margin:35px;">
