# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dostawcy(models.Model):
    iddostawcy = models.IntegerField(
        db_column="IDdostawcy", primary_key=True
    )  # Field name made lowercase.
    nazwafirmy = models.CharField(
        db_column="NazwaFirmy", max_length=40
    )  # Field name made lowercase.
    przedstawiciel = models.CharField(
        db_column="Przedstawiciel", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    stanowiskoprzedstawiciela = models.CharField(
        db_column="StanowiskoPrzedstawiciela", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    adres = models.CharField(
        db_column="Adres", max_length=60, blank=True, null=True
    )  # Field name made lowercase.
    miasto = models.CharField(
        db_column="Miasto", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    region = models.CharField(
        db_column="Region", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    kodpocztowy = models.CharField(
        db_column="KodPocztowy", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    kraj = models.CharField(
        db_column="Kraj", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    telefon = models.CharField(
        db_column="Telefon", max_length=24, blank=True, null=True
    )  # Field name made lowercase.
    faks = models.CharField(
        db_column="Faks", max_length=24, blank=True, null=True
    )  # Field name made lowercase.
    stronamacierzysta = models.TextField(
        db_column="StronaMacierzysta", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Dostawcy"


class Kategorie(models.Model):
    idkategorii = models.IntegerField(
        db_column="IDkategorii", primary_key=True
    )  # Field name made lowercase.
    nazwakategorii = models.CharField(
        db_column="NazwaKategorii", max_length=20
    )  # Field name made lowercase.
    opis = models.TextField(
        db_column="Opis", blank=True, null=True
    )  # Field name made lowercase.
    rysunek = models.BinaryField(
        db_column="Rysunek", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Kategorie"


class Klienci(models.Model):
    idklienta = models.CharField(
        db_column="IDklienta", max_length=5, primary_key=True
    )  # Field name made lowercase.
    nazwafirmy = models.CharField(
        db_column="NazwaFirmy", max_length=40
    )  # Field name made lowercase.
    przedstawiciel = models.CharField(
        db_column="Przedstawiciel", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    stanowiskoprzedstawiciela = models.CharField(
        db_column="StanowiskoPrzedstawiciela", max_length=35, blank=True, null=True
    )  # Field name made lowercase.
    adres = models.CharField(
        db_column="Adres", max_length=60, blank=True, null=True
    )  # Field name made lowercase.
    miasto = models.CharField(
        db_column="Miasto", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    region = models.CharField(
        db_column="Region", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    kodpocztowy = models.CharField(
        db_column="KodPocztowy", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    kraj = models.CharField(
        db_column="Kraj", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    telefon = models.CharField(
        db_column="Telefon", max_length=24, blank=True, null=True
    )  # Field name made lowercase.
    faks = models.CharField(
        db_column="Faks", max_length=24, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Klienci"


class Pracownicy(models.Model):
    idpracownika = models.IntegerField(
        db_column="IDpracownika", primary_key=True
    )  # Field name made lowercase.
    nazwisko = models.CharField(
        db_column="Nazwisko", max_length=20
    )  # Field name made lowercase.
    imię = models.CharField(
        db_column="Imię", max_length=10
    )  # Field name made lowercase.
    stanowisko = models.CharField(
        db_column="Stanowisko", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    zwrotgrzecznościowy = models.CharField(
        db_column="ZwrotGrzecznościowy", max_length=25, blank=True, null=True
    )  # Field name made lowercase.
    dataurodzenia = models.DateTimeField(
        db_column="DataUrodzenia", blank=True, null=True
    )  # Field name made lowercase.
    datazatrudnienia = models.DateTimeField(
        db_column="DataZatrudnienia", blank=True, null=True
    )  # Field name made lowercase.
    adres = models.CharField(
        db_column="Adres", max_length=60, blank=True, null=True
    )  # Field name made lowercase.
    miasto = models.CharField(
        db_column="Miasto", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    region = models.CharField(
        db_column="Region", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    kodpocztowy = models.CharField(
        db_column="KodPocztowy", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    kraj = models.CharField(
        db_column="Kraj", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    telefondomowy = models.CharField(
        db_column="TelefonDomowy", max_length=24, blank=True, null=True
    )  # Field name made lowercase.
    telefonwewnętrzny = models.CharField(
        db_column="TelefonWewnętrzny", max_length=4, blank=True, null=True
    )  # Field name made lowercase.
    fotografia = models.BinaryField(
        db_column="Fotografia", blank=True, null=True
    )  # Field name made lowercase.
    uwagi = models.TextField(
        db_column="Uwagi", blank=True, null=True
    )  # Field name made lowercase.
    szef = models.IntegerField(
        db_column="Szef", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Pracownicy"


class Produkty(models.Model):
    idproduktu = models.IntegerField(
        db_column="IDproduktu", primary_key=True
    )  # Field name made lowercase.
    nazwaproduktu = models.CharField(
        db_column="NazwaProduktu", max_length=40
    )  # Field name made lowercase.
    iddostawcy = models.ForeignKey(
        Dostawcy,
        db_column="IDdostawcy",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    idkategorii = models.ForeignKey(
        Kategorie,
        db_column="IDkategorii",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    ilośćjednostkowa = models.CharField(
        db_column="IlośćJednostkowa", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    cenajednostkowa = models.DecimalField(
        db_column="CenaJednostkowa",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    stanmagazynu = models.SmallIntegerField(
        db_column="StanMagazynu", blank=True, null=True
    )  # Field name made lowercase.
    ilośćzamówiona = models.SmallIntegerField(
        db_column="IlośćZamówiona", blank=True, null=True
    )  # Field name made lowercase.
    stanminimum = models.SmallIntegerField(
        db_column="StanMinimum", blank=True, null=True
    )  # Field name made lowercase.
    wycofany = models.BooleanField(db_column="Wycofany")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Produkty"


class Pozycjezamówienia(models.Model):
    idzamówienia = models.IntegerField(
        db_column="IDzamówienia", primary_key=True
    )  # Field name made lowercase.
    idproduktu = models.ForeignKey(
        Produkty, db_column="IDproduktu", on_delete=models.CASCADE
    )  # Field name made lowercase.
    cenajednostkowa = models.DecimalField(
        db_column="CenaJednostkowa", max_digits=19, decimal_places=4
    )  # Field name made lowercase.
    ilość = models.SmallIntegerField(db_column="Ilość")  # Field name made lowercase.
    rabat = models.FloatField(db_column="Rabat")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "PozycjeZamówienia"


class Spedytorzy(models.Model):
    idspedytora = models.IntegerField(
        db_column="IDspedytora", primary_key=True
    )  # Field name made lowercase.
    nazwafirmy = models.CharField(
        db_column="NazwaFirmy", max_length=40
    )  # Field name made lowercase.
    telefon = models.CharField(
        db_column="Telefon", max_length=24, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Spedytorzy"


class Zamówienia(models.Model):
    idzamówienia = models.IntegerField(
        db_column="IDzamówienia", primary_key=True
    )  # Field name made lowercase.
    idklienta = models.ForeignKey(
        Klienci, db_column="IDklienta", on_delete=models.CASCADE
    )  # Field name made lowercase.
    idpracownika = models.ForeignKey(
        Pracownicy,
        db_column="IDpracownika",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )  # Field name made lowercase.
    datazamówienia = models.DateTimeField(
        db_column="DataZamówienia", blank=True, null=True
    )  # Field name made lowercase.
    datawymagana = models.DateTimeField(
        db_column="DataWymagana", blank=True, null=True
    )  # Field name made lowercase.
    datawysyłki = models.DateTimeField(
        db_column="DataWysyłki", blank=True, null=True
    )  # Field name made lowercase.
    idspedytora = models.ForeignKey(
        Spedytorzy,
        db_column="IDspedytora",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )  # Field name made lowercase.
    fracht = models.DecimalField(
        db_column="Fracht", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    nazwaodbiorcy = models.CharField(
        db_column="NazwaOdbiorcy", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    adresodbiorcy = models.CharField(
        db_column="AdresOdbiorcy", max_length=60, blank=True, null=True
    )  # Field name made lowercase.
    miastoodbiorcy = models.CharField(
        db_column="MiastoOdbiorcy", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    regionodbiorcy = models.CharField(
        db_column="RegionOdbiorcy", max_length=15, blank=True, null=True
    )  # Field name made lowercase.
    kodpocztowyodbiorcy = models.CharField(
        db_column="KodPocztowyOdbiorcy", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    krajodbiorcy = models.CharField(
        db_column="KrajOdbiorcy", max_length=15, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Zamówienia"

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sysdiagrams"
        unique_together = (("principal_id", "name"),)
