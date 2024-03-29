# Features
- jinja2 intergration to render dynamic content
- Enabled routing
- Configurable TCP ports
- SSL  Integration
- Url-rewriting/rewiring enabled

Demo
Login screen 


# Built With
- python
- html
- jinja2
- twisted
(back to top)

# Run project locally
-Getting Started
   create a local environment to install the project dependencies listed at requirements.txt
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
- clone this repository git clone https://github.com/myk4040okothogodo/servingSockets.git

- generate a self signed certificate, follow instructions at https://linuxize.com/post/creating-a-self-signed-ssl-certificate/
  save the generated documents at the root folder /keys and remember to point to this documents in       servaScript.py  

- run  python servaScript.py
- go to localhost:8082/login or localhost:8082/register
- go to localhost:8082/data/this/that  for url rewiring/rewrite
- go to localhost:8082/dynamic for dynamic rendering using jinja2
 


# Prerequisites

----------------- -------
- attrs             21.4.0
- Automat           20.2.0
- constantly        15.1.0
- hyperlink         21.0.0
- idna              3.3
- incremental       21.3.0
- Jinja2            3.0.3
- MarkupSafe        2.0.1
- pip               21.3.1
- setuptools        59.6.0
- six               1.16.0
- Twisted           21.7.0
- typing_extensions 4.0.1
- wheel             0.37.1
- zope.interface    5.4.0


# Usage
the project is a demonstatrion of webserver communication using sockets and the rendering of pages Dynamically and statically. With SSL and Jinja2 for rendering html content.
You can change the values in the envars.py that holds the variable values to 

For more examples, please refer to the Documentation

(back to top)

Roadmap
 Feature 1
 Feature 2
 Feature 3
 Nested Feature
See the open issues for a full list of proposed features (and known issues).


# Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

# Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request
- 

# License
Distributed under the MIT License. See LICENSE.txt for more information.

(back to top)

# Contact
Your Name -   myk_okoth - mikeogodo5@gmail.com

Project Link:  https://github.com/myk4040okothogodo/servingSockets

(back to top)

Acknowledgments

