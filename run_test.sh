#!/bin/bash

$PWD/python3-virtualenv/bin/python -m unittest discover -v tests/

curl --request GET http://127.0.0.1:5000//api/timeline_post

curl --request POST http://127.0.0.1:5000//api/timeline_post -d 'name=Conrad&email=cuyakonwu@mlh.io&content=Just Added Database to my portfolio site!'

curl --request DELETE http://127.0.0.1:5000/api/timeline_post/1
