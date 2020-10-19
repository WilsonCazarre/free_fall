# Free Fall -  A SR Tracking tool for Overwatch Players

### How to run this project

1 - Clone the repository:
```
https://github.com/WilsonCazarre/free_fall.git
```

2 - Navigate to the repository root:
```
cd free_fall
```

3 - Create a python virtual env
```
python3.8 -m venv venv
```

4 - Activate the venv
```
source venv/bin/activate
```

5 - Install the dependencies
```
pip install -r requirements.txt
```

6 - Run the schema migrations
```
python manage.py migrate
```

7 - Run the data migrations
```
python manage.py loaddata initial_data/Heroes.json
python manage.py loaddata initial_data/Maps.json
```

8 - Start the server
```
python manage.py runserver
```

