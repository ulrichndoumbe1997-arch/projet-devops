
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        // 1. Recuperation du code depuis GitHub
        stage('Recuperation du code') {
            steps {
                checkout scm
            }
        }

        // 2. Installation des dependances Python
        stage('Installation des dependances') {
            steps {
                bat '"C:\\Users\\ulric\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m pip install -r requirements.txt'

                bat '"C:\\Users\\ulric\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m pip install pytest'
            }
        }

        // 3. Tests automatises et generation du rapport
        stage('Tests automatises') {
            steps {
                bat '"C:\\Users\\ulric\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m pytest -v --junitxml=rapport-tests.xml'

                junit 'rapport-tests.xml'
            }
        }

        // 4. Construction de l'image Docker
        stage('Construction de l image Docker') {
            steps {
                bat '''
                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t mon-application-flask-jenkins .
                '''
            }
        }

        // 5. Deploiement du conteneur Docker
        stage('Deploiement Docker') {
            steps {
                bat '''
                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" rm -f mon-conteneur-jenkins 2>NUL

                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" run -d -p 5001:5000 --name mon-conteneur-jenkins mon-application-flask-jenkins
                '''
            }
        }

        // 6. Verification de l'application apres deploiement
        stage('Verification HTTP') {
            steps {
                bat '''
                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" ps

                    curl.exe -f http://localhost:5001
                '''
            }
        }
    }
}
