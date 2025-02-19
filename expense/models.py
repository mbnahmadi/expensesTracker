from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here.


User = get_user_model()

class CategoryModel(models.Model):
    title = models.CharField(verbose_name=_('title'))
    status = models.BooleanField(default=True, verbose_name=_('status'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f'{self.title}'    


class ExpenseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    category = models.ForeignKey("CategoryModel", on_delete=models.CASCADE, verbose_name=_('category'))
    expense = models.DecimalField(max_digits=10, decimal_places=5, verbose_name=_('expense'))
    status = models.BooleanField(default=True, verbose_name=_('status'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = _('expense')
        verbose_name_plural = _('expenses')

    def __str__(self):
        return f'{self.user}-{self.title}'    


