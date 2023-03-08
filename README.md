# gender-detection
Machine Learning model that detects the gender and age of a person from an image of their face. 

## Installation instructions

**Note :** Suggested python version is 3.9

- Create virtual environment.
```
python3 -m venv venv
```
- Install requirements.
```
pip intsall -r requirements.txt
```
- Download Dataset.

**Note :** API key can be obtained from the 'Account' tab of your user profile [https://www.kaggle.com/<username>/account]and select 'Create API Token'. This will trigger the download of kaggle.json, a file containing your API credentials.
```
export KAGGLE_USERNAME=<your-kaggle-username>
```
```
export KAGGLE_KEY=<your-kaggle-api-key>
```
```
kaggle datasets download -d jangedoo/utkface-new
```
- Unzip the dataset.
- Use `gender-detection-train.ipynb` to train the model.

**Note :** Skip the above step if you wish to use the weights I provided.

- Run the app.
```
python app.py
```





