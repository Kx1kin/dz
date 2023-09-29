from django.db import models
from django.utils.html import format_html
from django.contrib import admin

class Advertisement(models.Model):
     title = models.CharField("заголовок", max_length=128)
     description = models.TextField("описание")
     price = models.DecimalField("цена", max_digits=10, decimal_places=2)
     auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
     create_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)

     @admin.display(description="Дата создания")
     def created_date(self):
          from django.utils import timezone
          if self.create_at.date() == timezone.now().date():
               create_time = self.create_at.time().strftime("%H:%M:%S")
               return format_html(
                    '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', create_time
               )
          return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

     @admin.display(description="Дата изменения")
     def update_date(self):
          from django.utils import timezone
          if self.update_at.date() == timezone.now().date():
               updated_time = self.update_at.time().strftime("%H:%M:%S")
               return format_html(
                    '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', updated_time
               )
          return self.update_at.strftime("%d.%m.%Y в %H:%M:%S")

     def __str__(self):
          return f'Advertisements(id = {self.id}, title = {self.title}, price = {self.price})'

     class Meta:
          db_table = "Advertisements"

#app_advertisments_advertisement