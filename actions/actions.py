from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFollowUpMenu(Action):
    def name(self) -> Text:
        return "action_followup_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Envia a pergunta de acompanhamento
        dispatcher.utter_message(response="utter_proxima_pergunta") 
        
        # Em seguida, envia o Menu Principal
        dispatcher.utter_message(response="utter_Menu_doacao")

        return []