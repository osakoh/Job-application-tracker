from django.shortcuts import render, get_object_or_404

from .models import Job, Contact

# Create your views here.
#  j1 = Job.objects.get(id=1)
# c1 = Contact.objects.get(job=j1)
# c1.name
# c1.job.company_name


def applications(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'jobs/list.html', context)


def app_detail(request, pk):
    application = get_object_or_404(Job, id=pk)

    # contact = get_object_or_404(Contact, job=application)

    context = {
        'application': application,
        # 'contact': contact
    }

    return render(request, 'jobs/detail.html', context)