# Hamravesh Task
## This script takes the target (domain) from the user and obtains all the subdomains using the subfinder tool.
Then, using the nuclei tool, using its templates, the tool displays the information and vulnerabilities in the templates for us.

## Installation
```bash
git clone https://github.com/0xuf/HR.git
cd HR
(change docker-compose.yml file [line 14] address to your server address(can be ip or domain))
docker-compose up --build
```

## Some explanations in case of confusion
```
After installation you can open this url in your browser: http://your_address
you will see swagger-ui page

you can create your account using this address: http://your_server/api/user/create-user/
after register you can get your token address from: http://your_server/api/user/token/

After receiving the token, you can login in the Authorize section at the top of the page with this format: Bearer ReceivedToken
```

Hope you like it ;)
