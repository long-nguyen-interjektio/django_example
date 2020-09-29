#!groovy

node {

    try {
        stage 'Test'
            sh 'virtualenv env -p python'
            sh 'source env/bin/activate'
            sh 'ls'
            sh 'pip install -r requirements.txt'
            sh 'python manage.py test polls.tests_view'
    }

    catch (err) {
        throw err
    }

}
