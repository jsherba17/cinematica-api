from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None):
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            username=username)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash
        user.save()
        return user

    def create_superuser(self,first_name, last_name, username, password=None):
        user = self.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        print(user.is_staff)
        return user
