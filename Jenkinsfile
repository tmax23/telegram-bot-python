#!/usr/bin/env groovy

pipeline {
  agent any
	environment {
	  IMAGE_NAME = 'tmax23/tg-bot-py:latest'
    TG_BOT_TOKEN = credentials('tg-bot-token')
	}

  stages {

	  stage('Build docker image') {
      steps {
        script {
          sh "echo 'ENV_API_TOKEN=${TG_BOT_TOKEN}' > ./.env"
          withCredentials([usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
            sh "docker build -t ${IMAGE_NAME} ."
            sh "echo $PASS | docker login -u $USER --password-stdin"
            sh "docker push ${IMAGE_NAME}"
          }
				}
      }
    }

    stage('Provision server on AWS') {
      environment {
        AWS_ACCESS_KEY_ID = credentials('aws_access_key_id')
        AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
      }

      steps {
        script {
          dir ('terraform') {
            sh "terraform init"
            EC2_STATUS = sh(
              script: "terraform apply -auto-approve",
              returnStdout: true
              ).trim()

            EC2_PUBLIC_IP = sh(
              script: "terraform output ec2_public_ip",
              returnStdout: true
              ).trim()

          }
        }
      }
    }

		stage('Deploy to EC2') {
			steps {
				script {
            def hasMatch = (EC2_STATUS =~ /(.*)Resources: 0 added, 0 changed, 0 destroyed(.*)/)
            if (!hasMatch) {
              hasMatch = null
              echo "Waiting for EC2 server to initialize"
              sleep(time: 90, unit: "SECONDS")
              }
            hasMatch = null

            def shellCmd = "bash ./server-cmds.sh ${IMAGE_NAME} ${TG_BOT_TOKEN} ${EC2_PUBLIC_IP}"
				    def ec2Instance = "ec2-user@${EC2_PUBLIC_IP}"

				    sshagent(['my-ssh-key']) {
              sh "ssh -o StrictHostKeyChecking=no ${ec2Instance} 'mkdir -p /home/ec2-user/cert'"
              sh "ssh -o StrictHostKeyChecking=no ${ec2Instance} 'mkdir -p /home/ec2-user/nginx'"
              sh "scp -o StrictHostKeyChecking=no ./nginx/mybot.conf ${ec2Instance}:/home/ec2-user/nginx/mybot.conf"

              withCredentials([file(credentialsId: 'private-key-nginx-tg-bot', variable: 'private')]) {
                sh "cat \$private > ./private.key"
              }
              sh "chmod 644 ./private.key"
              sh "scp -o StrictHostKeyChecking=no ./private.key ${ec2Instance}:/home/ec2-user/cert/private.key"

              sh "scp -o StrictHostKeyChecking=no ./cert/public.pem ${ec2Instance}:/home/ec2-user/cert/public.pem"
              sh "scp -o StrictHostKeyChecking=no server-cmds.sh ${ec2Instance}:/home/ec2-user"
				      sh "scp -o StrictHostKeyChecking=no docker-compose.yaml ${ec2Instance}:/home/ec2-user"
							sh "ssh -o StrictHostKeyChecking=no ${ec2Instance} ${shellCmd}"
              sh "curl -F 'url=https://${EC2_PUBLIC_IP}/' -F 'certificate=@/home/ec2-user/cert/public.pem' https://api.telegram.org/bot${TG_BOT_TOKEN}/setWebhook"
				    }

            echo "APP IS READY AT: http://${EC2_PUBLIC_IP}"
			  }
			}
	  }
	}
}
