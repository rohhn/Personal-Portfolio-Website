from photography.models import Image, Genre, Album
from django.core.paginator import Paginator


def get_all_images():
    images = Image.objects.all().order_by("-posted_on")
    return images


def get_images_by_genre(genre, paginate=False, page_no=1, n=9):
    genre_obj = Genre.objects.get(id=genre)
    images = Image.objects.filter(genre=genre_obj).order_by('-posted_on')

    if paginate:
        paginator = Paginator(images, per_page=n, allow_empty_first_page=True)
        requested_page = paginator.get_page(page_no)

        response = {
            "data": requested_page.object_list,
            "page_details": {
                "current_page": requested_page.number,
                "currently_loaded": genre,
                "has_next": requested_page.has_next(),
                "has_previous": requested_page.has_previous(),
                "next_page": requested_page.next_page_number() if requested_page.has_next() else None
            }
        }
    else:
        response = {
            "data": images
        }

    return response


def get_images_by_album(album_id, paginate=False, page_no=1, n=9):
    album_obj = Album.objects.get(id=album_id)
    images = Image.objects.filter(genre=album_obj).order_by('-posted_on')

    if paginate:
        paginator = Paginator(images, per_page=n, allow_empty_first_page=True)
        requested_page = paginator.get_page(page_no)

        response = {
            "data": requested_page.object_list,
            "page_details": {
                "current_page": requested_page.number,
                "currently_loaded": album_id,
                "has_next": requested_page.has_next(),
                "has_previous": requested_page.has_previous(),
                "next_page": requested_page.next_page_number() if requested_page.has_next() else None
            }
        }
    else:
        response = {
            "data": images
        }

    return response


def get_featured_images(paginate=False, page_no=1, n=9):

    images = Image.objects.filter(feature=True).order_by('-posted_on')

    if paginate:
        paginator = Paginator(images, per_page=n, allow_empty_first_page=True)
        requested_page = paginator.get_page(page_no)

        response = {
            "data": requested_page.object_list,
            "page_details": {
                "current_page": requested_page.number,
                "currently_loaded": "featured",
                "has_next": requested_page.has_next(),
                "has_previous": requested_page.has_previous(),
                "next_page": requested_page.next_page_number() if requested_page.has_next() else None
            }
        }
    else:
        response = {
            "data": images
        }

    return response
