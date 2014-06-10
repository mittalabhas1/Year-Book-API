# Year-Book-API

An Year Book API made on using Django Rest Framework

## Download and Setup the project

- Clone the files in a directory. `$ git clone https://github.com/mittalabhas1/Year-Book-API`
- Setup the virtual environment. `$ virtualenv env`
- Activate the env `$ source /env/bin/activate`
- Run the pip install script `$ pip install -r requirements.txt`
- Run the server `$ python manage.py runserver`

## Running the API

- Open `http://localhost:8000/users/`
- The default username: `macchi` and password: `qwerty`
- Create users from `http://localhost:8000/admin/`
- Add questions

## Accessing the API

- List of the users: `http://localhost:8000/users`
- Details of a particular users along with the answers given by him: `http://localhost:8000/users/USER_ID`
- List of question: `http://localhost:8000/question`
- Answers of a question: `http://localhost:8000/question/QUESTION_ID`
- Answers of a question by a user: `http://localhost:8000/question/QUESTION_ID/user/USER_ID`