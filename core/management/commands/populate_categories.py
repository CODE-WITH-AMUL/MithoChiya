from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import Category

class Command(BaseCommand):
    help = 'Populates the database with initial categories for menu items.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to populate categories...")
        
        categories = [
            'Veg',
            'Non Veg',
            'Drinks',
            'Snacks',
            'Desserts',
            'Beverage',
        ]
        
        for category_name in categories:
            slug = slugify(category_name)
            
            # Check if a category with the same name or slug already exists
            if not Category.objects.filter(name=category_name).exists() and \
               not Category.objects.filter(slug=slug).exists():
                
                Category.objects.create(name=category_name, slug=slug)
                self.stdout.write(self.style.SUCCESS(f'Successfully created category: {category_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category "{category_name}" already exists.'))
                
        self.stdout.write(self.style.SUCCESS("Category population complete."))

