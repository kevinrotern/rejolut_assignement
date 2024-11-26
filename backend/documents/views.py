from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os
import PyPDF2

@csrf_exempt
def upload_document(request):
    if request.method == 'POST' and request.FILES['document']:
        file = request.FILES['document']
        file_extension = file.name.split('.')[-1].lower()
        file_path = default_storage.save(f"document1/{file.name}", file)
        if file_extension == 'pdf':
            try:
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    content = ''.join([page.extract_text() for page in reader.pages])
            except Exception as e:
                return JsonResponse({'status': 'failed', 'message': 'Error processing PDF'})
        elif file_extension == 'txt':
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                return JsonResponse({'status': 'failed', 'message': 'Error processing text file'})
        else:
            return JsonResponse({'status': 'failed', 'message': 'Unsupported file format'})
        return JsonResponse({'status': 'success', 'content': content})

    return JsonResponse({'status': 'failed', 'message': 'Invalid request'})
