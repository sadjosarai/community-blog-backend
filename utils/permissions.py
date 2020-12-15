from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the owner of this object"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsPublish(BasePermission):
    message = "This item not found"
    status = ['published', 'Published']
    
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS and obj.status in self.status

class FormationHasPublish(BasePermission):
    message = "This item izoefje not found"
    status = ['published', 'Published']
    
    def has_object_permission(self, request, view, obj):
        return request.method == SAFE_METHODS and obj.formation.status == self.status

class IsAdminFormation(BasePermission):
    message = "You must be the owner of this object"

    def has_object_permission(self, request, view, obj):
        return request.method in ['POST', 'PUT'] and obj.formation.user == request.user

class IsNotPublish(BasePermission):
    message = "This item not found"
    status = ['published', 'Published']
    
    def has_object_permission(self, request, view, obj):
        return not (request.method in SAFE_METHODS and obj.status in self.status)
