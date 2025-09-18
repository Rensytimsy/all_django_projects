from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid


# Create your models here.
    
class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    location = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    STORE_LIST=(
        ('clothing', 'Apparel&Accessories'),
        ('electronics', 'Electronics&Accessories'),
        ('food', 'Food&Bevarages'),
        ('beauty', 'Health&Beauty'),
        ('games', 'Hobby,Toys&Games'),
        ('library', 'Books,Music&Media'),
        ('jewelry', 'Jewelry&Luxury goods'),
    )
    store_type = models.TextField(
        choices=STORE_LIST,
        default="electronics",
        blank=True,
        max_length=100,
        help_text="Please provide the type of store you are creating"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="store_case_insentive_unique",
                violation_error_message="A store with the name exists"
            )
        ]
        
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    store = models.ManyToManyField(
        Store, help_text="Please provide a store for this product"
    )
    available = models.BooleanField(default=False)
    
    #return the created product title
    def __str__(self):
        return self.title
    
    #Below function gets a store name for a specific product
    def get_product_store(self):
        return ", ".join(store.name for store in self.store.all())
    get_product_store.short_description = "Store" #type: ignore