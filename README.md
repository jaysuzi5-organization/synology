# Documentation for synology
### fastAPI: API to wrap CRUD operations for the synology Postgres table.  This table will be used to store statistics on the Synology NAS


This application has two generic endpoints:

| Method | URL Pattern           | Description             |
|--------|-----------------------|--------------------|
| GET    | /api/v1/synology/info         | Basic description of the application and container     |
| GET    | /api/v1/synology/health    | Health check endpoint     |



## CRUD Endpoints:
| Method | URL Pattern           | Description             | Example             |
|--------|-----------------------|--------------------|---------------------|
| GET    | /api/v1/synology         | List all synology     | /api/v1/synology       |
| GET    | /api/v1/synology/{id}    | Get synology by ID     | /api/v1/synology/42    |
| POST   | /api/v1/synology         | Create new synology    | /api/v1/synology       |
| PUT    | /api/v1/synology/{id}    | Update synology (full) | /api/v1/synology/42    |
| PATCH  | /api/v1/synology/{id}    | Update synology (partial) | /api/v1/synology/42 |
| DELETE | /api/v1/synology/{id}    | Delete synology        | /api/v1/synology/42    |


### Access the info endpoint
http://home.dev.com/api/v1/synology/info

### View test page
http://home.dev.com/synology/test/synology.html

### Swagger:
http://home.dev.com/api/v1/synology/docs