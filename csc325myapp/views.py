from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    """Simple health/status endpoint for the CI/CD pipeline demo."""
    return Response({"status": "ok", "service": "csc325-module8-cicd", "version": "1.1"})



@api_view(["GET"])
def hello(request):
    """Simple greeting endpoint."""
    name = request.query_params.get("name", "world")
    return Response({"message": f"Hello, {name}!"})
