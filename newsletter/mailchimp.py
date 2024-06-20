# mailchimp.py
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings

client = MailchimpMarketing.Client()
client.set_config({
    "api_key": settings.MAILCHIMP_API_KEY,
    "server": settings.MAILCHIMP_API_KEY.split('-')[-1]
})


def add_email_to_list(email):
    try:
        response = client.lists.add_list_member(settings.MAILCHIMP_AUDIENCE_ID, {
            "email_address": email,
            "status": "subscribed"
        })
        return response
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        # Log detailed error message
        return {"error": error.text}
