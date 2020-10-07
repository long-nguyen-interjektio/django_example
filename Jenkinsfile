#!groovy

node {
    checkout scm
    try {
        stage ('CHECK DIR') {
            sh 'ls -a'
        }
        stage ('GRANT PERMISSION') {
            sh 'groupadd docker'
            sh 'usermod -aG docker $USER'
            sh 'chmod 0700 /var/run/docker.sock'
            sh 'chmod 0700 tag-images.sh Dockerfile'
        }
        stage ('run docker') {
            sh './tag-images.sh'
        }
    }

    catch (err) {
        throw err
    }

}
