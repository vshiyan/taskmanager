from .models import Task
import datetime


class Checker:
    def __init__(self, user):
        self.user = user

    def checking(self):
        date = datetime.date.today()
        all = Task.objects.filter(owner=self.user)
        for u in all:
            Task.objects.filter(pk=u.pk).update(type_task=self.cmpare(u.date_finish, date))

    def cmpare(self, date1, date2):
        a = date1 - date2
        return int(a.days)

    def checking_state(self):
        date = datetime.date.today()
        all = Task.objects.filter(owner=self.user)
        for u in all:
            if u.state == 'activ':
                if self.cmpare(u.date_finish, date) < 0:
                    Task.objects.filter(pk=u.pk).update(state='fail')
            elif u.state == 'compl':
                Task.objects.filter(pk=u.pk).update(state='compl')
            elif u.state == 'fail':
                Task.objects.filter(pk=u.pk).update(state='fail')
            else:
                Task.objects.filter(pk=u.pk).update(state='activ')
