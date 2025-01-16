from .models import Wishlist, Tours


def wishlist(request):
	# Check if the user is authenticated and has a wishlist
	if request.user.is_authenticated:
		wishlist_tours = Tours.objects.filter(
			id__in=Wishlist.objects.filter(user=request.user).values_list('tour', flat=True))
	else:
		wishlist_tours = []

	return {'wishlist_tours': wishlist_tours}
