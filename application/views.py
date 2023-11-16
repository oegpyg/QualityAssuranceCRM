from collections import OrderedDict
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core import models as core_models
from core.forms import ProjectForm, ReleaseForm, TaskForm, TestEjecutionForm
from django.contrib.auth.models import User
# email inbox page


@login_required
def inbox(request):
    return render(request, 'pages/application/email/inbox.html')

# email read page


@login_required
def read(request):
    return render(request, 'pages/application/email/read.html')

# chat page


@login_required
def chat(request):
    return render(request, 'pages/application/chat/chat.html')

# ecommerce products page


@login_required
def products(request):
    return render(request, 'pages/application/ecommerce/products.html')

# ecommerce product details page


@login_required
def productDetails(request):
    return render(request, 'pages/application/ecommerce/details.html')

# ecommerce add product page


@login_required
def addProduct(request):
    return render(request, 'pages/application/ecommerce/add_product.html')

# ecommerce cart page


@login_required
def cart(request):
    return render(request, 'pages/application/ecommerce/cart.html')

# ecommerce orders page


@login_required
def orders(request):
    return render(request, 'pages/application/ecommerce/orders.html')

# ecommerce sellers page


@login_required
def sellers(request):
    return render(request, 'pages/application/ecommerce/sellers.html')

# ecommerce invoices page


@login_required
def invoices(request):
    return render(request, 'pages/application/ecommerce/invoices.html')

# project list page


@login_required
def projectList(request):
    projects = core_models.Project.objects.all()
    form = ProjectForm()
    ctx = {'projects': projects, 'frm': form}
    return render(request, 'pages/application/project/list.html', context=ctx)

# project details page


@login_required
def projectAdd(request):
    if request.method == 'POST':
        data = OrderedDict()
        data.update(request.POST)
        data['reporter'] = request.user
        form = ProjectForm(data)
        if form.is_valid():
            stmt = form.save()
        # else:
        #    print('no valid')
        #    print(form.errors)
    return redirect(reverse('application:project_list'))


@login_required
def projectDetails(request, pk):
    ctx = {'project': core_models.Project.objects.get(pk=pk)}
    return render(request, 'pages/application/project/details.html', context=ctx)


@login_required
def releaseList(request):
    releases = core_models.Release.objects.all()
    form = ReleaseForm()
    ctx = {'releases': releases, 'frm': form}
    return render(request, 'pages/application/release/list.html', context=ctx)


@login_required
def releaseDetails(request, pk):
    ctx = {'release': core_models.Release.objects.get(
        pk=pk), 'statuss': core_models.Status.objects.all()}
    return render(request, 'pages/application/release/details.html', context=ctx)


@login_required
def taskList(request):
    tasks = core_models.Task.objects.all()
    form = TaskForm()
    ctx = {'tasks': tasks, 'frm': form}
    return render(request, 'pages/application/task/list.html', context=ctx)


@login_required
def taskDetails(request, pk):
    ctx = {'task': core_models.Task.objects.get(pk=pk)}
    return render(request, 'pages/application/task/details.html', context=ctx)


@login_required
def testejecutionList(request):
    testsexe = core_models.TestEjecution.objects.all()
    form = TestEjecutionForm()
    ctx = {'testsexe': testsexe, 'frm': form}
    return render(request, 'pages/application/testejecution/list.html', context=ctx)


@login_required
def testejecutionDetails(request, pk):
    ctx = {'testexe': core_models.TestEjecution.objects.get(pk=pk)}
    return render(request, 'pages/application/testejecution/details.html', context=ctx)


@login_required
def casetestList(request):
    casetests = core_models.CaseTest.objects.all()
    form = TestEjecutionForm()
    ctx = {'casetests': casetests, 'frm': form}
    return render(request, 'pages/application/casetest/list.html', context=ctx)


@login_required
def casetestDetails(request, pk):
    ctx = {'casetest': core_models.CaseTest.objects.get(pk=pk)}
    return render(request, 'pages/application/casetest/details.html', context=ctx)


