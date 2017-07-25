from django.db import models

# Create your models here.
class Subscriber(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=128)

	# эта ф-ция помогает в модели выводить название по умолчанию
	def __str__(self):
		return 'Пользователь %s %s' % (self.name, self.email)
		#self.id or self.email or self.name

	#для названия папки на сервере и в ед.числе и в мн.числе
	class Meta:
		verbose_name = 'MySubscriber'
		verbose_name_plural = 'A lot of Subscribers'   

