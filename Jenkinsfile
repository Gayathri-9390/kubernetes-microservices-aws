
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Gayathri-9390/kubernetes-microservices-aws.git'
            }
        }

        stage('Validate Project') {
            steps {
                sh '''
                    echo "Validating project..."
                    test -f user-service/app.py
                    test -f product-service/app.py
                    test -f order-service/app.py
                    test -f k8s/user-deployment.yaml
                    test -f k8s/product-deployment.yaml
                    test -f k8s/order-deployment.yaml
                    echo "Validation successful!"
                '''
            }
        }

        stage('Build User Service') {
            steps {
                sh 'docker build -t user-service:v2 ./user-service'
            }
        }

        stage('Build Product Service') {
            steps {
                sh 'docker build -t product-service:v2 ./product-service'
            }
        }

        stage('Build Order Service') {
            steps {
                sh 'docker build -t order-service:v2 ./order-service'
            }
        }

        stage('Verify Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }
}