@login_required
def casetestdocDetails(request, pk):
    ctx = {'att': core_models.CaseTestDocumentation.objects.get(pk=pk)}
    return render(request, 'pages/application/casetest/image_details.html', context=ctx)


@login_required
def typeoftestsList(request):
    typetests = core_models.TypeOfTests.objects.all()
    form = TestEjecutionForm()
    ctx = {'typetests': typetests, 'frm': form}
    return render(request, 'pages/application/typeoftest/list.html', context=ctx)


@login_required
def typeoftestsDetails(request, pk):
    ctx = {'typetest': core_models.TypeOfTests.objects.get(pk=pk)}
    return render(request, 'pages/application/typeoftest/details.html', context=ctx)

# calendar page


@login_required
def calendar(request):
    return render(request, 'pages/application/calendar/calendar.html')

# user member page


@login_required
def team(request):
    return render(request, 'pages/application/user/team.html')

# user card page


@login_required
def card(request):
    return render(request, 'pages/application/user/card.html')

# user list page


@login_required
def list(request):
    return render(request, 'pages/application/user/list.html')

# user grid page


@login_required
def grid(request):
    return render(request, 'pages/application/user/grid.html')

# user group page


@login_required
def group(request):
    return render(request, 'pages/application/user/group.html')

# user add page


@login_required
def add(request):
    return render(request, 'pages/application/user/add.html')

# user table page


@login_required
def table(request):
    return render(request, 'pages/application/user/table.html')

# contact grid page


@login_required
def contactGrid(request):
    return render(request, 'pages/application/contact/grid.html')

# contact list page


@login_required
def contactList(request):
    return render(request, 'pages/application/contact/list.html')

# contact create page


@login_required
def contactCreate(request):
    return render(request, 'pages/application/contact/create.html')

# note page


@login_required
def note(request):
    return render(request, 'pages/application/note/note.html')

# todo page


@login_required
def todo(request):
    return render(request, 'pages/application/todo/todo.html')

# kanban page


@login_required
def kanban(request):
    return render(request, 'pages/application/kanban/kanban.html')

# import page


@login_required
def importPage(request):
    return render(request, 'pages/application/import_export/import.html')

# export page


@login_required
def exportPage(request):
    return render(request, 'pages/application/import_export/export.html')

# export selected page


@login_required
def exportSelectedPage(request):
    return render(request, 'pages/application/import_export/export_selected.html')

# file manager page


@login_required
def filemanager(request):
    return render(request, 'pages/application/filemanager/filemanager.html')

# task app page


@login_required
def task(request):
    return render(request, 'pages/application/task/task.html')

# bookmark page


@login_required
def bookmark(request):
    return render(request, 'pages/application/bookmark/bookmark.html')

# social profile page


@login_required
def profile(request):
    return render(request, 'pages/application/social/profile.html')

# social profile settings page


@login_required
def profileSettings(request):
    return render(request, 'pages/application/social/settings.html')

# social profile timeline page


@login_required
def timeline(request):
    return render(request, 'pages/application/social/timeline.html')

# social profile activity page


@login_required
def activity(request):
    return render(request, 'pages/application/social/activity.html')

# support ticket page


@login_required
def ticket(request):
    return render(request, 'pages/application/support/ticket.html')

# support ticket details page


@login_required
def details(request):
    return render(request, 'pages/application/support/details.html')

# support new ticket page


@login_required
def newTicket(request):
    return render(request, 'pages/application/support/new.html')

# job search page


@login_required
def jobSearch(request):
    return render(request, 'pages/application/job/search.html')

# job search list page


@login_required
def jobSearchList(request):
    return render(request, 'pages/application/job/search_list.html')

# job details page


@login_required
def jobDetails(request):
    return render(request, 'pages/application/job/details.html')

# job apply page


@login_required
def jobApply(request):
    return render(request, 'pages/application/job/apply.html')

# basic table page


@login_required
def basicTable(request):
    return render(request, 'pages/application/table/basic.html')

# data table page


@login_required
def datatable(request):
    return render(request, 'pages/application/table/data.html')

    # dynamic table page


@login_required
def dynamicTable(request):
    return render(request, 'pages/mixed/dynamic_table.html')
