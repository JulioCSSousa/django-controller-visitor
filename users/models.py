from django.db import models
from django.contrib.auth.models import (
    Group,
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    Permission
)

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        user = self.model(
            email = self.normalize_email(email)
            
        )
        user.is_active = True
        user.is_staff = False
        
        if password:
            user.set_password(password)
        
        user.save()
        
        return user

    def create_super_user(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email), #exige formato de email
            password=password
        )
    
        user.is_active = models.BooleanField(
            verbose_name = 'super user',
            
        )
        
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save()
        
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Nome único para o relacionamento reverso
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set_permissions',  # Nome único para o relacionamento reverso
        blank=True
    )
    
    email = models.EmailField(
        verbose_name='user email',
        max_length = 194,
        unique=True
    )
    
    is_active = models.BooleanField(
        verbose_name='active user',
        default=True
    )
    
    is_staff = models.BooleanField(
        verbose_name='staff user',
        default=True
    )
    
    is_superuser = models.BooleanField(
        verbose_name="is super user",
        default=False
    )
    
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
        
    def __str__(self):
        return self.email 


        
        


