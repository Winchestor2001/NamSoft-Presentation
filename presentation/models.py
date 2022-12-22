from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Subject(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Presentation(models.Model):
    num = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return '{} - {}'.format(self.subject, self.title)
    
    class Meta:
        ordering = ('num',)


class PresentationDetail(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    code = RichTextUploadingField()

    def __str__(self) -> str:
        return '{}'.format(self.presentation)
