from django.contrib import admin
from tweetapp.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group', {"fields":['message']}),
        ('Nickname Group', {"fields":["nickname"]})
    ] # burada da kolonları gruplama yapıyoruz.
    
    # fields = ['message', 'nickname'] # admin sayfasında database kolon başlıklarından ya da diğer anlamıyla model.py de oluşturduğumuz sınıfının bileşenlerinden hangisinin görünmesini istiyorsak onu yazıyoruz.

admin.site.register(Tweet,TweetAdmin) #burada admin hesabında görünecek modelimizi register ediyoruz. tanıtıyoruz. böylece database e bağlanabiliyoruz. tweetleri görüyoruz.