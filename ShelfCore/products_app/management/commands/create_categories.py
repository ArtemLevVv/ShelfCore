from django.core.management.base import BaseCommand

from products_app.models import Category

class Command(BaseCommand):
    help = 'Crate default product category'
    
    def handle(self, *args, **options):
        
        categories = [
            {
                'name': 'Food',
                'descriptions': 'Food Products',
            },
            {
                'name': 'Drinks',
                'descriptions': 'Cold and hot drinks',
            },
            {
                'name': 'Tobacco',
                'descriptions': 'Cigarettes and tobacco products'
            },
            {
                'name': 'Alcohol',
                'descriptions': 'Alcohol beverages'
            },
        ]
        
        for category in categories:
            obj, created = Category.objects.get_or_create(
                name = category['name'],
                defaults={
                    'description': category['descriptions']
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created category: {obj.name}'
                    )
                )
            
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Already exists: {obj.name}'
                    )
                )