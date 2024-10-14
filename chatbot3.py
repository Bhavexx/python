# Import the required libraries
import random
Name=input("what is your name")
print("my name is ",Name)
# Define a dictionary with responses to common medical questions
responses = {
    'how are you': ['I\'m feeling a bit under the weather.', 'I\'ve been experiencing some symptoms.', 'I\'m not feeling well.'],
    'what brings you here today': ['I have a fever.', 'I\'ve been experiencing chest pain.', 'I have a rash.'],
    'where does it hurt': ['My head is hurting.', 'I have a pain in my chest.', 'My stomach hurts.'],
    'how long have you been feeling this way': ['A few days.', 'A week or so.', 'For a few months.'],
    'default': ['Sorry, I didn\'t understand that.', 'Can you please rephrase?', 'I\'m not sure what you mean.']
}

# Define a dictionary with medicine prescriptions
medicines = {
    'fever': 'Paracetamol',
    'chest pain': 'Aspirin',
    'rash': 'Hydrocortisone cream',
    'headache': 'Ibuprofen',
    'stomach pain': 'Antacid'
}

# Define a function to get a response from the doctor chatbot
def get_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    return random.choice(responses['default'])

# Define a function to get a medicine prescription
def get_medicine(user_input):
    user_input = user_input.lower()
    for keyword in medicines:
        if keyword in user_input:
            return medicines[keyword]
    return 'Unknown medicine'

# Define a function to start the doctor chatbot
def start_doctor_chatbot():
    print('Welcome to the doctor\'s office!')
    print('Please answer the doctor\'s questions to the best of your ability.')
    while True:
        user_input = input('Doctor: How are you today? ')
        if user_input.lower() == 'quit':
            break
        print('You:', user_input)
        print('Doctor:', get_response(user_input))
        print('Doctor: What brings you here today? ')
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        print('You:', user_input)
        print('Doctor:', get_response(user_input))
        print('Doctor: Where does it hurt? ')
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        print('You:', user_input)
        print('Doctor:', get_response(user_input))
        print('Doctor: How long have you been feeling this way? ')
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        print('You:', user_input)
        print('Doctor:', get_response(user_input))
        medicine = get_medicine(user_input)
        print('Doctor: Based on your symptoms, I\'m going to prescribe you {}.'.format(medicine))
        print('Doctor: Please take two tablets of {} every 4 hours and rest for the next 24 hours.'.format(medicine))
        print('Doctor: You should start feeling better soon. If your symptoms persist, please come back and see me.')
        print(Name,"meet me asap when you not feeling well")
        break

# Start the doctor chatbot
start_doctor_chatbot()