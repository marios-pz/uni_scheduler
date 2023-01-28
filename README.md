# DEPRECATED
  UPDATING THE SCHEDULE MANUALLY IS TEDIOUS AND REQUIRES MAINTAINING AND THERE IS NO SOURCE FOR AUTOMATION
  WE WILL WORK ON A DIFFERENT BUT SIMILAR PROJECT NAMED ECLASS-UTILS

## Uniwa Scheduler

setup guide:

* `go to uni_scheduler directory`
* `pip install -r requirements.txt`

-- To use the CLI --

* `python3 cli.py`

<br />

-- To host the webapp --

- `cd /webapp/`
- `python3 server.py` # port has been changed to 99

-- To host the app under docker --

- `docker pull mariospapaz/uni_scheduler:1.0`
- `docker run -d -p 99:99 mariospapaz/uni_scheduler:1.0`

DISCLAIMER: Both Applications are in Greek

WEBAPP: <br />
![web](https://user-images.githubusercontent.com/30930688/164054158-c6cf78a6-412d-446f-a969-667c0d6cb52b.png) <br />

CLI: <br />
![cli](https://user-images.githubusercontent.com/30930688/164053519-81df953a-e42b-4932-934a-cce4b5d9073c.png) <br />

DATABASE USED: <br />
![mongodb](https://webimages.mongodb.com/_com_assets/cms/kuzt9r42or1fxvlq2-Meta_Generic.png) <br />
