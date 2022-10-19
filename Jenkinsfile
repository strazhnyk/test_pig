pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker-hub-creds')
	}
	
  	stages {
	  
  		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
  

		stage('Build') {

			steps {
        sh 'docker build ./api/ -t ${DOCKERHUB_CREDENTIALS_USR}/flask:$BUILD_NUMBER'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push ${DOCKERHUB_CREDENTIALS_USR}/flask:$BUILD_NUMBER'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
			sshPublisher(publishers: [sshPublisherDesc(configName: 'Test-Deploy', transfers: [sshTransfer(excludes: '', execCommand: 'docker-compose down && docker-compose up -d && docker system prune -a -f', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'docker-compose.yml')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])

		}
	}

}
