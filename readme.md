Start up docker-hosts-updater:

$ docker run \
    --name docker-hosts-updater \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /etc/hosts:/opt/hosts \
    -e "HOSTS_LIST={www,adminer,portainer}.dev.loval;dev.local"\
    dankastudio/docker-hosts-updater