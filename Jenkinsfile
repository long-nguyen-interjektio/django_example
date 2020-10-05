#!groovy

node {

    try {
        stage 'Test'
            sh 'tag-images.sh'
    }

    catch (err) {
        throw err
    }

}
