from src.views.http_types.http_response import HttpResponse

def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Internal server error",
                "description": str(error)
            }]
        }
    )
