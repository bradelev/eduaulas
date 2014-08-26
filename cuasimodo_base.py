def send_data(area, topic, exercise_id, result, answers, is_teacher, time=0.0):
    global serial
    if serial == "":
        serial = "TEST"
    try:
        area = area.capitalize()
        subject = json.loads(__generic_send__('GET','/api/%s/subject/?name=%s&format=json'%(api_version,area),{})).get('objects')
        subject_id = subject[0].get('id')
        person_query = __generic_send__('GET','/api/%s/person/?serial=%s&format=json'%(api_version,serial),{})
        person = json.loads(person_query).get('objects')
        person_id = person[0].get('id')
        exercise = json.loads(__generic_send__('GET','/api/%s/exercise/?cuasimodo_exercise_id=%s&unit__letter=%s&unit__subject=%s&format=json'%(api_version, exercise_id, topic, subject_id),{})).get('objects')
        exercise_id = exercise[0].get('id')
        send_data = __generic_send__('POST', '/api/%s/result/'%api_version, {'points':result,'answer':answers,'exercise':'/api/v1/subject/%s/'%exercise_id,'person':'/api/v1/person/%s/'%person_id,'time_elapsed':time})
        return True
    except:
        return False

def send_student(name, last_name, dob, code_class, gender):
    global serial
    try:
        send_student = __generic_send__('POST', '/api/%s/student/'%api_version, {'name': name,'last_name':last_name, 
            'date_of_birth':dob, 'class_room':'/api/%s/classroom/%s/'%(api_version, code_class), 'gender':gender})
        return True
    except:
        return False


def __generic_send__(method, path, data):
    global server
    global port

    try:
        conn = httplib.HTTPConnection(server, port)
        params = json.dumps(data)
        conn.request(method, path, params, {"Content-Type": "application/json"})
        response = conn.getresponse()
        dict_response = response.read()
        
        conn.close()
        return dict_response
    except:
        return False