# The-Phone-Database

Get the Dataset from Kaggle too:
https://www.kaggle.com/datasets/sanjayramrr/gsm-arena-phones-2023-2016

## Overview

Mobile Phone Price Prediction is a web application that helps users predict the prices of mobile phones based on various features and specifications. The application utilizes a dataset obtained through web scraping from GSMArena, a prominent source of phone specifications and information. Users can input features such as brand, release year, weight, operating system, storage size, screen size, battery capacity, RAM, and camera specifications to predict the price of a mobile phone.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [About the Webpage](#about-the-webpage)
- [About the Project](#about-the-project)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

- **Clone the Repository:**
  ```
  git clone https://github.com/rrsr28/The-Phone-Database
  cd The-Phone-Database
  ```

- **Install Dependencies:**
  ```
  pip install -r requirements.txt
  ```

- **Run the Application:**
  ```
  streamlit run Home.py
  ```

The application should open in your web browser.

## Features

- Predict mobile phone prices based on features.
- User-friendly interface for inputting specifications.
- Utilizes a web-scraped dataset from GSMArena.
- Data visualization for insights.
- About page with project details and references.
- Python-based using Streamlit.

## Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- BeautifulSoup
- Requests
- GSMArena (data source)

## Installation

1. Clone the repository to your local machine.
2. Install the required Python dependencies using `pip` as mentioned in the "Getting Started" section.
3. Run the Streamlit application using the `streamlit run Home.py` command.

## Usage

1. Upon running the application, you will be presented with a user interface for entering mobile phone specifications.
2. Select the brand, release year, weight, operating system, storage size, screen size, battery capacity, RAM, and camera specifications.
3. Click the "Predict" button to predict the price of the mobile phone.
4. The application will display the predicted price and accuracy percentage.

## About the Webpage

The Mobile Phone Price Prediction webpage is designed to help users make informed decisions about mobile phone purchases. Here are some key points about the webpage:

- The webpage provides users with the ability to predict the price of a mobile phone based on its features.
- The dataset used for predictions is sourced from GSMArena, a reliable and extensive database of mobile phone specifications.
- Web scraping has been done using BeautifulSoup to extract data from GSMArena.
- The webpage features an intuitive and user-friendly interface for entering mobile phone specifications.
- Users can select the brand, release year, weight, operating system, storage size, screen size, battery capacity, RAM, and camera specifications.
- Upon clicking the "Predict" button, the webpage calculates and displays the predicted price and accuracy percentage.

## About the Project

The Mobile Phone Price Prediction project is an open-source initiative that aims to provide valuable insights and predictions related to mobile phone prices. Here are some key aspects of the project:

- The dataset used in the project is obtained through web scraping from GSMArena, a renowned online provider of phone information.
- Data cleaning and wrangling have been performed to ensure the dataset's quality and accuracy.
- The project includes a user-friendly web application developed using Streamlit, a Python framework for building data applications.
- Data visualization is an integral part of the project, allowing users to gain insights from the dataset.
- The project is accompanied by an "About" page that provides details about the webpage and references to sources of inspiration.

## References

- [Streamlit Documentation](https://docs.streamlit.io/stable/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [GSMArena](https://www.gsmarena.com/)
