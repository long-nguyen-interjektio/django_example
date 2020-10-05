#!groovy

node {

    try {
        stage 'Test'
            sh 'ls -a'
            sh 'tag-images.sh'
    }

    catch (err) {
        throw err
    }

}
