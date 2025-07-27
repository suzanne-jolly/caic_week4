# caic_week4
# Tweet Generator and Like Predictor

This is a web application that generates tweets for a selected company and predicts how many likes the tweet might get. It uses a machine learning model trained on a dataset of tweets.

## Project Structure
Tweet-Generator-With-Like-Prediction/
├── backend/
│   ├── tweet_generator.py
│   ├── like_predictor_api.py
│   ├── like_predictor.pkl
│   ├── company_encoder.pkl
│   ├── app_generator.py
│   
├── frontend/
│   └── test1.py
├── requirements.txt
├── README.md
└── training/ (colab)
    └── Week1_EDA_Cleanup.ipynb (in week1 repository); file to be updated soon



## Features

- Frontend form that accepts user inputs like company, tweet type, and message
- Generates a tweet based on the selected options
- Predicts likes using a trained machine learning model
- Displays both the generated tweet and predicted number of likes

## Technologies Used

- Python (Flask for backend)
- Streamlit (for frontend)
- XGBoost Regressor (for predicting likes)
- Pandas and NumPy (for data handling)

## How to Run the Project Locally

1. Clone the repository
  
3. Set up a virtual environment:

4. Install dependencies:

5. Start the Flask server:

6. Open `test1.py` using the command; "streamlit run test1.py" in command terminal in your browser.

## Machine Learning Model

- The model is trained using XGBoost Regressor.
- Features used: word count, character count, sentiment score, presence of media, hour of the day, day of the week, and company.
- Target: log-transformed like counts.
- The model file is saved as `like_predictor.pkl`.

## Week 4 Progress

- Completed a working frontend that takes inputs
- Connected frontend to backend `/generate` and `/predict` APIs
- Generated tweets and predicted likes based on user input
- All features integrated and functional

