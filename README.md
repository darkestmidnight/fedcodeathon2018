# Viso Verita

Viso Verita is a security automation server which helps make security easy while also more secure. Viso Verita additionally can automatically clock in and out employees to save time and increase accuracy of timesheets.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

#### Windows:
Install Python3 from [https://www.python.org/downloads/](https://www.python.org/downloads/)
**Make sure 'pip' is checked when installing**

Hit Windows Key + r
type cmd then hit enter
then enter the following commands
```
pip install django
pip install mysqlclient
```

#### Ubuntu/Debian:
```
$ sudo apt-get install python3 -y
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
$ pip install -U pip

$ sudo pip install django
$ sudo pip install mysqlclient
```

### Installing

From the Command Prompt, initialize the project.

#### Windows:

```
cd C:\path\to\fedcodathon2018
python manage.py migrate
```

#### Ubuntu/Debian:

```
cd /path/to/fedcodathon2018
python manage.py migrate
```

Now go to a browser and go to http://localhost and there should be a website that looks like this:

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org/) - The programming language
* [Django](https://www.djangoproject.com/) - The web framework
* [Mysql](https://www.mysql.com/) - The database software
* HTML
* Javascript
* CSS

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Cooper Mahring** - *Database/UI Design* - [coopmaster](https://github.com/coopmaster)
* **Hannah West** - *UI Design* - [hannah-west](https://github.com/hannah-west)
* **Elly Richardson** - *Back End Functionality* - [darkestmidnight](https://github.com/darkestmidnight)
* **Parker Milum** - *Video and Presentation* - [coopmaster](https://github.com/coopmaster)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Special thanks to Parker Milum for coming up with our idea!
