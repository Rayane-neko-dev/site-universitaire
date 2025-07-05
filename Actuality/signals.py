# actu/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Actuality
from Home.models import Subscriber
from django.urls import reverse

@receiver(post_save, sender=Actuality)
def send_newsletter_on_new_actuality(sender, instance, created, **kwargs):
    if created:
        subject = f"Nouvelle Actualité : {instance.titre}"

        # Génère le lien vers la page de détail de l'actualité (si elle existe)
        # Assure-toi que tu as une URL nommée 'actuality_detail' avec actualite_id en paramètre
        try:
            url = f"http://ton-domaine.com{reverse('actuality_detail', args=[instance.actualite_id])}"
            

        except:
            url = "Lien non disponible"

        message = (
            f"Bonjour,\n\nUne nouvelle actualité a été publiée :\n\n"
            f"Titre : {instance.titre}\n\n"
            f"Contenu : {instance.contenu[:300]}...\n\n"
            f"Consultez-la ici : {url}\n\n"
            f"Merci pour votre fidélité."
        )

        for subscriber in Subscriber.objects.all():
            send_mail(
                subject,
                message,
                'exemple@gmail.com',  # Remplace par ton adresse d'envoi
                [subscriber.email],
                fail_silently=False,
            )
