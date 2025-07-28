from django.db import models
class AllAssignment(models.Model):
    title = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "All Categories"

    def __str__(self):
        return f"{self.title}"

class AssignmentTopic(models.Model):
    assignment = models.ForeignKey(AllAssignment, on_delete=models.CASCADE, related_name='topics')  # One assignment, many topics
    topic_name = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')  # Store PDF files

    def __str__(self):
        return f"{self.topic_name}"

class Project_Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Project Categories'

    def __str__(self) -> str:
        return f"{self.title}"
    
class Project_Name(models.Model):
    project= models.ForeignKey(Project_Category, on_delete=models.CASCADE, related_name='projects')
    project_name=models.CharField(max_length=200)
    pdf=models.FileField(upload_to='pdfs/')

    def __str__(self) -> str:
        return f"{self.project_name}"
    class Meta:
        verbose_name_plural = 'Project Name'
    
    


