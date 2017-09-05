from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .forms import EmailForm
from .models import Join
import uuid

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(',')[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '')
	try:
		id_exists = Join.objects.get(ref_id = ref_id)
		if id_exists:
			return get_ref_id()
	except:
		return ref_id

def first_page(request):
	form = EmailForm()
	if request.method == 'POST':
		form = EmailForm(data = request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			join_obj, created = Join.objects.get_or_create(email = email)
			print("ip is: " + get_ip(request))
			if created:
				join_obj.ip_address = get_ip(request)
				join_obj.ref_id = get_ref_id()
				join_obj.save()

			print(reverse('emails:share_url', kwargs = {
			'ref_id': join_obj.ref_id,
			}))
			return HttpResponseRedirect(reverse('emails:share_url', kwargs = {
			'ref_id': join_obj.ref_id,
			}))

	return render(request, 'first_page.html', {'form': form})

def share(request, ref_id):
	return render(request, 'share.html', {'ref_id': ref_id})