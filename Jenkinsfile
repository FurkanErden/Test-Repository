/*pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}*/
node('dockerclusterserver_label') {
    stage 'Checkout'
        checkout scm

    stage 'Build'
        sh 'python3 --version'
        //sh 'docker build -t test/test:latest -f Dockerfile .'
        //sh 'docker push test/test:latest'
}