#!groovy

node {

    try {
        stage 'Test'
            sh 'virtualenv env -p python3.5'
            sh '. env/bin/activate'
            sh 'env/bin/pip install -r requirements.txt'
            sh 'env/bin/python3.5 manage.py test polls.tests_view'
    }

    catch (err) {
        throw err
    }

}
