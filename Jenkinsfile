pipeline {
    agent any

    environment {
        IMAGE_NAME = 'elevate-task-2-app'
        CONTAINER_NAME = 'elevate-task-2-app'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building the application Docker image...'
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application unit tests...'
                sh 'docker run --rm --entrypoint python ${IMAGE_NAME}:latest -m unittest -v test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application container...'
                sh '''
                    docker rm -f ${CONTAINER_NAME} 2>/dev/null || true
                    docker run -d --name ${CONTAINER_NAME} \
                        --restart unless-stopped \
                        -p 8000:8000 ${IMAGE_NAME}:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'CI/CD pipeline failed. Check the console output.'
        }
    }
}
