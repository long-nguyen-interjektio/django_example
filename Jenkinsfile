#!groovy

node {
    checkout scm
    try {
        stage ('CHECK DIR') {
            sh 'ls -a'
        }
        stage ('run docker') {
            sh './tag-images.sh'
        }
    }

    catch (err) {
        throw err
    }

}
