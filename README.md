# alexa-nighttime-stories
Alexa skill that reads nighttime stories. 




#### Dev portal settings

Requires `ngrok`


- Make sure the HTTPS radio button is selected for the "Endpoint" field.

- Enter the HTTPS endpoint from ngrok into the textfield.

- Don't bother with "Account Linking".




It's important to choose the second radio button with the following label because that's what ngrok uses:

```My development endpoint is a subdomain of a 
domain that has a wildcard certificate from a 
certificate authority.```


#### Tools

Test with online emulator: https://echosim.io/


#### Misc

Developed with `flask_ask`, `flask`, and `python3.6`.

For more info, visit [this tutorial](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development) on amazon.