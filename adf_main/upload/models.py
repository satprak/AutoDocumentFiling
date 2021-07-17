# class TextIndex(
#     fields=(),
#     name=None,
#     unique=False,
#     background=False,
#     partialFilterExpression=None,
#     weights=None, 
#     default_language='english', 
#     language_override=None, 
#     textIndexVersion=None)
# from djongo.models.indexes import TextIndex
import os
from djongo import models
# from gdstorage.storage import GoogleDriveStorage

# # Define Google Drive Storage
# gd_storage = GoogleDriveStorage()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# class Map(models.Model):
#     id = models.AutoField( primary_key=True)
#     map_name = models.CharField(max_length=200)
#     map_data = models.FileField(upload_to='maps', storage=gd_storage)

# Create your models here.
# class Document(models.Model):
#     FileName = models.CharField(max_length=255)
#     FilePath = models.FilePathField(path = os.path.join(BASE_DIR,"media"))
#     Content_HTML = models.TextField()
#     Content_TEXT = models.TextField()
#     Page_no = models.IntegerField()

#     # class Meta:
#     #     indexes = [
#     #         TextIndex(fields=['Content_HTML'])
#     #     ]

#     def __str__(self):
#         return self.FileName