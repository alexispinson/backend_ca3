# backend_ca3

I went back to what I had done for the last two CA, then I added the tests and I improved the security.

First, I will show and explain the tests on the models.
For the first model, the cats, I did not check the types of the variables because the form of django does it automatically, I thus checked the date of birth because it could pose problem. Indeed, the cat can't be born in the future and can't be more than 40 years old (the record is 36), so I had to check this information.
For the second model, the user, I checked the size of the phone number, if the email address had an '@' as well as the size of the password, if it contained a number and a capital letter.
For the views, I check that the status code is 200 and that the right templates are loaded for all pages.
For the urls, I check that the reverse works well.
For these tests, I run them in another database called 'testdb' (you can see how I did it in settings.py).

At the level of security, I have changed the url of the admin that you can see in 'urls.py' but most of my work is in the 'deployed_settings.py', which is the settings to be used when the site goes live. I changed the debug to False, ensured to be in https, changed the authorized hosts, and hid the secret key. To hide it, I used a .env file that I hid in my .gitignore. Then, I just have to load the secret key in my settings file.
