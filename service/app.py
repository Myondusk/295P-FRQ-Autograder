from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Free Response Autograder", 
		  description = "Score student responses automatically")

model = app.model('Prediction params', 
				  {'kwField': fields.String(required = True, 
				  							   description="Scoring Guidelines", 
    					  				 	   help="Enter keywords, comma separated, spaces separate synonyms"),
					'rField': fields.String(required = True, 
				  							   description="Student Response", 
    					  				 	   help="Enter answer"),
				  })

@app.route("/prediction")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add('Access-Control-Allow-Origin', "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@app.expect(model)		
	def post(self):
		kws = []
		rs = []

		def is_kw(word):
			for wordset in kws:
				if word in wordset:
					return True
			return False

		try: 
			formData = request.json
			kws = formData['kwField'].split(",")
			kws = [ [words.strip() for words in wordset.split()] for wordset in kws]
			rs = formData['rField'].split()
			data = [word for word in rs if is_kw(word)]
			if data == []:
				data = "No keywords found in response"
			else:
				data = "Keywords found: " + str(data) + "\n(" + str(min(100, 100.00*(len(data)/len(kws)))) + "%)"

			response = jsonify({
				"statusCode": 200,
				"status": "Response evaluated",
				"result": data
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response

		except Exception as error:
			print("Error")
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})