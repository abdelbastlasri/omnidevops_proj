node {
  stage('SCM') {
    checkout scm
  }

  stage('SonarQube Analysis') {
    // Must match the “Name” you set under Global Tool Configuration
    def scannerHome = tool 'SonarScanner'

    // Must match the “Name” of your SonarQube server in Configure System
    withSonarQubeEnv('sonarserver') {
      // Single‑line bat invocation:
      bat "\"${scannerHome}\\bin\\sonar-scanner.bat\" " +
          "-Dsonar.projectKey=omnidevops_proj " +
          "-Dsonar.sources=. " +
          "-Dsonar.host.url=%SONAR_HOST_URL% " +
          "-Dsonar.login=%SONAR_AUTH_TOKEN%"
    }
  }
}
