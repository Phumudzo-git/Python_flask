## Getting started
1. Create a working directory
```
$ mkdir <work-directory>
$ cd <work-directory>
```
## Create a virtual environment
2. Copy the requirements.txt file into your working directory and then create a virtual environment by running the following commands
```
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```
The requirements.txt file contains flask-restful and geopy packages. Geopy package will be used to calculate distance between latitude and longitude coordinates.
## Run the app.py file
3. Run the following command
```
$ python app.py
```
Below will be the output after running the code above:

invalid json: Expecting value: line 1 column 1 (char 0)
invalid json: Expecting value: line 1 column 1 (char 0)
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
invalid json: Expecting value: line 1 column 1 (char 0)
invalid json: Expecting value: line 1 column 1 (char 0)
 * Debugger is active!
 * Debugger PIN: 266-016-902

The application can be accessed by going into the   http://127.0.0.1:5000/  address shown  above from the output. By going into the address http://127.0.0.1:5000/all_distance/ and entering random numbers for the latitude and longitude coorinates as follows,

```  
http://127.0.0.1:5000/all_distance/12.23,23.54
```
After entering the latitude and longitude numbers, the data.json page will appear ordered in distance, the distance will be in kilometres. To get the maximum distance from the data.json enter the url address,
```
http://127.0.0.1:5000/max_distance/12.23,23.54
```
then the data with the highest distance will appear.
