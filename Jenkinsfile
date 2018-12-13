@Library('promebuilder')_

pipeline {
  agent any
  parameters {
    booleanParam(
      name: 'skip_tests',
      defaultValue: false,
      description: 'Skip all tests'
    )
    booleanParam(
      name: 'force_upload',
      defaultValue: false,
      description: 'Force Anaconda upload, overwriting the same build.'
    )
  }
  environment {
    CONDAENV = "${env.JOB_NAME}_${env.BUILD_NUMBER}".replace('%2F','_').replace('/', '_')
  }
  stages {
    stage('Bootstrap') {
      steps {
        writeFile file: 'buildnum', text: "${env.BUILD_NUMBER}"
        writeFile file: 'commit', text: "${env.GIT_COMMIT}"
        writeFile file: 'branch', text: "${env.GIT_BRANCH}"
        stash(name: "source", useDefaultExcludes: true)
      }
    }
    stage("MultiBuild") {
      parallel {
        stage("Build on Linux") {
          steps {
            doubleArchictecture('linux')
          }
        }
        stage("Build on Windows") {
          steps {
            doubleArchictecture('windows')
          }
        }
      }
    }
  }
  post {
    success {
      deleteDir()
    }
    failure {
      mail to: 'pytho_support@prometeia.com ',
        subject: "PYTHO: Failed Pipeline ${currentBuild.fullDisplayName}",
        body: "Loot at ${env.BUILD_URL}"
    }
  }
}
