# Frappe-Test
A simple "Inventory Management Web Application"

# Table of Content
+ [About](#description)
+ [Getting Started](#getting_started)
+ [File Structure](#file_structure)
+ [Contributing](#contributing)
+ [Author](#authors)
+ [Screenshots](#screens)

## About<a name="description"></a>
+ A web application using Flask framework to manage inventory of a list of products in respective warehouses.
+ Consists of various locations and products, the user can add/edit/delete these locations and products. The user will also be able to import products, export products and move products from one location to another location.
+ The Client side is build using Vue.js and the Server is build using Python-Flask, using a restfull architecture.


## Getting Started<a name="getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

Installing VueJs
```
$ npm install -g @vue/cli
```
Installing Flask
```
$ pip install Flask
```
Installing mysql dependency
```
$ pip install mysql-connector
```
### Installing

A step by step series of examples that tell you how to get a development env running

Cloning the repo
```
$ git clone https://github.com/caldenrodrigues/Frappe-Test.git
```
Installing the dependencies
```
$ cd web/frappe/
$ npm install
```
If you are running a development environment, use the following command:
```
$ npm run serve 
```
If you are running a deployment environment, use the following command:
```
$ npm run build
```

Running the server
```
$ python server.py
```
The application will now be running on https://localhost:8080/ <br>
and Flask will be serving on https://localhost:5000/

## Built With<a name="built_with"></a>
+ [VueJs](https://vuejs.org/) - Web Framework
+ [Flask](http://flask.palletsprojects.com/en/1.1.x/) - Server Framework
+ [MySQL](https://dev.mysql.com/doc/) - Database

## File Structure <a name="file_structure"></a>
/server.py  : Main server code <br>
/web/frappe  : Website code <br>

## Contributing<a name="contributing"></a>

1. Fork it (<https://github.com/caldenrodrigues/Frappe-Test/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Author<a name="authors"></a>

+ [Calden Rodrigues](https://github.com/caldenrodrigues) <br>

## Screenshots<a name="screens"></a>
## Products
![Product](https://i.imgur.com/AHb1MRA.png)
## Locations
![Location](https://i.imgur.com/AjEu1jJ.png)
## Product Movement
![Product Movement](https://i.imgur.com/6mhu8Ys.png)
## Move Product
![Move Product](https://i.imgur.com/w70YSgZ.png)
