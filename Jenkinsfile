pipeline {
    agent any



    stages {
         stage("clean up workspace"){
                        steps{
                            dir("http_cats") {
                                deleteDir()
                            }
                        }
                    }
                    stage("download files from git") {
                        steps{
                         sh("git clone https://github.com/karpovichart/http_cats.git")
                        }
                    }
        stage("install") {
            steps {
                dir("http_cats") {

                                sh("python3 -m venv env")
                               script: ''' #!/bin/bash
                                source ./env/bin/activate
                                 python3 setup.py install'''


                }
            }

        }
		stage("tests"){
         steps {
                dir("http_cats") {
                                sh("python3 setup.py pylint --pylint-rcfile=tests/.pylintrc")
								sh("flake8")
								sh("python3 setup.py test")


                }
            }

        }
		stage("build"){
         steps {
                dir("http_cats") {
								sh("python3 setup.py build")
                }
            }

        }
    }
}
