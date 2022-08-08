from django.http.response import JsonResponse

from django.shortcuts import render

# Create your views here.
from philosophia.lib.dto.usecases.home_usecase_request_dto import HomeUseCaseRequestDTO
from philosophia.lib.repositories.philosophia_repository import PhilosophiaRepositoryIMPL
from philosophia.lib.usecases.home_usecase import HomeUseCase


def home(request):
    return JsonResponse(HomeUseCase(repo=PhilosophiaRepositoryIMPL()).handle(
        request=HomeUseCaseRequestDTO(username=request.user.username)),safe=False)
