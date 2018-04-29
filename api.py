# Import libraries
import flask 
import perfect_numbers 

# Create flask app
app = flask.Flask(__name__)

# Define API
@app.route('/classify-perfect-number')
def api():

	# PCreate dictionary for results so they can be returned as a json object
	result = {}
	# Take query from the URL
	query = flask.request.args.get('number')

    # Return just an error when there is no query
	if query is None:
		query['error'] = 'no input found'

	if query is not None:
		# Append the classification to the result dictionary if possible 
		try:
			result['classification'] = perfect_numbers.classify(query)
		# Return an error if the input is not an integer 
		except perfect_numbers.InvalidInputException as e:
			result['error'] = str(e)
		# Return an error if the input is 0 or negative 
		except perfect_numbers.NumberException as e:
			result['error'] = str(e)
	result['input'] = query

	return flask.jsonify(result)
