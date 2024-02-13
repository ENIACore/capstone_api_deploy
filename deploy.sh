#!/bin/bash

#Ensure environment variables are set, includes ALL environment variables injected into containers
setEnv() {
	export DB_PASSWORD=password >> /etc/profile
	export DB_NAME=vacation >> /etc/profile

	read -p "Do you need to set new domain environment variables for this deployment? (y/n)" env_choice
	if [[ $env_choice == "y" || $env_choice == "Y" ]]; then
		echo "Please enter the domain and sub-domain credentials for this deployment (do not include http or https but do include .com)"

		# Ask for environment variables
		echo "Do not include http/https for following input"
		read -p "Enter the value for DOMAIN: " domain

		# Update environment variables in /etc/profile
		export DOMAIN=$domain >> /etc/profile
		export API_DOMAIN=$api_domain >> /etc/profile

	fi
}

#Check if docker volume needs to be removed
checkVolume() {
	read -p "Would you like to prune docker volumes? This is recommended, the current database will be exported to UWFITS-Run/oldData/dump-<current time>.sql (y/n)" volume_choice
	
	if [[ $volume_choice == "y" || $volume_choice == "Y" ]]; then
		#Export old dump file and append name with current time
		TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
		OUTPUT_FILE="../old_data/dump-$TIMESTAMP.sql"
		docker exec prod_db mysqldump -u root -p$DB_PASSWORD $DB_NAME > "$OUTPUT_FILE"

		docker-compose down

		#Prune docker volume
		docker volume prune --force
	fi
}

#Ensure server is up to date
sudo apt-get update

setEnv

# Prompt for redeploy or deploy
read -p "Is this a deployment on a new machine? If no services will be updated to latest dockerhub images. (y/n)" redeploy_choice

if [[ $redeploy_choice == "y" || $redeploy_choice == "Y" ]]; then
 
	sudo apt-get install docker.io docker-compose -y
	
	#Ensure no images/containers/volumes exist
	y | docker volume prune
	docker container prune -f
	docker image prune -a -f

    
	sudo apt install snapd
	sudo snap install core
	sudo snap refresh core
	sudo snap install --classic certbot
	sudo ln -s /snap/bin/certbot /usr/bin/certbot
	sudo certbot --config-dir /ssl_certs --apache

	echo "Starting production services"
	docker-compose up -d
else
	echo "Stopping running services and pulling in latest images"
	docker-compose down
	docker container prune -f
	docker-compose pull

	echo "Starting new production services"
	docker-compose up -d
fi
