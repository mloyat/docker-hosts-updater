# docker-hosts-updater
An ultra simple /etc/hosts file updater working with docker based on env variables

Embed it in docker-compose.yml file as a service with the environment variable HOST_LIST

for example :

```
services: 
  hosts-updater:
    image: dankastudio/docker-hosts-updater
    environment:
      HOSTS_LIST: mysite.local;{adminer,mailhog,portainer}.mysite.local
    volumes:
      - /etc/hosts:/opt/hosts
```

It updates the /etc/hosts file appending the listed domain names in HOSTS_LIST.
- Separate multiple domain names by ;
- add multiple subdomains between {} separated by ,

It simply maps the domain name with 127.0.0.1

With docker run :
```
docker run \
    -v /etc/hosts:/opt/hosts \
    -e "HOSTS_LIST={www,adminer,portainer}.dev.loval;dev.local"\
    dankastudio/docker-hosts-updater
