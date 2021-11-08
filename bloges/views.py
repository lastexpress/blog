from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from slider.models import Slider
from features.models import Features
from gallery.models import Category, Photo
from django.urls import reverse
from offer.models import ReloadTitle, ReloadTitleDesc
from buildws.models import BuildWebsite, BuildButton, MainImage
from fmblog.models import FmBlog, Comment, PublishedManager, ChangeTitle, ChangeTitleCategory, CategoryList
from price.models import PriceChangedTitle, PriceChanged
from team.models import TeamMainTitle, TeamBox
from bloges.models import ChangeHeader, ChangeFooter, ChangeFooterTitleGallery, ChangeFooterGallery
from pagebanner.models import PageBanner
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag

def IndexView(request):
	#Хеадер
	header_phone = ChangeHeader.objects.get(pk=1)

	#Слайдер
	slider_list = Slider.objects.all()

	#Замена функций
	features_all = Features.objects.all()
	features_1 = Features.objects.get(pk=1)
	features_2 = Features.objects.get(pk=2)
	features_3 = Features.objects.get(pk=3)
	features_4 = Features.objects.get(pk=4)
	features_5 = Features.objects.get(pk=5)
	features_6 = Features.objects.get(pk=6)

	#Категории для галлереи
	category = None
	categories = Category.objects.all()
	category_car = Category.objects.in_bulk(['car'], field_name='slug')
	photo_car = Photo.objects.filter(category__name='car')
	photo_girl = Photo.objects.filter(category__name='girls')
	photo_mushrooms = Photo.objects.filter(category__name='mushroms')
	photo_people = Photo.objects.filter(category__name='people')

	#Что мы предлагаем
	off_re_title = ReloadTitle.objects.get(pk=1)

	#Карточки
	rtd_1_title = ReloadTitleDesc.objects.get(pk=1)
	rtd_2_title = ReloadTitleDesc.objects.get(pk=2)
	rtd_3_title = ReloadTitleDesc.objects.get(pk=3)

	#Buildws
	build_txt = BuildWebsite.objects.get(pk=1)
	build_btn = BuildButton.objects.all()
	build_img = MainImage.objects.get(pk=1)

	#Blog
	ch_title = ChangeTitle.objects.get(pk=1)

	posts = FmBlog.published.all()

	#Price and plans
	price_main_title = PriceChangedTitle.objects.get(pk=1)
	price_title = PriceChanged.objects.get(pk=1)
	price_title_2 = PriceChanged.objects.get(pk=2)
	price_title_3 = PriceChanged.objects.get(pk=3)

	#Team
	team_title = TeamMainTitle.objects.get(pk=1)
	team_info_1 = TeamBox.objects.get(pk=1)
	team_info_2 = TeamBox.objects.get(pk=2)
	team_info_3 = TeamBox.objects.get(pk=3)
	team_info_4 = TeamBox.objects.get(pk=4)
	team_info_5 = TeamBox.objects.get(pk=5)
	team_info_6 = TeamBox.objects.get(pk=6)
	team_info_7 = TeamBox.objects.get(pk=7)
	team_info_8 = TeamBox.objects.get(pk=8)

	#Footer
	footer_content = ChangeFooter.objects.get(pk=1)


	#Flicker Gallery
	#title
	flick_name = ChangeFooterTitleGallery.objects.get(pk=1)
	
	#image
	flick_img = ChangeFooterGallery.objects.all()
	
	dic_obj = {'header_phone' : header_phone,
			   'slider_list':slider_list,
			   'features_all' : features_all,
			   'features_1' : features_1,
			   'features_2' : features_2, 'features_3' : features_3,
			   'features_4' : features_4, 'features_5' : features_5, 'features_6' : features_6,
			   'categories' : categories,
			   'category_car' : category_car,
			   'photo_car' : photo_car, 'photo_girl' : photo_girl, 'photo_mushrooms' : photo_mushrooms, 'photo_people' : photo_people,
			   'off_re_title' : off_re_title,
			   'rtd_1_title' : rtd_1_title, 'rtd_2_title' : rtd_2_title, 'rtd_3_title' : rtd_3_title,
			   'build_btn' : build_btn, 'build_txt' : build_txt, 'build_img' : build_img,
			   'ch_title' : ch_title, 'posts' : posts,
			   'price_main_title' : price_main_title,
			   'price_title' : price_title, 'price_title_2' : price_title_2, 'price_title_3' : price_title_3,
			   'team_title' : team_title,
			   'team_info_1' : team_info_1, 'team_info_2' : team_info_2, 'team_info_3' : team_info_3, 'team_info_4' : team_info_4,
			   'team_info_5' : team_info_5, 'team_info_6' : team_info_6, 'team_info_7' : team_info_7, 'team_info_8' : team_info_8,
			   'footer_content' : footer_content, 'flick_name' : flick_name, 'flick_img' : flick_img}

	return render(request, 'indexex.html', dic_obj)


