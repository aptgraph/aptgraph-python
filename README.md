![Aptgraph](http://aptgraph.com/images/logo_on_grey.png)

Usage is pretty simple.

	# Get a instance of the API (while passing in your apikey)
	api = PyAptgraph('wKJtkVQ3QXoUJW5hryrFXRXDEoJhiwFmvA2KEWMSNH3AcMMPsx')

	# Add a couple of random values to this graph, then send it to Aptgraph
	# Note that 8jspy is this graphs id.
	api.add('8jspy', random.randint(1,100))
	api.add('8jspy', random.randint(1,100))
	api.send()

See Aptgraph for more details
