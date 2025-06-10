# Docker-project
python app deployement on AWS EC2 using Docker
 
# 1.launch an ubuntu ec2 instance and connect via ssh using windows powershell
# 2.Update the system
  -sudo apt update
# 3.Install docker and added it to user group to executing docker command directly
 - sudo apt install -y docker.io
 - sudo usermod -aG docker $USER
# 4.After adding to user group we should have to exit and reconnect our ec2. its done by only using one command.we dont need to exit.
 - newgrp docker
# 5.clone the github repo.
 -git clone <repo_url>
# 6. nevigate to the repository
 - cd <repo>
# 7. build an image 
 - docker build . -t <image_tag>
# 8. run the container in detach mode using image 
 - docker run -d --name <conatiner_name> -p 8000:8000 <image_id>

 #access running application outside by browsing
  http://ec2_public_ip:8000 and
   http://ec2_public_ip:8000/health
