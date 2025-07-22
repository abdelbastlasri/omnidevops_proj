pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    environment {
        SONARQUBE_ENV = 'sonarserver'  
    }

    stages {
        stage('Quality Gate Status Check') {
            steps {
                withSonarQubeEnv('sonarserver') {
                    sh '''
                        
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pip install pytest flake8 sonar-scanner

                       
                        flake8 . || true
                        pytest || true

                        
                        sonar-scanner \
                          -Dsonar.projectKey=todolist-app \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=$SONAR_HOST_URL \
                          -Dsonar.login=$SONAR_AUTH_TOKEN
                    '''
                }

                
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
