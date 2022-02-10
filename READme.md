## GithubWebhook 

- It is a form of automation for a GitHub project that will prevent
merging impolite pull requests
- The impolite pull request can be detected as the one that has no “please”, “appreciate”,
“would be great” phrases in the description

#### _Requirements_ 
 - `npm` should be installed 
 - Latest code from the `master` branch is available at your machine

#### _Prerequisites_

Follow the steps in order to run the webhook server

1. #### Install `Requests` python package

```sh
pip3 install requests
```

2. #### Install `localtunnel` npm package

```sh
npm install -g localtunnel
```

3. #### Start the server on the localhost on port 80 by going to the project root location

```sh
python3 app.py
```

> You should see the service at http://127.0.0.1:80/hook

4. #### Start the localtunnel to exposes your localhost to the world via public url

```sh
lt --port 80
```

5. Add the webhook to github repository by following [these](https://hookdeck.com/guides/platforms/post/getting-started-github-webhooks#what-are-github-webhooks) instruction with:
- `application/json` for the “Content type” dropdown
- `Pull requests` for "Which events would you like to trigger this webhook?"

6. Now raise a PR in the same repository and if the description doesn't contain any of the polite words mentioned below then the PR will be rejected/closed:

- plz
- pls
- please
- appreciate
- would be great

> ### **Note**
> You'd need to create and store the github access token in the data.ini file in order to successfully reject the PR.
> 
> Please follow this [link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create the access token with scope `public_repo` 


##### Owner
**Nitun Pachauri**