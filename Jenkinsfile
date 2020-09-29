#!groovy

node {

    try {
        stage 'Test'
            sh 'virtualenv env -p python'
            sh '. env/bin/activate'
            sh 'env/bin/pip install -r requirements.txt'
            sh 'env/bin/python manage.py test polls.tests_view'
    }

    catch (err) {
        throw err
    }

}
