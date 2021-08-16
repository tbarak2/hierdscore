from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

# Create your views here.
class GetData(APIView):
    def get(self, request, format=None):
        my_response = []
        response = requests.get("https://hs-resume-data.herokuapp.com/v3/candidates/all_data_b1f6-acde48001122")
        for resp in  response.json():
            candidate = {}
            candidate['CANDIDATE_NAME'] = resp['contact_info']['name']['formatted_name']
            candidate['experience'] = []
            for exp in resp['experience']:
                experience = {}

                experience['JOB_TITLE'] = exp['title']
                if not exp['current_job']:
                    experience['START_DATE'] =exp['start_date']
                    experience['END_DATE']=exp['end_date']
                else:
                    experience['START_DATE'] =exp['start_date']
                    experience['END_DATE']=exp['end_date']
                candidate['experience'].append(experience)
            my_response.append(candidate)
        return Response(my_response)