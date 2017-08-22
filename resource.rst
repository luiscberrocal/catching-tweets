Supervisor for uwsgi


Tests
-------
@anabalica

https://speakerdeck.com/anabalica/djangocon-us-testing-in-django


--parallel
--tag
--exclude-tag

self.subTest()

SimpleTestCase
    No database

Hypothesis

Coverage is desceptive

Mutation testing
    mutpy

Tips

MD5PasswordHasher
SimpleTestCase
setUpTestData()
mocks are for isolation
Dont create a database object if youd dont need use build() or stub() from FactoryBoy


Serverless Django
-------------------
API Gatewar

Zappa

1 request = 1 server

Zero load balancing

Event driven arquitecture


For database use RDS or EC2

zappa-django-utils

Lighning Talks
---------------

Fix myDjango
+++++++++++++

pip install fixmydjango

6 - 11 octubre pycon Brazil


The Zen of DJango
++++++++++++++++++

@pizzapanther

pip-save

Ptrack
+++++++

django-ptrack

Tracking Pixel

Does not support python 3

Non locking migrations
++++++++++++++++++++++++

For MySQL

10 year app
++++++++++++

django registrations

Did not like this

wrds databases
++++++++++++++++

wharton wrds

postgres 1.5 tb per month

wagtail cms

UTF
-----
pip install emojificate

🌲

🌲

End to En Django on Kubernetes
------------------------------

@fwiles

kops

Patroni for Postresql. https://github.com/zalando/patroni

Files in Django
----------------

django-storage

whitenoise

CDN in front of a s3 for media.

16-ago-2017
------------

GraphQL in the Wild
---------------------
Arianne Dee

Github
pip install graphene_django

Graphene is not being updated.

Need to extend graphene to authorization.

DOS

    #. Whitelist for allowed queries
    #. Maximum limit
    #. Maximum query cost

Linters
----------
https://docs.google.com/presentation/d/1ccYOC1O1asGIbE62-pKFKlBRvkdu2sd2WQGCpSSiGC8/edit#slide=id.p

@flaviojuvenal

mangage.py check

dodgy library
pycodestyle
abstract syntax tree
flake8
import ast
pyflake

pylint astroid

mypy

pre-commit.com writen in Python

bandit -r .

prospector

Denormalized query engine design pattern
-------------------------------------------

Simon Willlison

http://lanyrd.com/2017/djangocon/sftkxk/


elasticsearch

Dilithium mysql


Practical Testing
------------

Daniel Davis DjangoCon 2015 youtube

@WayneMerry1

The beauty viewsets
---------------------

Buddy Lindsey, Jr.

ListAPICreateView filter_backends

RetrieveUpdateDestroyAPIView


Celery Tasks
--------------

@xima

vinta.com.br/playbook

tapioca Facebook

idempotent and atomic

https://www.vinta.com.br/playbook/

https://docs.google.com/presentation/d/1Ao0S3Z-VRn_pcT5T4mXIhv3t3liQ3ZrwqaGeDqz9XCQ/edit#slide=id.g1fc007b8dd_0_12

https://github.com/infernojs/inferno