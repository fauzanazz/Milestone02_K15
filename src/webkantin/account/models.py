from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    CHOICES =(
        ("1", "Teknik Informatika"),
        ("2", "Sistem dan Teknologi Informasi"),
        ("3", "Teknik Elektro"),
        ("4", "Teknik Tenaga Listrik"),
        ("4", "Teknik Telekomunikasi"),
        ("4", "Teknik Biomedis"),
        ("5", "Matematika"),
        ("6", "Aktuaria"),
        ("7", "Fisika"),
        ("8", "Astronomi"),
        ("9", "Kimia"),
        ("10", "Biologi"),
        ("11", "Mikrobiologi"),
        ("12", "Rekayasa Hayati"),
        ("13", "Rekayasa Pertanian"),
        ("14", "Rekayasa Kehutanan"),
        ("15", "Teknologi Pasca Panen"),
        ("16", "Sains dan Teknologi Farmasi"),
        ("17", "Farmasi Klinik dan Komunitas"),
        ("18", "Teknik Geologi"),
        ("19", "Teknik Geodesi dan Geomatika"),
        ("20", "Meteorologi"),
        ("21", "Oseanografi"),
        ("22", "Teknik Pertambangan"),
        ("23", "Teknik Perminyakan"),
        ("24", "Teknik Geofisika"),
        ("25", "Teknik Metalurgi"),
        ("26", "Teknik Kimia"),
        ("27", "Teknik Fisika"),
        ("28", "Teknik Industri"),
        ("29", "Manajemen Rekayasa"),
        ("30", "Teknik Pangan"),
        ("31", "Teknik Bioenergi dan Kemurgi"),
        ("32", "Teknik Mesin"),
        ("33", "Teknik Dirgantara"),
        ("34", "Teknik Material"),
        ("35", "Teknik Sipil"),
        ("36", "Teknik Lingkungan"),
        ("37", "Teknik Kelautan"),
        ("38", "Teknik dan Pengelolaan Sumber Daya Air"),
        ("39", "Rekayasa Infrastruktur Lingkungan"),
        ("40", "Arsitektur"),
        ("41", "Perencanaan Wilayah dan Kota"),
        ("42", "Manajemen"),
        ("43", "Kewirausahaan"),
        ("44", "Seni Rupa"),
        ("45", "Kriya"),
        ("46", "Desain Interior"),
        ("47", "Desain Komunikasi Visual"),
        ("48", "Desain Produk"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length= 52, default="")
    NIM = models.CharField(max_length=8, default="")
    jurusan = models.TextField(choices= CHOICES, default="")

    def __str__(self):
        return self.user.username