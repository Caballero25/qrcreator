from django.db import models
from django.core.files import File
import qrcode
from PIL import Image
from io import BytesIO

# Create your models here.

class QrModel(models.Model):
    contador = models.IntegerField(default=0)
    text = models.TextField(blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def save(self, *args, **kwargs):
        self.contador += 1
        qrcode_img = qrcode.make(self.text)
        qr_width, qr_height = qrcode_img.size
        canvas = Image.new('RGB', (qr_width, qr_height), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-QRcoder.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)