from django.db import models
from PIL import Image, ImageOps

class News(models.Model):
    title = models.CharField("Título", max_length=200)
    summary = models.TextField("Resumo", max_length=500)
    content = models.TextField("Conteúdo completo")
    image = models.ImageField("Imagem", upload_to='news/', blank=True, null=True)
    is_featured = models.BooleanField("Destaque na Home", default=False)
    
    external_link = models.URLField(
        "Link externo", 
        blank=True, 
        null=True,
        help_text="Link externo relacionado à notícia (opcional)"
    )
    
    created_at = models.DateTimeField("Data de criação", auto_now_add=True)
    updated_at = models.DateTimeField("Última atualização", auto_now=True)

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField("Título", max_length=200)
    summary = models.TextField("Resumo")
    image = models.ImageField("Imagem", upload_to='projects/', blank=True, null=True)
    link = models.URLField("Link do Projeto", blank=True, null=True)
    created_at = models.DateTimeField("Data de criação", auto_now_add=True)
    is_active = models.BooleanField("Ativo", default=True)
    is_featured = models.BooleanField("Destaque na Home", default=False)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class CodigoSocialCard(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Processo Seletivo Aberto'),
        ('fechado', 'Processo Seletivo Fechado'),
    ]

    title = models.CharField("Título", max_length=100)
    description = models.TextField("Descrição")
    status = models.CharField(
        "Status",
        max_length=10,
        choices=STATUS_CHOICES,
        default='fechado'
    )

    form_link = models.URLField(
        "Link do formulário (Microsoft Forms)",
        blank=True,
        null=True
    )

    opening_date = models.CharField(
        "Data de abertura",
        max_length=50,
        blank=True,
        null=True
    )

    is_active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Card do Código Social"
        verbose_name_plural = "Cards do Código Social"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class HealthcareJuniorCard(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Processo Seletivo Aberto'),
        ('fechado', 'Processo Seletivo Fechado'),
    ]

    title = models.CharField("Título", max_length=100)
    description = models.TextField("Descrição")
    status = models.CharField(
        "Status",
        max_length=10,
        choices=STATUS_CHOICES,
        default='fechado'
    )

    form_link = models.URLField(
        "Link do formulário (Microsoft Forms)",
        blank=True,
        null=True
    )

    opening_date = models.CharField(
        "Data de abertura",
        max_length=50,
        blank=True,
        null=True
    )

    is_active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Card da Healthcare Júnior Einstein"
        verbose_name_plural = "Cards da Healthcare Júnior Einstein"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField("Nome do produto", max_length=120)
    description = models.TextField("Descrição")
    price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    
    image = models.ImageField(
        "Imagem do produto",
        upload_to="products/",
        blank=True,
        null=True
    )

    link = models.URLField(
        "Link externo (opcional)",
        blank=True,
        null=True,
        help_text="Link para pagamento, WhatsApp, etc."
    )

    is_active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TeamMember(models.Model):

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)

    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            
            # Corrige orientação baseada no EXIF
            img = ImageOps.exif_transpose(img)

            width, height = img.size

            min_dim = min(width, height)

            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2

            img = img.crop((left, top, right, bottom))

            img = img.resize((200,200), Image.LANCZOS)

            img.save(self.photo.path)
        
class Eventos(models.Model):
    title = models.CharField("Título", max_length=200)
    summary = models.TextField("Resumo", max_length=550)
    image = models.ImageField("Imagem", upload_to='projects/', blank=True, null=True)
    link = models.URLField("Link do site do Evento", blank=True, null=True)
    created_at = models.DateTimeField("Data de criação", auto_now_add=True)
    is_active = models.BooleanField("Ativo", default=True)
    is_featured = models.BooleanField("Destaque na Home", default=False)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class CodigoSocialFoto(models.Model):

    foto = models.ImageField(upload_to='codigo_social/')
    legenda = models.CharField(max_length=200, blank=True)

    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.legenda or "Foto Código Social"

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.foto:
            img = Image.open(self.foto.path)

            # corrige rotação automática (EXIF de celular)
            img = ImageOps.exif_transpose(img)

            img.thumbnail((1600,1600), Image.LANCZOS)

            img.save(self.foto.path, quality=90)