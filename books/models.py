from django.db import models
from django.utils.translation import ugettext_lazy as _
from general.models import CommonModel
from general.functions import get_auto_id 
from customer.models import Customer

INTERVAL_CHOICES = (
    ('hours','Hours'),
    ('minutes','Minutes'),
)


# Create your models here.
class Book(CommonModel):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    files = models.FileField(upload_to='books/')
    time_interval = models.CharField(max_length=10)
    interval_in = models.CharField(max_length=10,choices=INTERVAL_CHOICES,)

    class Meta:
        db_table = 'book'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def save(self, *args, **kwargs):
        if self._state.adding:                    
           
            auto_id = get_auto_id(Book)            
            self.auto_id = auto_id           
            
        super(Book, self).save(*args, **kwargs)

        
    def __str__(self):
        return str(self.name)


class BookRequest(CommonModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = 'book_request'
        verbose_name = _('Book Request')
        verbose_name_plural = _('Book Requests')

    def save(self, *args, **kwargs):
        if self._state.adding:                    
           
            auto_id = get_auto_id(BookRequest)            
            self.auto_id = auto_id           
            
        super(BookRequest, self).save(*args, **kwargs)