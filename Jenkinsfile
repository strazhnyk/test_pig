pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker-hub-creds')
	}

  stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
  
	stages {

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
		}
	}

}
