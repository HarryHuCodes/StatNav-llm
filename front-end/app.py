from flask import Flask, request, jsonify, render_template
import retrieving_data

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the HTML interface
    return render_template('index.html')

@app.route('/search_companies', methods=['POST'])
def search_companies():
    data = request.get_json()
    company_name = data.get('companyName')
    companies = retrieving_data.get_companies_by_company_name(company_name)
    return jsonify(companies)

@app.route('/search_documents', methods=['POST'])
def search_documents():
    data = request.get_json()
    cik = data.get('cik')
    documentType = data.get('documentType')
    documents = retrieving_data.get_document_dates(cik, documentType)
    return jsonify(documents)

if __name__ == "__main__":
    app.run(debug=True)
