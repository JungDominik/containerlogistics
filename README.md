# Container Logistics Dashboard (WIP)
Data visualisation dashboard in the context of containerlogistics. Open dataset of automatically generated measurements by a large carrier.
![image](https://user-images.githubusercontent.com/29613804/222990359-61546f7f-60bf-4740-8570-82cce9c1a39d.png)


### Description
* Shows a timeseries development of  temperature and humidity in sea containers (on container level)
* Usecase: Reviewing development and alert to exceeding values

### Implementation
The project was implemented using the following python modules
* dash: Wrapper for plotly graph objects
* plotly: Interactive graphs
* pandas: Data management
* flask: Webserver and web application management

### Data
The underlying open dataset can be found here: https://data.deutschebahn.com/dataset/data-sensordaten-schenker-seefrachtcontainer.html

### Caveats / Options for further extension

 * Container selection
 * Could potentially be fed with real-time data import
 * Automatic alert in case of values exceeding customer-selected threshold 
 * No handling of outliers / unrealistic data yet. Requires manual data cleaning by the user.

### Instructions
Run from console with 

~~~
python .\container_dashboard_app_v3.py
~~~

Start the dashboard in a browser of your choice by navigating to 
~~~
localhost:8050/
~~~


