pipeline{
	agent any

	stages{

	   stage('Build')

	   {
	   steps{
	         echo"Build Application"
	                   }
	    }

	    stage('Test')

	     {
	   steps{
	         echo"Testing Application"
	                   }
	    }
	    stage('Deploy')

	     {
	   steps{
	         echo"Deploy Application"
	                   }
	    }
	}

	post {
        always {
            
        }
        failure {
            
            emailext body: 'Summary', subject: 'PipeLine_Status', to: 'rajvadiyadharam@gmail.com'
                }
        }
}
