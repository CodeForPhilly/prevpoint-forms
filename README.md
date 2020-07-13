# prevpoint-forms

This project is to design a piece of software to record information from scanned forms for Prevention Point. This project utilizes openCV and the Microsoft Azure API. Please contact the project lead on slack on how to get access the API key. 


## Main Project Parts

### 1. Form Intake Interface

There are several different types of forms that need to be scanned. The form intake interface should allow the user to select which type of form is being scanned. 

### 2. Rotate and Rescale Forms 

In order for the bounding box section of the project to work. The images for each form need to be in the same orientation and scale. The current thinking is to use the prevention point logo on each page to orient and scale. 

### 3. Create Proper Bounding Boxes to Collect Data from the Forms  

For each of the forms bounding boxes need to be created around text fields and marks. The collected data should be deposited in a csv that corresponds to the variables in the variable dictionary for that form. 

#### Text Fields 

- Text fields use the Microsoft Azure Read API

#### Mark Fields

- Mark fields use openCV to determine if a box is marked. 


### 4. Flagging System 

The client (Prevention Point) has flagged "Name" and "UniqueID" as the fields that need the most accurate information. The Microsoft Azure Read API returns a certainty number. If the certainty number is below a certain threshold. The software should display the form and a field that allows for manual entry and correction. 

# Installation

Before installing you must install python3, python-virtualenv, node, and yarn. If you have trouble installing these, feel free to reach out to @chriscauley on the slack.

```
# install packages, this will need to be re-run if requirements.txt or package.json is changed
./bin/install

# create a superuser for viewing data in admin (follow prompts)
python manage.py createsuperuser
```

# Usage and Development

Start the server

```
./bin/develop
```

This will start the django server and the node compiler in the same terminal. Navigate to http://localhost:8000 and select form type. Upload an image. Currently the image processing isn't hooked up, so step 3 (processing) is skipped and a blank form is shown.