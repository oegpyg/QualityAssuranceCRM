from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('email/inbox', views.inbox, name='inbox'),
    path('email/read', views.read, name='read'),
    path('chat', views.chat, name='chat'),
    path('ecommerce/products', views.products, name='products'),
    path('ecommerce/product/details',
         views.productDetails, name='product_details'),
    path('ecommerce/product/add', views.addProduct, name='product_add'),
    path('ecommerce/cart', views.cart, name='cart'),
    path('ecommerce/orders', views.orders, name='orders'),
    path('ecommerce/sellers', views.sellers, name='sellers'),
    path('ecommerce/invoices', views.invoices, name='invoices'),
    path('project/list', views.projectList, name='project_list'),
    path('project/details/<int:pk>/',
         views.projectDetails, name='project_details'),
    path('project/add', views.projectAdd, name='project_add'),

    path('release/list', views.releaseList, name='release_list'),
    path('release/details/<int:pk>/',
         views.releaseDetails, name='release_details'),
    path('release/add', views.releaseAdd, name='release_add'),

    path('task/list', views.taskList, name='task_list'),
    path('task/details/<int:pk>/',
         views.taskDetails, name='task_details'),
    path('task/add', views.taskAdd, name='task_add'),

    path('testejecution/list', views.testejecutionList, name='testejecution_list'),
    path('testejecution/details/<int:pk>/',
         views.testejecutionDetails, name='testejecution_details'),
    path('testejecution/add', views.testejecutionAdd, name='testejecution_add'),

    path('casetest/list', views.casetestList, name='casetest_list'),
    path('casetest/details/<int:pk>/',
         views.casetestDetails, name='casetest_details'),
    path('casetest/add', views.casetestAdd, name='casetest_add'),


    path('casetestdoc/list', views.casetestdocList, name='casetestdoc_list'),
    path('casetestdoc/details/<int:pk>/',
         views.casetestdocDetails, name='casetestdoc_details'),

    path('typeoftests/list', views.typeoftestsList, name='typeoftests_list'),
    path('typeoftests/details/<int:pk>/',
         views.typeoftestsDetails, name='typeoftests_details'),

    path('typeoftests/add', views.typeoftestsAdd, name='typeoftests_add'),

    path('qadocumentation/list', views.qadocumentationList,
         name='qadocumentation_list'),
    path('qadocumentation/details/<int:pk>/',
         views.qadocumentationDetails, name='qadocumentation_details'),


    path('reportedbugs/list', views.reportedbugsList,
         name='reportedbugs_list'),
    path('reportedbugs/details/<int:pk>/',
         views.reportedbugsDetails, name='reportedbugs_details'),

    path('implementationrelease/list', views.implementationreleaseList,
         name='implementationrelease_list'),
    path('implementationrelease/details/<int:pk>/',
         views.implementationreleaseDetails, name='implementationrelease_details'),


    path('calendar', views.calendar, name='calendar'),
    path('user/team', views.team, name='team'),
    path('user/card', views.card, name='card'),
    path('user/list', views.list, name='list'),
    path('user/grid', views.grid, name='grid'),
    path('user/group', views.group, name='group'),
    path('user/add', views.add, name='add'),
    path('user/table', views.table, name='table'),
    path('contact/grid', views.contactGrid, name='contact_grid'),
    path('contact/list', views.contactList, name='contact_list'),
    path('contact/create', views.contactCreate, name='contact_create'),
    path('note', views.note, name='note'),
    path('todo', views.todo, name='todo'),
    path('kanban-board', views.kanban, name='kanban'),
    path('import_export/import', views.importPage, name='import_page'),
    path('import_export/export', views.exportPage, name='export_page'),
    path('import_export/export-selected',
         views.exportSelectedPage, name='export_selected'),
    path('filemanager', views.filemanager, name='filemanager'),
    path('task', views.task, name='task'),
    path('bookmarks', views.bookmark, name='bookmark'),
    path('social/profile', views.profile, name='profile'),
    path('social/profile-settings', views.profileSettings, name='profile_settings'),
    path('social/timeline', views.timeline, name='timeline'),
    path('social/activity', views.activity, name='activity'),
    path('support/ticket', views.ticket, name='ticket'),
    path('support/ticket-details', views.details, name='ticket_details'),
    path('support/new-ticket', views.newTicket, name='new_ticket'),
    path('job/search', views.jobSearch, name='job_search'),
    path('job/search-list', views.jobSearchList, name='job_search_list'),
    path('job/details', views.jobDetails, name='job_details'),
    path('job/apply', views.jobApply, name='job_apply'),
    path('table/basic', views.basicTable, name='basic_table'),
    path('table/data', views.datatable, name='datatable'),
    path('table/dynamic-table', views.dynamicTable, name='dynamic_table'),
]
