from sentence_transformers import SentenceTransformer, util
import numpy as np
import get_data

class Lmm:

    def mapping_function(self):
        # Define a similarity threshold (this value can be tuned)
        similarity_threshold = 0.5
        
        data_list=[]
        obj = get_data.GetData()
        list_dir = obj.process_api_data('https://devapi.beyondchats.com/api/get_message_with_sources')

        # Initialize the model
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


        for item in list_dir:
            citations = []
            sources = item['sources']
            response = item['response']
            # Extract contexts
            source_texts = [source['context'] for source in sources]

            # Encode responses and sources
            response_embeddings = model.encode(response)
            source_embeddings = model.encode(source_texts)

            # Compute cosine similarities
            cosine_similarities = util.pytorch_cos_sim(response_embeddings, source_embeddings)

            # Get the matching sources
            for i in range(len(response)):
                for j in range(len(sources)):
                    similarity = cosine_similarities[i][j].item()
                    if similarity >= similarity_threshold:
                        citations.append({
                            "id": sources[j]["id"],
                            "link": sources[j]["link"]
                        }) 
            data_list.append({'response' : response[0], 'source':citations})

        return data_list

# For debugging 
# obj = Lmm()
# result = obj.mapping_function()
# print(result)


            

   











