pipeline {
    agent any

    environment {
        // Define your Airflow deployment path
        DEPLOY_PATH = "/home/marwat/Documents/Air-flow"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest validated code from your repo
                git branch: 'main', url: 'https://github.com/irshad-devops/devops-dataopd.git'
            }
        }

        stage('Infrastructure Update') {
            steps {
                dir('terraform') {
                    // Automates the Ops side: Terraform apply
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('Deploy to Airflow') {
            steps {
                // Syncs your DAGs and Scripts to the live server
                sh "cp -r dags/* ${DEPLOY_PATH}/dags/"
                sh "cp -r scripts/* ${DEPLOY_PATH}/scripts/"
                echo 'Deployment Complete!'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline deployed successfully to Airflow!'
        }
    }
}
