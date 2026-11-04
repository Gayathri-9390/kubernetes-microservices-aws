
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
                    echo "Checking project structure..."
                    ls -la
                    test -f user-service/app.py
                    test -f product-service/app.py
                    test -f order-service/app.py
                    test -f k8s/user-deployment.yaml
                    test -f k8s/product-deployment.yaml
                    test -f k8s/order-deployment.yaml
                    echo "Project validation successful!"
                '''
            }
        }
    }
}
