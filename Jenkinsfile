#!groovy

node {
    checkout scm
    try {
        stage 'generate file'
            sh 'ls -a'
    }

    catch (err) {
        throw err
    }

}
