from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates or resets the admin user'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'ismail'
        email = 'ismail@dzeeshop.com'
        password = 'admin123'

        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': email, 'is_staff': True, 'is_superuser': True}
        )
        if not created:
            user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Admin "{username}" password reset'))
        else:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Admin "{username}" created'))
