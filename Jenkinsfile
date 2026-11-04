
pipeline {
    agent any

    environment {
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }

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
                    test -f user-service/app.py
                    test -f product-service/app.py
                    test -f order-service/app.py
                    echo "Project validation successful!"
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker build -t user-service:v2 ./user-service
                    docker build -t product-service:v2 ./product-service
                    docker build -t order-service:v2 ./order-service
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl set image deployment/user-deployment \
                      user-container=user-service:v2

                    kubectl set image deployment/product-deployment \
                      product-container=product-service:v2

                    kubectl set image deployment/order-deployment \
                      order-container=order-service:v2

                    kubectl rollout status deployment/user-deployment
                    kubectl rollout status deployment/product-deployment
                    kubectl rollout status deployment/order-deployment
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    kubectl get deployments
                    kubectl get pods
                    kubectl get services
                '''
            }
        }
    }
}
