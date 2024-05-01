//DECLARATIVE

pipeline {
	agent any
	environment{
		sh " pip --version"
	}
	stages {
		stage('Checkout') {
			steps {
				echo "Build"
				echo "PATH - $PATH"
				echo "BUILD_NUMBER - $env.BUILD_NUMBER"
				echo "BUILD_ID - $env.BUILD_ID"
				echo "JOB_NAME - $env.JOB_NAME"
				echo "BUILD_TAG - $env.BUILD_TAG"
				echo "BUILD_URL - $env.BUILD_URL"
			}
		}
		stage('Package') {
			steps {
				sh "python3 app.py"
			}
		}
		stage('Build Docker Image') {
			steps {
				script {
					dockerImage = docker.build("khalibad/flask-api-rest:${env.BUILD_TAG}")
				}
			}
		}
		stage('Push Docker Image') {
			steps {
				script {
					docker.withRegistry('', 'dockerhub'){
						dockerImage.push();
						dockerImage.push('latest')
					}
				}
			}
		}
	} 
	post {
		always {
			echo 'Im awesome. I run always'
		}
		success {
			echo 'I run when you are successful'
		}
		failure {
			echo 'I run when you fail'
		}
	}
} 
