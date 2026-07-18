from django.core.management.base import BaseCommand

from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Assign permissions to groups"
    
    def handle(self, *args, **options):
        permissions = {
            "Manager":[
                'view_product',
                'add_product',
                'change_product',
            ],
            "Seller":[
                'view_product',
            ],
            "Admin":[
                "view_product",
                'add_product',
                'change_product',
                'delete_product',
            ],
        }
        
        for group_name, permission_list in permissions.items():
            
            try:
                group = Group.objects.get(
                    name= group_name
                )
            except Group.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(
                        f'Group {group_name} does not exist'
                    )
                )
                continue
            
            for permission_codename in permission_list:
                try:
                    permission= Permission.objects.get(
                        codename= permission_codename
                    )
                    group.permissions.add(permission)
                    
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'{group_name} -> {permission_codename}'
                        )
                    )
                except Permission.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Permission {permission_codename} not found'
                        )
                    )