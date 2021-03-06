## GithubWebhook 

- It is a form of automation for a GitHub project that will prevent
merging impolite pull requests
- The impolite pull request can be detected as the one that has no "pls", "plz", “please”, “appreciate”,
“would be great” phrases in the description

#### _Requirements_ 
 - `npm` should be installed 
 - Latest code from the `master` branch is available at your machine
 - Create a github access token by following this [link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with scope `public_repo` and add it as access_token in data.ini file.
 - Add your github username in the data.ini file and make sure that this user has access of the github repository with which we want to do the integration

## _How to integrate_

Follow the steps in order to run the webhook server

1. #### Install `Requests` python package

```sh
pip3 install requests
```

2. #### Install `flask` python package

```sh
pip3 install flask
```

3. #### Install `localtunnel` npm package

```sh
npm install -g localtunnel
```

4. #### Start the server on the localhost on port 80 by going to the project root location

```sh
python3 app.py
```

> You should see the service up at http://127.0.0.1:80/ saying "Hello World!"

5. #### Open a new terminal window and start the localtunnel to exposes your localhost to the world via public url

```sh
lt --port 80
```

> Open the url, generated by the command, in a web browser and select 'Click to Continue' and you should see the "Hello World!" page. This means now our service is up on a public url.

6. Add the webhook to github repository with which you want to integrate this feature, by following [these](https://hookdeck.com/guides/platforms/post/getting-started-github-webhooks#what-are-github-webhooks) instructions with values:
- `Content type` > "application/json"
- `Which events would you like to trigger this webhook?` > "Pull requests"
- `Payload URL` > public url generated in step #5 and append `/hook`, e.g, https://hot-frog-50.loca.lt/hook

7. Now you're done. To test it raise a PR in the same repository and if the description doesn't contain any of the polite words mentioned below then the PR will be rejected/closed:

- plz
- pls
- please
- appreciate
- would be great

##### Owner
**Nitun Pachauri**