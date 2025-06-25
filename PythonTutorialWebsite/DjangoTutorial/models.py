from django.db import models

class Objectives(models.Model):
    objective_description = models.TextField()
    intro = models.TextField(default='')
    
    class Meta:
        verbose_name = "Objectives"
        verbose_name_plural = "Objectives"
    
    def __str__(self):
        return self.objective_description


class Instructions(models.Model):
    objective = models.ForeignKey(Objectives,on_delete=models.CASCADE)
    step = models.IntegerField()
    code = models.ImageField(upload_to='images/')
    code_description = models.TextField()
    reference = models.TextField()

    class Meta:
        verbose_name = "Instructions"
        verbose_name_plural = "Instructions"

    def __str__(self):
        return self.code_description




