
pipeline {
    agent any

    environment {
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
        AWS_REGION = 'ap-south-1'
        ECR_REGISTRY = '025881472816.dkr.ecr.ap-south-1.amazonaws.com'
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
                    docker build -t user-service:v2 \
                        -t user-service:build-${BUILD_NUMBER} ./user-service

                    docker build -t product-service:v2 \
                        -t product-service:build-${BUILD_NUMBER} ./product-service

                    docker build -t order-service:v2 \
                        -t order-service:build-${BUILD_NUMBER} ./order-service
                '''
            }
        }

        stage('Login to AWS ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region "$AWS_REGION" |
                    docker login --username AWS --password-stdin "$ECR_REGISTRY"
                '''
            }
        }

        stage('Tag Docker Images') {
            steps {
                sh '''
                    for SERVICE in user-service product-service order-service
                    do
                        docker tag "$SERVICE:v2" \
                            "$ECR_REGISTRY/$SERVICE:v2"

                        docker tag "$SERVICE:build-$BUILD_NUMBER" \
                            "$ECR_REGISTRY/$SERVICE:build-$BUILD_NUMBER"
                    done
                '''
            }
        }

        stage('Push Images to ECR') {
            steps {
                sh '''
                    for SERVICE in user-service product-service order-service
                    do
                        docker push "$ECR_REGISTRY/$SERVICE:v2"
                        docker push "$ECR_REGISTRY/$SERVICE:build-$BUILD_NUMBER"
                    done
                '''
            }
        }

        stage('Verify ECR Images') {
            steps {
                sh '''
                    for SERVICE in user-service product-service order-service
                    do
                        aws ecr describe-images \
                            --repository-name "$SERVICE" \
                            --region "$AWS_REGION"
                    done
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

        stage('Verify Kubernetes') {
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
