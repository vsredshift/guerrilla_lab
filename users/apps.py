from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    
    # import signals 
    def ready(self):
        import users.signals
