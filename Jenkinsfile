pipeline {
  agent any
  stages {
    stage('update') {
      steps {
        sh '''pip3 install haf -U
pip3 install hafsqlpublish -U
pip3 install hafapiserver -U'''
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