pipeline {
    agent any
     environment {
       AWS_DEFAULT_REGION = 'eu-central-1'

    }

    parameters {
        string(defaultValue: "ami-04932daa2567651e7", description: 'AMI', name: 'AMI')
    }
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
                                sh("sudo apt-get install python3-venv -y")
                                sh("python3 -m venv env")
                                sh("sudo source env/bin/activate")
                                sh("python3 setup.py install")


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