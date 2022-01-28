from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView






from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework.decorators import api_view

# Create your views here.
'''def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)
    
def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project.html', context)'''

def index(request):
    print("------------------------- I AM HERE")
    queryset = Project.objects.all()
    return render(request, "projects/index.html", {'projects': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/index.html'

    def get(self, request):
        queryset = Project.objects.all()
        return Response({'projects': queryset})


class list_all_projects(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects/index.html'

    def get(self, request):
        queryset = Project.objects.all()
        return Response({'projects': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            projects = projects.filter(title__icontains=title)

        projects_serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(project_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(project_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Project.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Projects were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return JsonResponse({'message': 'The project does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        project_serializer = ProjectSerializer(project)
        return JsonResponse(project_serializer.data)

    elif request.method == 'PUT':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(project, data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(project_serializer.data)
        return JsonResponse(project_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return JsonResponse({'message': 'Project was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def project_list_published(request):
    projects = Project.objects.filter(published=True)

    if request.method == 'GET':
        projects_serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)

