from django.db import models

class FPDD_DocConnectED(models.Model):
    
    writeOffs = models.CharField('ID документа списания', unique=True, max_length=200)
    localInvent = models.CharField('ID документа инвентаризации', unique=True, max_length=200)
    liCreationState = models.CharField('Статус документа коррекции', max_length=50)# none|started|created|completed
    
    class Meta:
        verbose_name = 'Связка'
        verbose_name_plural = 'Связки'
    def __str__(self):
        return self.writeOffs