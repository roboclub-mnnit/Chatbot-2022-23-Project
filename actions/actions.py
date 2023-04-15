# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
import mysql

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher, Action
import webbrowser
from rasa_sdk.interfaces import Action
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher 
import spacy
import openai
from dotenv import load_dotenv
load_dotenv()
import os
class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(self, dispatcher,
        tracker: Tracker,
        domain: Dict) -> List[Dict[Text, Any]]:
        video_url="https://youtu.be/j76Z57O0Acw"
        dispatcher.utter_message(text="wait... Playing your video.")
        webbrowser.open(video_url)
        return []
# class ValidateRestaurantForm(Action):
  #  def name(self) -> Text:
  #     return "user_details_form"

   # def run(
      #   self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text -> Any]) -> List[EventType]:
   #     required_slots = ["name", "number"]

    #    for slot_name in required_slots:
         #   if tracker.slots.get(slot_name) is None:
         #       "The slot is not filled yet. Request the user to fill this slot next."
          #     return [SlotSet("requested_slot", slot_name)]

               
      #  return [SlotSet("requested_slot", None)] 
      #return []

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks", Name=tracker.get_slot("name"),Mobile_number=tracker.get_slot("number"))
        
        
class ActionImage(Action):
    def name(self) -> Text:
        return 'action_image'

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict) -> List[Dict[Text, Any]]:
        image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shiksha.com%2Funiversity%2Fmnnit-allahabad-motilal-nehru-national-institute-of-technology-24357&psig=AOvVaw2Huxtg15KnizdKpPlfMjVG&ust=1679021555456000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCICx0ea43_0CFQAAAAAdAAAAABAE"
        dispatcher.utter_message(text="Please.... wait image is upload..")
        webbrowser.open(image_url)
        return []
    
class ActionGreet(Action):
    def name(self) -> Text:
        return 'action_greet'
    
    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_message(text="MNNIT is the great campus")
        return []
    
# class ValidateRegisterForm(FormValidationAction):
#     def name(self) -> Text:
#         return 'validate_register_form'
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         return []

#     def validate_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate slot value."""
#         if not slot_value:
#          return {"utter_ask_registeremail": None}
#         else: 
#          return {"utter_ask_registeremail": slot_value}	
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_submitregister"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
	
        user_name = tracker.get_slot("registeremail")
        print("email id  is  : ",user_name) 
        
		
        dispatcher.utter_message(template="utter_details_thanks")
        return []
    
# class ActionDefaultFallback(Action):
#     # Executes the fallback action and goes back to the previous state
#     # of the dialogue

#     def name(self) -> Text:
#         return ACTION_DEFAULT_FALLBACK_NAME

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="my_custom_fallback_template")

#         # Revert user message which led to fallback.
#         return [UserUtteranceReverted()]
 
# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         # tell the user they are being passed to a customer service agent
#         dispatcher.utter_message(text="I am passing you to a human...")
     

#         return [ UserUtteranceReverted()]

# Import requests module
import requests

# Define function to call API
# def get_weather(city):
    
#     # API endpoint URL
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=<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>'
    
#     # Send request to API
#     response = requests.get(url)
    
#     # Parse response and return temperature
#     data = response.json()
#     temperature = data['main']['temp']
    
#     return temperature


# import spacy

# nlp = spacy.load('en')

# class ActionGetPersonName(Action):
#     def name(self):
#         return 'action_get_person_name'
    
#     def run(self, dispatcher, tracker, domain):
#          message = tracker.latest_message['text']
#          doc = nlp(message)
#          for ent in doc.ents:
#             if ent.label_ == 'PERSON':
#                 name = ent.text
#                 dispatcher.utter_message(f"The person's name is {name}.")
#                 return [SlotSet('person_name', name)]
            
#          dispatcher.utter_message("I couldn't find a person's name in your message.")
#          return []

# import openai
# import os
# from dotenv import load_dotenv
# load_dotenv()
# def DataUpdate(query,answer):
#     mydb=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd=os.getenv('awantbhanu@'),
#         database="chatbot"
#     )
#     mycursor=mydb.cursor()
#     # openai.api_key=os.getenv('api')
#     # completions=openai.Completion.create(engine='text-davinci-002',prompt=query,max_tokens=250)
#     # message=completions.choices[0].text
#     # message2=message.splitlines()
#     # answer=message2[-1]
#     ins='INSERT INTO fallback (Query,Answer) VALUES("{}","{}");'.format(query,answer)
#     mycursor.execute(ins)
#     mydb.commit()
#     # print("printing message")
#     # print(message)
#     # print(message2)
#     # print(answer)
#     print(mycursor._rowcount,"record inserted")
    
    
class DisplaywebAction(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nlp = spacy.load("en_core_web_md")
        user_input = tracker.latest_message.get("text")
        doc = nlp(user_input)
        openai.api_key=os.getenv('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')
        completions=openai.Completion.create(engine='text-davinci-002',prompt=user_input,max_tokens=1500)
        message=completions.choices[0].text
        answer=message
        print(answer)
        dispatcher.utter_message(answer)
        print(user_input)
        return[]