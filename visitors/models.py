from django.db import models

class Visitor(models.Model):
    fullname = models.CharField(
        verbose_name="Full Name", 
        max_length=50)
    
    person_identity = models.CharField(
        verbose_name="Social Security Number / cpf", 
        max_length=11)

    born_date = models.DateField(
        verbose_name="born Date",
        auto_now=False,
        auto_now_add=False
    )
    
    house_number = models.PositiveSmallIntegerField(
        verbose_name="House Number"
    )
    
    vehicle_sign = models.CharField(
        ("Vehicle Sign"), 
        max_length=7,
        blank=True,
        null=True
    )
    
    arrived_time = models.DateTimeField(
        ("Time Visitor Arrived"), 
        auto_now_add=True)
    
    leave_hour = models.DateTimeField(
        ("Time Visitor Left"), auto_now=False, 
        auto_now_add=False, 
        blank=True, null=True)
    
    authorization_time = models.DateTimeField(
        ("Time Authorization happened"), auto_now=False, 
        blank=True, null=True)
    
    authorized_by_resident = models.CharField(
        ("Resident who knows the visitor"), 
        max_length=194,
        blank=True)

    registered_by = models.ForeignKey(
        "doormen.Doorman", 
        verbose_name=("Doorman who gives the visitor enter authorization"), 
        on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitors"
        
    def __str__(self):
        return self.fullname
    
    