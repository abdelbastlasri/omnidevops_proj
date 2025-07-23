pipeline {
  agent any
  stages {
    stage('SonarQube Analysis') {
      steps {
        // récupère le scanner configuré
        def scannerHome = tool 'SonarScanner'
        // injecte les vars SONAR_HOST_URL et SONAR_AUTH_TOKEN via le serveur nommé 'sonarserver'
        withSonarQubeEnv('sonarserver') {
          // sous Windows : bat, sinon sh
          bat "\"${scannerHome}\\bin\\sonar-scanner.bat\" ^
            -Dsonar.projectKey=omnidevops_proj ^
            -Dsonar.sources=. ^
            -Dsonar.host.url=%SONAR_HOST_URL% ^
            -Dsonar.login=%SONAR_AUTH_TOKEN%"
        }
      }
    }
  }
}
