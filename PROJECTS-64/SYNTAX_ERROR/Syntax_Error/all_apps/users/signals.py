from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Stats
from django.contrib.auth.signals import user_logged_in
from django.utils.timezone import now
import pytz

# Create profile when user is created, excluding superusers
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:  # Exclude superusers
        profile = Profile.objects.create(user=instance)
        Stats.objects.create(profile=profile)  # Create stats for the profile

# Save the profile and stats when user is updated, excluding superusers
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:  # Exclude superusers
        instance.profile.save()
        instance.profile.stats.save()  # Save the associated stats as well


@receiver(user_logged_in)
def update_login_count(sender, request, user, **kwargs):
    if not user.is_superuser:  # Exclude superusers
        user_profile = Profile.objects.get(user=user)
        stats, created = Stats.objects.get_or_create(profile=user_profile)
        
        # Increment total logins
        if stats.total_logins is None:
            stats.total_logins = 0
        stats.total_logins += 1
        stats.save()

@receiver(user_logged_in)
def update_last_login(sender, request, user, **kwargs):
    try:
        # Get the Profile associated with the user
        profile = Profile.objects.get(user=user)
        
        # Get the Stats associated with the user's profile
        stats = Stats.objects.get(profile=profile)
        
        # Get the current datetime in UTC and convert to IST (Asia/Kolkata timezone)
        ist_timezone = pytz.timezone('Asia/Kolkata')
        local_time = now().astimezone(ist_timezone)
        
        # Format the time as '8:45 PM Thursday, 3 October 2024 (IST)'
        formatted_time = local_time.strftime('%I:%M %p %A, %d %B %Y (IST)')
        
        # Update the last_login field in Stats model
        stats.last_login = formatted_time
        
        # Increment the total_logins by 1
        stats.total_logins += 1
        
        # Save the updated Stats
        stats.save()
        
    except Profile.DoesNotExist:
        # Handle case where the Profile does not exist for the user
        pass
    except Stats.DoesNotExist:
        # Handle case where the Stats does not exist for the user's profile
        pass
