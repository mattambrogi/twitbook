from django import template
from accounts.models import Following

register = template.Library()

# I think I'm passing the filter a post..I think
def only_following(author, user):
    if author == user:
        return True
    else:
        return Following.objects.filter(user_id=user).filter(following_user_id=author).exists()
 
register.filter('only_following', only_following)
    

