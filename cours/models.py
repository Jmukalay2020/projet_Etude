from django.db import models

# Create your models here.


class Cours:
    def __init__(self,name_c,name_p):
        self.name_c = name_c
        self.name_p = name_p