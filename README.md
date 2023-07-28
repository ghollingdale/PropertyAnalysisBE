# PropertyAnalysisBE: A predictive model for calculating a house price in Belgium
### *A George Hollingdale project written in Python 3.11*
# About the repository
This repository contains a price prediction model for a property in Belgium. After data cleaning, the model has been based on a final data set of 3,950 properties scraped from [ImmoWeb](https://www.immoweb.be/en).

# Project context
I am a junior scientist at BEcode and this is my first fully pipelined prediction-modeling project. I started this project with about one month's prior programming experience. The main purpose of the project was to *explore* and *learn* a host of new Python libaries, functions and extensions, as well as many core aspects of data science, whilst building a functioning prediction model. 

It should go without saying, the journey was *far* more important than the destination!


# What to expect
In this respository you can expect to find:
* The [core property data](data/properties.csv) I previously scraped from ImmoWeb on 05/07/2023.
* Subsequently [cleaned data set](data/cleaned_output.csv).
* Some notebooks containing:
  * The [data cleaning process](model-building/1_Data_modeling_cleaning.ipynb)
  * Some [brief analysis](notebooks/data_analysis.ipynb)
   * The [output graphs](assets) of the analysis
  * Some exploration of differing [prediction models (files 2 & 3)](/model-building/)
* A [final model](/model-building/4_data_modeling_model.ipynb)
* A [working API](app.py) for predicting a house price using my model
* My [source code](src)


The model is far from perfect, but it has served as a useful tool for me to learn from, and there are many, *many*, things that I'd do differently in my next project.
### Libraries learned
Some libraries I encountered are:
* `requests`
* `pandas`
* `numpy`
* `sklearn`
* `matplotlib`
* `pickle`


# Installation
The model is not deployed to the web at this time, but you can fork the repo and test it locally on your machine.

This project is written in [Python 3.11](https://www.python.org/downloads/) and it is recommended that you install this version to ensure everything works as it should.

You will also want to install the necessary libaries for this project by running, in your chosen environment, the following code in your terminal.

> pip install -r requirements.txt

# Usage
 To activate the API you should naviagate to the repositories directory in your terminal and enter:

> uvicorn app:app --reload

This will load the app locally. You can now test the app by navigating to [docs](http://127.0.0.1:8000/docs).
From here you can select `POST /pricepredict`, press the `try it out` button, and enter your input into the `json` code.
Each variable is taken as either binary or a float. The binary inputs use `1` for a positive response and `0` for negative. 

```json
{
  "number_of_bedrooms": float,
  "living_area": float,
  "fully_equipped_kitchen": binary,
  "furnished": binary,
  "terrace": binary,
  "garden": binary,
  "total_property_area": float,
  "total_land_area": float,
  "swimming_pool": binary,
  "state_of_the_building": binary
}
```
# Timeline
This project had a timline of 12 days, 5 of which were spent on analysis, four on regression and modeling three on deployment.

# Contributors
I am the sole contributor to this analysis project. You can find my github profile [here](https://github.com/ghollingdale).

The data for this project was scraped in collaboration with [Bo Cao](https://github.com/Spike815) and [Sacha Schreuer](https://github.com/sachinovitch). You can find the repository for the scraping [here](https://github.com/Spike815/Immo_Scraping).
