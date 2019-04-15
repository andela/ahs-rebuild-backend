from django.db import models
from django.conf import settings

class Course(models.Model):
    """
    Model to create courses which learners can access
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    #create_by: To be added later
    #reviewed_by: To be added later

    def __str__(self):
        return "{}".format(self.title)



class Module(models.Model):
    """
    Model to create the modules which will belong to a particular course
    """
    module_title = models.CharField(max_length=50)
    description = models.TextField()
    body = models.TextField()
    date_created = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #create_by: To be added later
    #reviewed_by: To be added later

    def __str__(self):
        return "{}".format(self.module_title)