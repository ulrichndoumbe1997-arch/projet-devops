
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Recuperation du code') {
            steps {
                checkout scm
            }
        }

        stage('Installation des dependances') {
            steps {
                bat 'py -m pip install -r requirements.txt'
                bat 'py -m pip install pytest'
            }
        }

        stage('Tests automatises') {
            steps {
                bat 'py -m pytest -v'
            }
        }

        stage('Construction de l image Docker') {
            steps {
                bat '''
                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t mon-application-flask-jenkins .
                '''
            }
        }

        stage('Deploiement Docker') {
            steps {
                bat '''
                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" rm -f mon-conteneur-jenkins 2>NUL
                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" run -d -p 5001:5000 --name mon-conteneur-jenkins mon-application-flask-jenkins
                '''
            }
        }
    }
}