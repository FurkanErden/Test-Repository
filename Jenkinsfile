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
node('test_dockerserver_label') {
    stage 'Checkout'
        checkout scm

    stage 'Build'
        sh 'python3 --version'
        //sh 'docker build -t FurkanErden/Test-Repository:latest -f Dockerfile .'
        //sh 'docker push FurkanErden/Test-Repository:latest'
}