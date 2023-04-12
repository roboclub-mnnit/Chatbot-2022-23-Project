# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher, Action
import webbrowser
from rasa_sdk.interfaces import Action
from rasa_sdk.events import SlotSet ,EventType
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher , Action
from rasa_sdk.types import DomainDict
from mysql_connectivity import DataUpdate
import spacy
import openai
from dotenv import load_dotenv
load_dotenv()
import os

class ActionTellName(Action):

    def name(self) -> Text:
        return "action_tell_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")
        message = " Hi {}! , what is your mobile number ? ".format(name)
        print (message)
        dispatcher.utter_message(text=message)
        return []

class ActionTellName(Action):

    def name(self) -> Text:
        return "action_tell_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        number = tracker.get_slot("number")
      #  - text : " Hi {name}! , what is your mobile number 📱 ? "
        message = " Yeah , Your mobile number   is {} . Thanks for giving information ".format(number)
        print (message)
        dispatcher.utter_message(text=message)
        return []


class ValidateHealthForm(FormValidationAction):

  def name(self) -> Text:
      return "validate_health_form"

  async def required_slots(
    self,
    slots_mapped_in_domain: List[Text],
    dispatcher: "CollectingDispatcher",
    tracker: "Tracker",
    domain: "DomainDict"
  ) -> List[Text]:
    if tracker.get_slot("confirm_exercise") == True:
      return ["confirm_exercise", "exercise", "sleep", "diet", "stress", "goal"]
    else:
      return ["confirm_exercise", "sleep", "diet", "stress", "goal"]

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

class DisplaywebAction(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nlp = spacy.load("en_core_web_md")
        user_input = tracker.latest_message.get("text")
        doc = nlp(user_input)
        openai.api_key=os.getenv('api')
        completions=openai.Completion.create(engine='text-davinci-002',prompt=user_input,max_tokens=1500)
        message=completions.choices[0].text
        answer=message
        print(answer)
        dispatcher.utter_message(answer)
        DataUpdate(user_input,answer)
        print(user_input)
        return[]