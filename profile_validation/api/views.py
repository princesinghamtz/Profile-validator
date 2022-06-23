from fuzzywuzzy import fuzz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Duplicate_profile
from .serializers import Duplicate_profileSerializer

# This is Api view for find Duplicate Profile
@api_view(['POST'])
def validate_profile(request):
    pro_1 = convert_in_dict(request.data['profile1'])
    pro_2 = convert_in_dict(request.data['profile2'])
    score = 0
    matching_attributes = []
    non_matching_attributes = []
    ignored_attributes = []
    if (fuzz.ratio(pro_1['first_name']+pro_1['last_name']+pro_1['email']
            , pro_2['first_name']+pro_2['last_name']+pro_2['email']) > 80):
        score = score+1
    if pro_1['first_name'] == pro_2['first_name']:
        matching_attributes.append('first_name')
    else:
        non_matching_attributes.append('first_name')

    if pro_1['last_name'] == pro_2['last_name']:
       matching_attributes.append('last_name')
    else:
        non_matching_attributes.append('last_name')

    if pro_1['email'] == pro_2['email']:
         matching_attributes.append('email')
    else:
         non_matching_attributes.append('email')


    if pro_1['class_year'] != 'None' and pro_2['class_year'] != 'None':
        if pro_1['class_year'] == pro_2['class_year']:
            score = score+1
            matching_attributes.append('class_year')
        else:
            score = score-1
            non_matching_attributes.append('class_year')

    else:
        ignored_attributes.append('class_year')

    if pro_1['date_of_birth'] != 'None' and pro_2['date_of_birth'] != 'None':
        if pro_1['date_of_birth'] == pro_2['date_of_birth']:
            matching_attributes.append('date_of_birth')
            score = score+1

        else:
            non_matching_attributes.append('date_of_birth')
            score = score-1

    else:
        ignored_attributes.append('date_of_birth')

    if score > 1:
        profile_obj = Duplicate_profile.objects.create(profile1=pro_1['id'], profile2=pro_2['id'], total_match_score=score,
                                                       matching_attributes=','.join(matching_attributes), non_matching_attributes=','.join(non_matching_attributes),
                                                       ignored_attributes=','.join(ignored_attributes))
        profile_obj.save()
        serializer = Duplicate_profileSerializer(profile_obj)
        return Response(serializer.data)

#This Function convert the input into json
def convert_in_dict(profile):
    ini_string1 = profile[1:-1]
    final_str = ini_string1.replace("'", "").replace("’", "").replace(" ‘", "").replace(" ", "")
    res = dict(item.split(":") for item in final_str.split(","))
    return res
