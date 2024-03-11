# wotbStats
A website made using MySQL, Django, and ReactJS that filters and compares tank statistics.

The MySQL database contains 8 tables storing the statistics of over 500 tanks and 2500 modules, which are linked using tank_id and module_id in junction tables. The database is populated with statistics obtained from the offical [Wargaming Api](https://developers.wargaming.net/reference/na/wot/account/list/?language=en). 

<img width="500" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/264c1a38-b9a3-4470-bb64-f65aa6c000fb">
<img width="500" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/d1eb90ff-a17e-42c6-8aaa-878ba1ec55bf">

The Django backend handels any get or posts requests, performs the necessary database functions and return the results in json format ([views.py](api/views.py)). 

<img width="1440" alt="Screenshot 2024-03-10 at 9 20 49 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/42264fd1-9caa-49fd-9228-42616b4245f8">

The [React frontend](frontend/src) allows users to filter tanks by name, type and tier. The selected tanks will be displayed together in the table below. 

<img width="1440" alt="Screenshot 2024-03-10 at 9 22 12 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/7512c282-a0c1-4cae-ac6a-47b5e17be46b">
<img width="1440" alt="Screenshot 2024-03-10 at 9 25 35 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/2eb1b854-be97-4e8a-8209-d18acb878c09">
<img width="1440" alt="Screenshot 2024-03-10 at 9 26 27 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/e4a35a67-db4a-4829-98b4-bb8e64e9f3ca">
