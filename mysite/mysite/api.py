from rest_framework import routers
from rental import views as myapp_views

router = routers.DefaultRouter()
router.register(r'friends', myapp_views.FriendViewset)
router.register(r'belongings', myapp_views.BelongingViewset)
router.register(r'borrowings', myapp_views.BorrowedViewset)
router.register(r'movies', myapp_views.MovieViewset)
router.register(r'categories', myapp_views.CategoryViewset)

