#!groovy

node {
    checkout scm
    try {
        stage ('CHECKOUT') {
            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES.txt'
            def lastChanges = readFile('GIT_CHANGES.txt')
            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"
        }
        stage ('TEST') {
            slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
        }
    }
    catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
        throw err
    }

}
