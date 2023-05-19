import yaml

from django.core.management.base import BaseCommand

from usermenu.models import User, Menu, Region, Info

class Command(BaseCommand):
    help = 'Загрузка данных для демонстрации решения'

    def add_arguments(self, parser):
        parser.add_argument('datafile', type=str)

    def handle(self, *args, **options):
        filename = options['datafile']
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        import pprint
        pprint.pprint(data)

        self.load_users(data['Users'])
        self.load_menu(data['Tables'])
        for table_name in data['Data'].keys():
            self.clear_table(table_name)
        self.load_regions(data['Regions'])
        for table_name, table_data in data['Data'].items():
            self.load_table(table_name, table_data)
        
    def load_users(self, users):
        User.objects.all().delete()
        for user in users:
            User.objects.create_user(**user)
        
    def load_menu(self, tables):
        Menu.objects.all().delete()
        for table in tables:
            item = Menu.objects.create(id=table['id'], title=table['title'], table=table['table'])
            for user_id in table['users']:
                item.users.add(user_id)
        
    def load_regions(self, regions):
        Region.objects.all().delete()
        for region in regions:
            item = Region.objects.create(id=region['id'], name=region['name'])
            for user_id in region['users']:
                item.users.add(user_id)

    def clear_table(self, table_name):
        table = Info.get_table(table_name)
        table.objects.all().delete()

    def load_table(self, table_name, data):
        table = Info.get_table(table_name)
        table.objects.all().delete()
        for d in data:
            table.objects.create(**d)

