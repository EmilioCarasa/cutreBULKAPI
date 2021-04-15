from flask import Flask, request
from boto.connection import HTTPRequest

from handle_luk_request.use_cases.generate_bulk_import_use_case import GenerateBulkImportUseCase

app = Flask(__name__)


@app.route('/')
def bulk_request():
    company = request.form.get('Company')
    token = request.form.get('Token')
    data = request.form.get('file_input')

    if CheckTokenUseCase(company, token):
        use_case = GenerateBulkImportUseCase(company, data)
        use_case.run() #Aquí spliteo y llamo a otro microservicio
        return HTTPRequest("Bulk process created", use_case.id_bulk_process)
    else:
        return HTTPRequest("Error")

if __name__ == '__main__':
    app.run()
