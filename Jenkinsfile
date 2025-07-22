pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'sonarserver'
    }

    stages {
        stage('Test Environment') {
            steps {
                bat 'python --version'
                bat 'pip --version'
                bat 'flake8 --version'
                bat 'sonar-scanner -v'
            }
        }
        stage('Quality Gate Status Check') {
            steps {
                withSonarQubeEnv('sonarserver') {
                bat '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest flake8 sonar-scanner

                flake8 . || exit /b 0
                pytest || exit /b 0

                sonar-scanner \
                -Dsonar.projectKey=todolist-app \
                -Dsonar.sources=. \
                -Dsonar.host.url=%SONAR_HOST_URL% \
                -Dsonar.login=%SONAR_AUTH_TOKEN%

                '''

                }

                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
