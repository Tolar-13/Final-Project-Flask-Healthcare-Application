
# Income Analysis Survey - Flask Application

## Overview

This project is a web-based survey tool developed using Flask, Python, and MongoDB to collect and analyze user data related to income spending. The data collected is intended to be used for a new product launch in the healthcare industry. The application is designed to be aesthetically pleasing and user-friendly, with error handling implemented to ensure smooth user interaction. The collected data is stored in a MongoDB database and processed in Python to generate insights, which are then visualized for further analysis.

## Features

- **Web Development with Flask**: 
  - A web application with a title "Income Analysis Survey".
  - A user-friendly survey form titled "Income Survey Form".
  - Form includes fields for Age, Gender, Total Income, and Expenses, with checkboxes for various expense categories (utilities, entertainment, school fees, shopping, healthcare).
  - Includes error handling and a "Thank you for your submission" message upon successful form submission.

- **Data Storage with MongoDB**: 
  - User data including Age, Gender, Total Income, and Expenses are stored in a MongoDB database.
  - Each expense category has an associated textbox for the user to input the amount spent.

- **Data Processing with Python**:
  - A Python class named `User` is developed for processing the collected data.
  - Collected data is looped through and stored in a CSV file (`survey_data.csv`).
  - The CSV file is loaded into a Jupyter notebook for further analysis.

- **Data Visualization**:
  - Data is cleaned and analyzed to remove duplicates, handle missing values, and correct data entry errors.
  - Statistical analysis is performed, and visualizations are generated:
    - Ages with the highest income.
    - Gender distribution across spending categories.
  - Visualizations are saved as images for inclusion in client presentations.

- **Deployment on Heroku**:
  - The Flask application is hosted on Heroku, making it accessible online.

## Project Structure

```
Final-Project-Flask-Healthcare-Application/
├── Procfile                            # Heroku deployment file
├── ages_highest_income.png             # Visualization of ages with highest income
├── app.py                              # Main Flask application file
├── flask_survey.ipynb                  # Jupyter notebook for data processing and visualization
├── gender_spending_barplot.png         # Visualization of gender distribution across spending categories
├── requirements.txt                    # List of Python dependencies
├── survey_data.csv                     # CSV file containing collected survey data
└── templates/
    ├── index.html                      # HTML template for the survey form
    └── thank_you.html                  # HTML template for the thank you page
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Final-Project-Flask-Healthcare-Application
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**:
   - Ensure you have a MongoDB server running.
   - Update the MongoDB connection string in `app.py` to match your MongoDB configuration.

5. **Run the Flask application**:
   ```bash
   python app.py
   ```

6. **Deploy on Heroku**:
   - Follow the [Heroku deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy the application.

## Usage

- Access the survey form at `http://localhost:5000/` or your Heroku app URL.
- Fill in the required details and submit the form.
- The submitted data is stored in MongoDB and processed by the Python script.
- Visualizations can be viewed and further analyzed using the provided Jupyter notebook (`flask_survey.ipynb`).

## Data Analysis & Visualization

The Jupyter notebook (`flask_survey.ipynb`) provides the following insights:

1. **Data Cleaning**:
   - Duplicate entries removed.
   - Missing values handled.
   - Data normalized and entry errors corrected.

2. **Statistical Analysis**:
   - Ages with the highest income.
   - Gender distribution across various spending categories.

3. **Visualizations**:
   - `ages_highest_income.png`: Bar chart showing ages with the highest income.
   - `gender_spending_barplot.png`: Bar chart showing gender distribution across spending categories.

## Contributing

If you wish to contribute to this project, please fork the repository and create a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Flask documentation: https://flask.palletsprojects.com/
- MongoDB documentation: https://docs.mongodb.com/
- Heroku documentation: https://devcenter.heroku.com/
