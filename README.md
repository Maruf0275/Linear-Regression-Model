# Placement Predictor

A Streamlit app that estimates a placement score from a student's CGPA using a
trained scikit-learn linear regression model.

## Run locally

Use Python 3.10 or newer:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run test.py
```

The app opens at `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Open [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
3. Choose **New app**, then select this repository and the `main` branch.
4. Set **Main file path** to `test.py`.
5. Select **Deploy**.

Streamlit Cloud installs the dependencies from `requirements.txt`. Keep
`placement.pkl` in the repository root because it is the model used by the app.

## Project files

- `test.py` - Streamlit application
- `placement.pkl` - trained linear regression model
- `requirements.txt` - pinned runtime dependencies
- `Test.ipynb` - original model loading and prediction experiment