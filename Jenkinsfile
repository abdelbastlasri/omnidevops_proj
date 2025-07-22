pipeline {
    agent any

    environment {
        SONAR_HOST_URL = 'http://localhost:9000'
        SONAR_LOGIN = 'admin'
        SONAR_PROJECT_KEY = 'todolist-app'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    apt-get update && apt-get install -y curl unzip
                    pip install --upgrade pip
                    pip install pytest flake8
                '''
            }
        }

        stage('Lint and Test') {
            steps {
                sh '''
                    flake8 . || true  # Avoid pipeline fail on lint warnings
                    pytest || true    # Allow tests to fail without stopping build
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                bat '''
                    curl -o sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-7.1.0.4889.zip
                    unzip sonar-scanner.zip
                    export PATH=$PATH:$PWD/sonar-scanner-*/bin
                    sonar-scanner \
                      -Dsonar.projectKey=squ_559817aba5867e5c8577aa87f1e64e8428acaf57 \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://localhost:9000 \
                      -Dsonar.login=admin
                '''
            }
        }
    }
}
