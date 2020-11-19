from django.db import models


# using model --> Create SQL-Tabelle mit Python ohne SQL-Query

class Notice(models.Model):
    notice_title = models.CharField(max_length=70)
    notice_text = models.CharField(max_length=400)
    pub_start = models.DateTimeField()
    pub_end = models.DateTimeField()
