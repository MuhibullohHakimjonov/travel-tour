from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import TourCategory, Tours, Wishlist
from .forms import RegisterForm, LoginForm, RequestForm


def index(request):
	categories = TourCategory.objects.all()
	tours = Tours.objects.all()

	# Get the list of tour IDs that are in the user's wishlist
	wishlist_tours = Tours.objects.filter(id__in=Wishlist.objects.filter(user=request.user).values_list('tour',
																										flat=True)) if request.user.is_authenticated else []

	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			print(form.errors)
	else:
		form = RequestForm()

	context = {
		'tours': tours,
		'categories': categories,
		'wishlist_tours': wishlist_tours,
		'form': form
	}

	return render(request, 'tour/index.html', context)



def tour_search(request):
    tour_name = request.GET.get('tour_name', '')
    category_id = request.GET.get('category', '')

    # Filter tours based on search inputs
    tours = Tours.objects.all()
    if tour_name:
        tours = tours.filter(name__icontains=tour_name)
    if category_id:
        tours = tours.filter(category__id=category_id)

    categories = TourCategory.objects.all()
    context = {
        'tours': tours,
        'categories': categories,
    }
    return render(request, 'tour/index.html', context)



def login_view(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			if user:
				login(request, user)
				return redirect('index')
			else:
				return redirect('index')
		else:
			return redirect('index')


def register_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		if User.objects.filter(username=username).exists():
			messages.error(request, 'Username already taken.')
			return redirect('index')
		user = User.objects.create_user(username=username, email=email, password=password)
		user.save()
		login(request, user)
		messages.success(request, 'Account successfully created and logged in!')
		return redirect('index')
	return redirect('index')


def logout_view(request):
	logout(request)
	return redirect('index')




def wishlist_remove(request, pk):
	tour = get_object_or_404(Tours, pk=pk)
	user = request.user
	wish = Wishlist.objects.filter(tour=tour, user=user).first()
	if wish:
		wish.delete()
		message = "Tour removed from your wishlist."
	else:
		message = "Tour not found in your wishlist."

	return JsonResponse({
		'message': message,
	})


@login_required
def wishlist_view(request):
	user = request.user
	if user.is_authenticated:
		wishlist_items = Wishlist.objects.filter(user=user)
		user_wishlist = [item.tour for item in wishlist_items]
	else:
		user_wishlist = []

	return render(request, 'shop/index.html', {
		'user_wishlist': user_wishlist
	})


@login_required
def wishlist_action(request, pk):
	user = request.user
	tour = Tours.objects.get(pk=pk)
	if Wishlist.objects.filter(user=user, tour=tour).exists():
		Wishlist.objects.get(user=user, tour=tour).delete()
	else:
		Wishlist.objects.create(user=user, tour=tour)

	return redirect(request.META.get('HTTP_REFERER'))






