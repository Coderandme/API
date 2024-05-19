Overview - 

This project is a simple Flask web application that fetches responses and their associated sources from the API given.
It Identifes whether the response for each response-sources pair came from any of the given sources and then it lists
down the sources from which the response was formed. 

Files and their Information

1. index.html - 
   Purpose: This is the HTML template for the web application's front-end. It uses Bootstrap for styling and is
   responsible for displaying the responses and their corresponding sources in a user-friendly format. Please note that this file should be inside a folder called templates.

2. app.py -
   Purpose: This file contains the Flask application that serves the web interface and handles routing. It 
   initializes the Flask app, sets up routes for rendering the main page, and integrates with the Sentence 
   Transformer model to process data and calculate similarities.

3. get_data.py -
   Purpose: This file fetches data from the provided API endpoint and preprocesses it for use
   with the Sentence Transformer model. It ensures that the data is in the correct format for embedding and 
   similarity calculations.

4. llm.py -
   Purpose: This file contains the core logic for using the Sentence Transformer model to encode responses and
   sources, and to calculate the similarities between them. It defines functions to generate embeddings, compute
   cosine similarities, and determine which sources are relevant to each response based on a similarity threshold.

5. requirements.txt - 
   Purpose: This file lists all the necessary Python packages required to run the application. It ensures that the
   correct dependencies are installed in the environment, such as Flask and Sentence Transformers.
  
