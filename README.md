# How to run
```
git clone https://github.com/techiehkr/django_curd_rest_with_jwt.git
cd django_curd_rest_with_jwt 
cd restdjagnocurd
pip3 install -r requirement.txt
cd curd_rest_django
```


>get token
http://127.0.0.1:8000/api/token/
####request:POST
####json body
{"username":"test","password":"User@1234"}
[Responds]:
{
  "refresh": "***",
  "access": "***"
}

Get Data
>get Items
http://127.0.0.1:8000/api/items/
####request:GET
####Header
>Authorization: Bearer <access from token>
Content-Type: application/json

