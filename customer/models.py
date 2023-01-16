from django.db import models
from general.models import CommonModel
from general.functions import get_auto_id
# Create your models here.

class Customer(CommonModel):
    user = models.OneToOneField("auth.User",on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    

    class Meta:
        db_table = 'users_customer'

    def save(self, *args, **kwargs):
        if self._state.adding:                    
           
            auto_id = get_auto_id(Customer)
            
            self.auto_id = auto_id
            
        super(Customer, self).save(*args, **kwargs)

        
    def __str__(self):
        return str(self.name)