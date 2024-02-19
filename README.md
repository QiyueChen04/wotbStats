# wotbStats
A website made using ReactJS and Django that filters and compares tank statistics.

The [database](db.sqlite3) contains 5 tables storing the tanks' statistics and are linked using tank_id and module_id. The database is [populated](/expapi/views.py) by information obtained from the offical [Wargaming Api](https://developers.wargaming.net/reference/na/wot/account/list/?language=en). 

<img width="500" alt="Screenshot 2024-02-19 at 1 29 41 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/b675026b-5db0-4fa0-b232-c9a41b2dd739">
<img width="500" alt="Screenshot 2024-02-19 at 1 30 36 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/dee8d3c7-0ef5-4b92-ab2c-21e87b744736">

The Django backend handels any get or posts requests, performs the necessary database functions and return the results in json format ([views.py](api/views.py)). 

<img width="1440" alt="Screenshot 2024-02-19 at 1 44 53 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/d18afc46-9970-4e15-9ee6-92c06ae36646">

The [React frontend](frontend/src/pages/Compare.js) allows users to filter tanks by name, type and tier. The selected tanks will be displayed together in the table below. 

<img width="1440" alt="Screenshot 2024-02-19 at 1 22 10 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/a3239753-f736-48ee-877f-7a69c9367fa8">
<img width="1440" alt="Screenshot 2024-02-19 at 1 23 04 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/8697ff51-2be0-4f86-a322-c1b151acb677">
<img width="1440" alt="Screenshot 2024-02-19 at 1 23 39 PM" src="https://github.com/QiyueChen04/wotbStats/assets/116856703/89aa7a38-0765-4aeb-9a7f-2acf5b35004e">
