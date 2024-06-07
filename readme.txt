#all commands
makesure you are in the devsearch directory and in that directory the docker file must be there
docker build -t ecsdocker .
docker container run -dit -p 80:80 ecsdocker