# Container Logistics Dashboard
Data visualisation dashboard in the context of containerlogistics. Open dataset of automatically generated measurements by a large carrier.


### Description
* Shows a timeseries development of  temperature and humidity in sea containers (on container level)
* Usecase: Reviewing development and alert to exceeding values
* Options for further extension: 
 * Container selection
 * Could potentially be fed with real-time data import
 * Automatic alert in case of values exceeding customer-selected threshold 

### Implementation
The project was implemented using the following python modules
* dash: Wrapper for plotly graph objects
* plotly: Interactive graphs
* pandas: Data management

### Data
The underlying open dataset can be found here: https://data.deutschebahn.com/dataset/data-sensordaten-schenker-seefrachtcontainer.html

### Instructions
Run from console with 

~~~
python .\container_dashboard_app_v3.py
~~~

Start the dashboard in a browser of your choice by navigating to 
~~~
localhost:8050/
~~~


