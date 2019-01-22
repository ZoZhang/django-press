from django.contrib.auth.models import User
from django.db import models

# class Person(models.Model):
#     user = models.OneToOneField(User,
#                                 on_delete=models.CASCADE,
#                                 default=None)
#
#     birthday = models.DateTimeField(default=None,
#                                     verbose_name='Birthday')
#
#     phones = models.ManyToManyField('Phone')
#
#     def __str__(self):
#         return '{}{}{}'.format(
#             self.user.first_name if self.user is not None else '?',
#             self.user.last_name if self.user is not None else '?',
#             self.user.email if self.user is not None else '?',
#         )
#
#
# class TypePhone(models.Model):
#     description = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.description
#
#
# class Phone(models.Model):
#     type_telephone = models.ForeignKey(TypePhone,
#                                        on_delete=models.CASCADE)
#     number = models.CharField(max_length=12,
#                               default=None)
#
#     def __str__(self):
#         return self.type_telephone + self.number
#
#
# class Cocktail(models.Model):
#     title = models.CharField(max_length=20)
#     description = models.CharField(max_length=50)
#     recette = models.TextField(max_length=3000)
#
#     def __str__(self):
#         return self.title
#
#
# class Unit(models.Model):
#     description = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.description
#
#
# class Ingredient(models.Model):
#     description = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.description
#
#
# class CocktailIngredientUnite(models.Model):
#     cocktail = models.ForeignKey(Cocktail,
#                                  related_name='c_i_u',
#                                  on_delete=models.CASCADE,
#                                  default=None)
#     ingredient = models.ForeignKey(Ingredient,
#                                    on_delete=models.CASCADE,
#                                    default=None)
#     unite = models.ForeignKey(Unit,
#                               on_delete=models.CASCADE,
#                               default=None)
#     value = models.IntegerField(null=None,
#                                 default=None)
#
#     def __str__(self):
#         return '{}: {}{}{}'.format(
#             self.cocktail if self.cocktail is not None else '?',
#             self.value if self.value is not None else '?',
#             self.unite if self.unite is not None else '?',
#             self.ingredient if self.ingredient is not None else '?',
#         )
#
