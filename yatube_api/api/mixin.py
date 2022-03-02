from rest_framework import mixins, viewsets


class FollowMixinViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    """Mixin для подписок."""
    pass
