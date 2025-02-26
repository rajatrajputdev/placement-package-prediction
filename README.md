# Predicting Placement Package using Machine Learning

A small Linear Regression-based model for predicting the placement package of a student based on a historical data of a tier 3 college. This project covers data analysis, model training, and deployment using Streamlit for easy interaction.

Specially handcrafted for GDG Amity's Build with AI Cohort -> [Link](https://gdgamity.tech)

## Demo
![demo_image](https://raw.githubusercontent.com/rajatrajputdev/placement-package-prediction/refs/heads/main/resources/demonstration.png)

## Features
- **Linear Regression Model:** A simple yet effective approach to predicting customer spending.
- **Jupyter Notebook:** Contains code for data analysis, model training, and evaluation.
- **Streamlit App:** Provides an interactive UI to input customer data and get predictions.
- **Deployment Ready:** Can be hosted on cloud platforms like Heroku or Streamlit Sharing.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Jupyter Notebook
- Streamlit

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/rajatrajputdev/placement-package-prediction.git
   cd placement-package-prediction
   ```
2. Install dependencies:
   ```sh
    pip install scikit-learn pandas numpy seaborn matplotlib streamlit
   ```
3. Run the Jupyter Notebook to explore the dataset and train the model:
   ```sh
   jupyter notebook
   ```
   Open `placement-prediction.ipynb` and execute the cells.

## How to Use?
1. Train the Linear Regression model by running `placement-prediction.ipynb`.
2. Start the Streamlit app:
   ```sh
   streamlit run deployed-model.py
   ```
3. Enter customer details in the UI and get predictions on yearly spending.

## Dataset
The dataset contains student-related features such as:
- CGPA
- Package Secured(in LPA)

These features help predict the yearly spending of a customer.

## Model
We use **Linear Regression**, a simple yet powerful algorithm, to predict yearly cost spending based on customer features. The model is trained using `scikit-learn` and evaluated for accuracy.

## Deployment
This project is deployed using:
- **Streamlit Sharing:** Quick and easy deployment.

## Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License.

**Free and Open Source Software with Open Source Hardware, Hell Yeah!**
