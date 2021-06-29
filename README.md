# How to run API

## You have to install all libraries using command (in app folder)
```sh
pip3 install -r requirements-dev.txt 
```
## Run api via command (in app folder)
```sh
python3 -m app.app 
```
## Environment variables

| Env                 | Description                                | Default                                                            |
| ------------------- | ------------------------------------------ | ------------------------------------------------------------------ |
| `DB_NAME`           | name of DB                           | `api`                                                                 |
| `DB_HOST`         | DB_HOST                                 | `localhost`                                                                   |
| `DB_USER`         | DB_USER                                 | `api`                                                                   |
| `DB_PASS`         | DB_PASS                                 | `1234qwe`                                                                   |



## How to view data in API

You need to init data in DB, for this you need to run next command.  
```sh
curl -X POST http://localhost:5000/api/v1/init_data
```
## How to view information for all users
```sh
curl http://localhost:5000/api/v1/users
```
## How to view information about specific user
```sh
curl -i http://localhost:5000/api/v1/users/USER_ID
```
## How to add user to db
```sh
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"USER_NAME", "last_name":"LAST_NAME", "description":"POSITION"}' http://localhost:5000/api/v1/users
```
## How to delete user from db
```sh
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/v1/users/USER_ID
```
# How to change information about specific user
```sh
curl -i -H "Content-Type: application/json" -X PUT -d '{"description":"new_position", "employee": true or false}' http://localhost:5000/api/v1/users/USER_ID
```