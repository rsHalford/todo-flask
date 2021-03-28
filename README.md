### TODO JSON API

Created using Flask to connect clients to a server database, to perform CRUD operations with a Todo Application.


---

#### Setup w/Authentication

Create a file named api_access.py in root folder.
```sh
$ touch api_access.py
```

Then add the following varialbes with your own values. Remembering to surround them in quotations.
```py
USERNAME="username"
PASSWORD="password"
```

> NB: Authentication is simply setup for single user/admin client access. As personal todo apps don't usually have multiple users authorised for the same list.
