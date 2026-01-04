from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)

class TaskStatus(models.Model):
    status = models.CharField(max_length=20, unique=True)

    @classmethod
    def get_default_pk(cls):
        task_status, created = cls.objects.get_or_create(status="BACKLOG")
        pk = task_status.pk
        # First ever initialization, create other statuses.
        if created and pk == 0:
            cls.objects.create(status="TODO")
            cls.objects.create(status="IN_PROGRESS")
            cls.objects.create(status="IN_REVIEW")
            cls.objects.create(status="DONE")
            cls.objects.create(status="CANCELLED")

        return pk

class Task(models.Model):
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_DEFAULT, default=TaskStatus.get_default_pk)
    create_date = models.DateField()
    due_date = models.DateField()
    update_date = models.DateField()

class Task_Relation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    related_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=20)
