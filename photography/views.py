import random

from django.http.response import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.core.paginator import Paginator

from .models import *
from .src import gallery_actions


def get_navbar_elements(request):
    """
    Return a list of all menu items required for the Navbar
    """
    travel_diaries = TravelDiary.objects.filter(publish=True).order_by("-travel_date")[:5]
    projects = Project.objects.all().order_by("-publish_date")[:5]

    all_genres = Genre.objects.all()
    response = {
        'travel_diaries': travel_diaries,
        'gallery_options': all_genres,
        'all_projects': projects
    }
    return response


def handler404(request, exception):
    response = render(request, 'photography/error_pages/404.html', status=404)
    return response


def handler500(request):
    response = render(request, 'photography/error_pages/500.html', status=500)
    return response


def landing_page_view(request):
    # Randomly list featured images
    landing_page_images = LandingImage.objects.filter(active=True).order_by('?')[:3]

    context = {
        'navbar_elements': get_navbar_elements(request),
        'featured_images': landing_page_images
    }
    return render(request, 'photography/index.html', context)


def about_page_view(request):
    profile_photos = ProfilePhoto.objects.filter(active=True).order_by('?')
    background_image = profile_photos[random.randint(0, profile_photos.count() - 1)]
    profile_photos = profile_photos[:5]

    context = {
        'navbar_elements': get_navbar_elements(request),
        'background_image': background_image,
        'profile_photos': profile_photos
    }
    return render(request, 'photography/about.html', context)


def single_diary_view(request, diary_id):
    try:
        diary = TravelDiary.objects.get(id=diary_id)
        # if not diary.publish:
        #     return handler404(request, "404 error")
    except diary.DoesNotExist:
        return handler404(request, "404 error")
    context = {
        'diary': diary,
        'navbar_elements': get_navbar_elements(request)
    }
    return render(request, 'photography/travel_diaries/single_diary.html', context)


def all_diaries_view(request):
    page_no = request.GET.get("page", 1)
    all_diaries = TravelDiary.objects.filter(publish=True).order_by('-travel_date')

    paginator = Paginator(all_diaries, per_page=3)
    requested_page = paginator.get_page(page_no)

    response = {
        "all_diaries": requested_page.object_list,
        "page": {
            "current": requested_page.number,
            "has_next": requested_page.has_next(),
            "has_previous": requested_page.has_previous(),
        },
        'navbar_elements': get_navbar_elements(request)
    }

    return render(request, 'photography/travel_diaries/all_diaries.html', response)


def single_project_view(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except project.DoesNotExist:
        return handler404(request, "404 error")
    context = {
        'project': project,
        'navbar_elements': get_navbar_elements(request)
    }
    return render(request, 'photography/project_pages/single_project.html', context)


def all_projects_view(request):
    page_no = request.GET.get("page", 1)
    all_projects = Project.objects.all().order_by('-publish_date')

    paginator = Paginator(all_projects, per_page=4)
    requested_page = paginator.get_page(page_no)

    response = {
        "all_projects": requested_page.object_list,
        "page": {
            "current": requested_page.number,
            "has_next": requested_page.has_next(),
            "has_previous": requested_page.has_previous(),
        },
        'navbar_elements': get_navbar_elements(request)
    }

    return render(request, 'photography/project_pages/all_projects.html', response)


def make_image_grid(images):
    """
    Create the image grid to show in gallery

    Add this to add a caption to the images
    '''<div class="work-caption font-alt">
        <h3 class="work-title">{image.title}</h3>
        <div class="work-descr">{image.album.name}</div>
    </div>'''
    """

    html_content = []
    for image in images:
        html_content.append(
            f"""
            <li class="work-item gallery-item">
              <a class="gallery" title="{image.title}" href="{image.image.url}">
                <div class="work-image"><img src="{image.thumbnail.url}" alt="Portfolio Item"/></div>
              </a>
            </li>"""
        )
    html_content = "\n".join(html_content)

    return html_content


def gallery_page_view(request):

    all_genres = Genre.objects.all()
    selected_genre_id = request.GET.get("filter", "featured")
    paginate = bool(request.GET.get("paginate", True))
    page_no = int(request.GET.get("page_no", 1))

    if selected_genre_id == "featured":
        response = gallery_actions.get_featured_images(paginate=paginate, page_no=page_no, n=6)
    else:
        response = gallery_actions.get_images_by_genre(selected_genre_id, paginate=paginate, page_no=page_no, n=6)

    grid_only = bool(request.GET.get("grid_only", False))

    if not grid_only:
        context = {
            'genres': all_genres,
            'image_grid_html': make_image_grid(response["data"]),
            'navbar_elements': get_navbar_elements(request),
            'page_details': response.get('page_details', None)
        }

        return render(request, 'photography/gallery_pages/gallery.html', context)

    else:
        final_resp = {
            "image_grid_html": make_image_grid(response["data"]),
            "page_details": response.get('page_details', None)
        }
        return JsonResponse(final_resp)  # HttpResponse(final_resp)
