pipeline {
  agent any
  stages {
    stage('update') {
      steps {
        sh 'pip3 install haf -U'
        sh 'pip3 install hafsqlpublish -U'
        sh 'pip3 install hafapiserver -U'
      }
    }
    stage('run test') {
      steps {
        sh 'python -m haf run -c=config.json'
      }
    }
    stage('report') {
      steps {
        sh 'ls data'
      }
    }
  }
}