def post_list(request, tag_slug=None):
	#Хеадер
	header_phone = ChangeHeader.objects.get(pk=1)


	object_list = FmBlog.published.all()

	# #ТЭГИ
	# tag = None

	# if tag_slug:
	# 	tag = get_object_or_404(Tag, slug=tag_slug)
	# 	object_list = object_list.filter(tags__in=[tag])


	#ПАГИНАЦИЯ
	paginator = Paginator(object_list, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	#Посты
	obj_post = FmBlog.published.filter().order_by('-publish')[:4]

	#Заголовок категорий
	category_title = ChangeTitleCategory.objects.get(pk=1)

	category_name = CategoryList.objects.all()

	#titlebanner
	banner_title = PageBanner.objects.get(pk=1)

	#Footer
	footer_content = ChangeFooter.objects.get(pk=1)

	#Flicker Gallery
	#title
	flick_name = ChangeFooterTitleGallery.objects.get(pk=1)
	
	#image
	flick_img = ChangeFooterGallery.objects.all()

	dict_obj = {'header_phone' : header_phone,
				'page' : page,
				'posts' : posts,
				'category_title' : category_title, 'category_name' : category_name,
				'banner_title' : banner_title,
				'footer_content' : footer_content,
				'flick_name' : flick_name,
				'flick_img' : flick_img,
				'obj_post' : obj_post,
				# 'tag' : tag,
				'object_list' : object_list}

	return render(request, 'blog/main_direct.html', dict_obj)

# def post_list_by_tag(request, tag_slug=None):

# 	#ТЭГИ
# 	tag = None

# 	if tag_slug:
# 		tag = get_object_or_404(Tag, slug=tag_slug)
# 		object_list = object_list.filter(tags__in=[tag])

# 	dict_obj = {'tag' : tag}

# 	return render(request, 'blog/main_direct.html', dict_obj)


def category_list(request, slug):
	
	#Хеадер
	header_phone = ChangeHeader.objects.get(pk=1)
	
	#Заголовок категорий
	category_title = ChangeTitleCategory.objects.get(pk=1)
	category_one = CategoryList.objects.filter(slug='for-girl')

	category_two = CategoryList.objects.get(slug=slug)
	post = FmBlog.objects.filter(category=category_two)
	last_postest = FmBlog.objects.filter(category=category_two)[:4]

	category_name = CategoryList.objects.all()


	object_list = FmBlog.published.all()
	#ПАГИНАЦИЯ
	paginator = Paginator(last_postest, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	#titlebanner
	banner_title = PageBanner.objects.get(pk=1)

	#Footer
	footer_content = ChangeFooter.objects.get(pk=1)

	#Flicker Gallery
	#title
	flick_name = ChangeFooterTitleGallery.objects.get(pk=1)
	
	#image
	flick_img = ChangeFooterGallery.objects.all()

	dictonary_object = {'header_phone' : header_phone,
						'category_one' : category_one, 'category_two' : category_two,
						'category_title' : category_title, 
						'post' : post,
						'banner_title' : banner_title,
						'footer_content' : footer_content,
						'flick_name' : flick_name,
						'flick_img' : flick_img,
						'category_name' : category_name,
						'last_postest' : last_postest,
						'posts' : posts, 'page' : page}

	return render(request, 'blog/post/category_direct1.html', dictonary_object)

# def category_detail(request, slug):
# 	queryset = CategoryList.objects.filter(username=slug)
# 	category = get_object_or_404(queryset, slug=slug)
# 	return render(request, 'blog/post/category_detail', {'category' : category})


def post_detail(request, year, month, day, post):
	post = get_object_or_404(FmBlog, slug=post,
									 status='published',
									 publish__year=year,
									 publish__month=month,
									 publish__day=day)

	comments = post.comments.filter(active=True)

	new_comment = None

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()

	header_phone = ChangeHeader.objects.get(pk=1)
	category_title = ChangeTitleCategory.objects.get(pk=1)
	category_name = CategoryList.objects.all()

	recent_posts = FmBlog.objects.all()[:3]

	#titlebanner
	banner_title = PageBanner.objects.get(pk=1)

	#Footer
	footer_content = ChangeFooter.objects.get(pk=1)

	#Flicker Gallery
	#title
	flick_name = ChangeFooterTitleGallery.objects.get(pk=1)
	
	#image
	flick_img = ChangeFooterGallery.objects.all()

	dict_obj = {'post' : post,
				'header_phone' : header_phone,
				'category_title' : category_title,
				'category_name' : category_name,
				'footer_content' : footer_content,
				'flick_name' : flick_name,
				'flick_img' : flick_img,
				'banner_title' : banner_title,
				'recent_posts' : recent_posts,
				'comments' : comments, 'new_comment' : new_comment, 'comment_form' : comment_form}

	return render(request, 'blog/post/blog_single_direct.html', dict_obj)


def post_share(request, post_id):
	post = get_object_or_404(FmBlog, id=post_id, status='published')
	sent = False

	if request.method == 'Post':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get.get_absolute_url())
			subject = f"{cd['name']} рекомендации ты читаешь" f"{post.title}"
			message = f"Читай {post.title} в {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
			send_mail(subject, message, 'admin@myblog.com', [cd['to']])
			sent = True
	else:
		form = EmailPostForm()

	#Хеадер
	header_phone = ChangeHeader.objects.get(pk=1)

	#Footer
	footer_content = ChangeFooter.objects.get(pk=1)

	#Flicker Gallery
	#title
	flick_name = ChangeFooterTitleGallery.objects.get(pk=1)
	
	#image
	flick_img = ChangeFooterGallery.objects.all()

	dic_obj = {'post' : post,
			   'form' : form,
			   'sent' : sent,
			   'header_phone' : header_phone,
			   'footer_content' : footer_content,
			   'flick_name' : flick_name,
			   'flick_img' : flick_img}

	return render(request, 'blog/post/share.html', dic_obj)




# class IndexView(TemplateView):
# 	slider_list = Slider.objects.all()
# 	dic_obj = {'slider_list':slider_list}
# 	template_name = 'indexex.html'

# class BlogView(TemplateView):
# 	template_name = 'blog/blog.html'

# class BlogSingleView(TemplateView):
# 	template_name = 'blog/blog-single.html'