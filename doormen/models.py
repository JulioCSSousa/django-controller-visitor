from django.db import models

class Doorman(models.Model):
    
    user = models.OneToOneField(
        
        'users.CustomUser',
        verbose_name='User',
        on_delete=models.PROTECT
    )
    
    fullname = models.CharField(
        verbose_name='Full Name',
        max_length=194
    )
    
    register_id = models.CharField(
        verbose_name = 'Social Security Number / cpf',
        max_length=11
    )
    
    phone = models.CharField(
        verbose_name='Phone',
        max_length=11
    )

    born_date = models.DateField (
        verbose_name='Born Date',
        auto_now=False,
        auto_now_add=False
    )
    
    class Meta:
        verbose_name = "Doorman"
        verbose_name_plural = "Doormen"
        db_table = 'doorman'
        
    def __str__(self):
        return self.fullname
    